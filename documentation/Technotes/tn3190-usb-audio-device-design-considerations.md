# TN3190: USB audio device design considerations

**Framework**: Technotes

Learn the best techniques for designing devices that conform to the USB Audio Device Class specifications.

#### Overview

This document helps you design audio devices that connect to Mac, iPad, and iPhone over USB. Such devices must conform to the *Universal Serial Bus Class Definition for Audio Devices* published by USB Implementers Forum, Inc., also known as the USB-IF ([`usb.org`](https://developer.apple.comhttps://www.usb.org)).

#### Choosing a Version of the Usb Audio Device Class Specification

There are four versions of the USB Audio Device Class (ADC) specification:

- [`Release 1.0`](https://developer.apple.comhttps://usb.org/document-library/audio-device-document-10) was published on March 18, 1998.
- [`Release 2.0`](https://developer.apple.comhttps://usb.org/document-library/usb-device-class-definition-audio-devices-release-20-errata-and-ecn-through-april) was first published on May 31, 2006. The most recent version has ECN and errata through April 2, 2025.
- Release 3.0 was published on September 22, 2016 and has been replaced by Release 4.0.
- [`Release 4.0`](https://developer.apple.comhttps://usb.org/document-library/usb-audio-devices-release-40-and-adopters-agreement) was first published in April 2023. The most recent version has ECN and errata through April 2, 2025.

##### Audio Device Class 1 Adc1

ADC1 introduced the concepts you need to design a compliant audio device. It includes all of the building blocks for describing data flow within your device. However, there are some limitations that you should consider before implementing a new device using ADC1:

1. The ADC1 specification was published prior to the existence of USB 2, and therefore the ADC1 specification assumes that the device is operating on a Full Speed bus. ADC1 is limited to a data transfer polling interval of 1 ms.
2. ADC1 does not provide a robust way to describe and resolve clocks to individual audio streams. Clocking information is encapsulated in the Format Type descriptor in the stream, and the clock is programmed using the data endpoint on that stream. This introduces ambiguity in whether two or more streams are using the same clock. The Apple USB audio driver attempts to determine the clocking model based on the list of sample rates supported by each stream and the synchronization type of the data endpoints, but it isn’t always possible to deduce the intended clocking architecture of an ADC1 device.
3. ADC1 devices have a lower channel count and sample rate limit, as they are limited to data transfer sizes of 1023 bytes per millisecond for Full Speed devices, and 1024 bytes per millisecond for High Speed devices.
4. ADC1 only defines 12 spatial locations for channels, which does not meet the requirements of the latest surround and spatial audio systems.
5. ADC1 does not have a function latency control. Your devices do not have the ability to advertise the internal latency of the audio function to Apple operating systems for synchronization purposes.
6. ADC1 does not have a Connector control in Terminal entities. On iOS and iPadOS, this is used by the operating system to automatically route audio to or from the device when a physical connection is made by the customer. For example when a headset is attached to a USB to 3.5mm adapter.
7. It is possible to build a High Speed USB Audio device which uses ADC1, but it is a violation of the ADC1 specification section **4.6.1.1, Table 4-20**, which requires that the standard Endpoint Descriptor have a *bInterval* of 1. To build a High Speed device which operates as ADC1, the *bInterval* must be set to 4, which is the 1 ms polling interval for a High Speed device. This significantly limits the ability of the audio function to support higher channel counts, sampling rates, and bit depths, as shown in the following table:

| Sampling Rate | Channel Count | Bit Depth/Bit Width | Sync/Async | Bytes/ms (1024 bytes max) |
| --- | --- | --- | --- | --- |
| 44.1 kHz | 2 | 16/16 | Sync | 45 * 2 * 2  = 180 |
| 48 kHz | 4 | 24/24 | Async | 49 * 4 * 3 = 588 |
| 48 kHz | 1 | 24/24 | Async | 49 * 1 * 3 = 147 |
| 96 kHz | 2 | 24/32 | Async | 97 * 2 * 4 = 776 |

A Full Speed bus can transfer a maximum of 1500 bytes (12000 bits) per millisecond including bus overhead, so a 96 kHz 2 in/2 out device is not possible with ADC1.

##### Audio Device Class 2 Adc2

ADC2 inherits all components from ADC1 and adds the Clock Source and Clock Selector descriptors to address shortcomings describing the clocking model in ADC1. In ADC2, device descriptors can specify which clock is attached to which stream. Other characteristics of the clock can be specified, such as whether it is internal or external to the device, whether it is synchronized to the USB Start Of Frame (SOF) clock, or if the clock is valid.

ADC2 is designed to support all bus speeds of the USB transport; Full Speed, High Speed and SuperSpeed. You can build audio devices with significantly increased channel counts and sample rates at High and SuperSpeeds. For example, a High Speed ADC2 device operating with a polling interval of 125 µs can transfer up to 24kB of audio data every millisecond in each direction without saturating the bus.

The following table illustrates how it is possible to achieve significantly higher sampling rates and channel counts with an ADC2 device operating at High Speed with a *bInterval* of 1 (125 µs service interval).

| Sampling Rate | Channel Count | Bit Depth/Bit Width | Sync/Async | Bytes/125 µs (3072 bytes max) |
| --- | --- | --- | --- | --- |
| 96 kHz | 32 | 24/24 | Async | (97 * 32 * 3) / 8 = 1,164 |
| 192 kHz | 32 | 24/32 | Sync | (192 * 32 * 4) / 8 = 3,072 |

On a High Speed bus, a 192 kHz, 32 channel device using a bit width of 32 bits (4 bytes) needs to be implemented as a Synchronous device and must transfer exactly the maximum number of bytes every service interval. This device is allowed to transfer that amount of data in each direction without saturating the High Speed bus.

##### Audio Device Class 3 Adc3

ADC3 adds several improvements for Audio Device Class devices, notably Cluster and Connector descriptors:

- Cluster descriptors provide more detailed information about each channel in a channel cluster. This information can include location or ambisonic information.
- Connector descriptors specify the connector type and other connector attributes.

ADC3 introduces Power Domains which allow a device to save energy. Power domains describe groups of elements which can switch into low power mode. The Apple USB audio driver does not support this functionality.

ADC3 introduced new Audio Function Category codes (compare ADC2, **Table A.7** with ADC3, **Table A.7**). The *HEADPHONE* and *HEADSET_ADAPTER* Audio Function Category codes are used to inform audio routing layers on iOS and iPadOS that a headphone or headset adapter USB device is connected.

ADC3 has a backwards compatibility protocol that requires the first Configuration Descriptor to support an ADC1 or ADC2 Audio Function. The ADC3 Audio Function must be supported by a different USB configuration. The Apple USB audio driver supports ADC3 configurations. However, ADC3 has not been widely adopted by other operating systems and it has been superseded by Audio Device Class 4.

##### Audio Device Class 4 Adc4

Audio Device Class 4, introduced in 2023, resolves the channel count and string limitations of previous versions of the specification:

- Every cluster in a device can support up to 65,535 channels.
- The audio device contains its own string descriptor domain with up to 65,535 string descriptors.
- A Feature Unit Descriptor can support up to 16,378 channels (plus cluster channel 0).

In ADC4, audio building blocks can be grouped and the state of all of the blocks in a group can be modified simultaneously. This has performance benefits for complex devices, as state changes do not need to be set on each block in the group.

> **Note**: The Apple USB audio driver does not currently support Audio Device Class 4 devices.

#### Channel Counts with Adc1 3

Versions 1-3 of the Audio Device Class Specification have channel count limitations that you should be aware of, in addition to the bandwidth limitations of ADC1:

- Clusters in any of these implementations are limited to a maximum of 255 channels.
- If a cluster is transported through a Feature Unit, only a maximum of 61 channels + “cluster channel 0” can be controlled by the Feature Unit.
- On a standard USB device there are a maximum of 255 total strings available to the entire device. A device cannot provide names for 255 channels in addition to common strings like device name, manufacturer name, and serial number.

#### Endpoint Synchronization Types

The *Universal Serial Bus Specification, Revision 2.0* and the *Universal Serial Bus 3.n Specifications* specify that USB Isochronous endpoints have one of four Synchronization Types:

- **No Synchronization**: Should only be used for explicit feedback endpoints and not audio data endpoints.
- **Adaptive**: Indicates that the device will adapt to a data rate chosen by the host, and will either consume or produce audio data at the desired rate. See [`Adaptive data endpoints`](tn3190-usb-audio-device-design-considerations#Adaptive-data-endpoints.md) below for more details.
- **Synchronous**: Indicates that the device will consume or produce audio data at a rate that is synchronous with the USB SOF clock. See [`Synchronous data endpoints`](tn3190-usb-audio-device-design-considerations#Synchronous-data-endpoints.md) below for more details.
- **Asynchronous**: Indicates that the audio data is either being consumed or produced by the device at a rate which is not synchronous with the USB Start Of Frame (SOF) clock. See [`Asynchronous data endpoints`](tn3190-usb-audio-device-design-considerations#Asynchronous-data-endpoints.md) below for more details.

##### Adaptive Data Endpoints

Your device can use an Adaptive data endpoint to adapt to the data rate the host sends or receives.

For example, some early ADC1 USB Audio speakers indicate that they can receive output data at any rate from 5 to 50 kHz. The OUT endpoint does not have to be programmed to receive a specific rate. If the host sends data at 48 kHz, the device must render it at 48 kHz. If the host sends data at 12 kHz, the device must render it at 12 kHz etc.

Per the USB Core Specification 5.12.4.1, a device that uses an Adaptive IN streaming endpoint should also provide an explicit feedback endpoint. The Apple USB Audio driver does not support adaptive feedback endpoints. Adaptive IN streaming endpoints are treated the same as asynchronous IN streaming endpoints.

ADC2 introduced Clock Source entities to address some of the shortcomings with Adaptive Data Endpoints. The Audio Device Class 4 specification, **Section 3.11.4.2** specifically states that this type of endpoint is not recommended for implementation.

##### Synchronous Data Endpoints

If your device specifies a Synchronous data endpoint, the audio data transferred on that endpoint must be synchronous with the USB SOF clock. Your device must use the USB SOF to discipline and lock the audio clock to the SOF, or implement an Asynchronous Sample Rate Converter (ASRC) to adjust the rate of audio data to match the SOF rate.

For example, if a device is using a sample rate of 48 kHz, it should transfer exactly 48 audio samples every millisecond as defined by the SOF tokens on the bus. If it is on a High Speed bus with a polling interval of 125 µs, it should transfer exactly 6 samples every 125 µs.

The *USB Audio* specification does allow for a Virtual Frame Packet (VFP) of the nominal rate ±1 but a carefully designed device should be able to transfer exactly the nominal sample rate if that sample rate is divisible by the transfer interval timing. See section **2.3.1.1 USB Packets** in *Universal Serial Bus Device Class Definition for Audio Data Formats, Release 2.0*.

###### Asynchronous Data Endpoints

If your device specifies an Asynchronous data endpoint, then the data flow will be asynchronous to the USB SOF clock.

For audio input streams (from device to host), the host adapts to the incoming data rate within the tolerance required by the ADC specification. For example, if an input stream is clocked at 48 kHz, your device must provide between 47 and 49 audio samples every millisecond. If the polling interval is 125 µs, your device must deliver between 5 and 7 samples every microframe, and the total number of samples in 8 microframes must remain between 47 and 49. See section **2.3.1.1 USB Packets** in *Universal Serial Bus Device Class Definition for Audio Data Formats, Release 2.0* for more information on this requirement.

For audio output streams (from host to device), your device must provide a way for the device to provide feedback to the host for the desired sample rate. There are two types of feedback:

- **Explicit Feedback**: Feedback is provided on another Isochronous endpoint. See [`Explicit feedback`](tn3190-usb-audio-device-design-considerations#Explicit-feedback.md) below for more details.
- **Implicit Feedback**: Feedback is provided on an Isochronous IN data endpoint. See [`Implicit feedback`](tn3190-usb-audio-device-design-considerations#Implicit-feedback.md) below for more details.

###### Explicit Feedback

Explicit Feedback uses an Isochronous IN Endpoint with a Synchronization Type of No Synchronization. This is an IN endpoint which is part of the same Interface as the data OUT endpoint. The maxPacketSize of the explicit feedback endpoint depends on the speed of the bus and is not related to the version of the ADC specification.

Feedback reporting for Full Speed and High Speed buses must comply with section **5.12.4.2 Feedback** of the *Universal Serial Bus Specification, Revision 2.0*

- **Full Speed**: The feedback endpoint payload must be 3 bytes.
- **High Speed**: The feedback endpoint payload must be 4 bytes.

Feedback reporting for a SuperSpeed endpoint must comply with section **4.4.8.4.1 Explicit Feedback** of the *Universal Serial Bus 3.2 Specification, Revision 1.0*

- **SuperSpeed and above**: The feedback endpoint payload must be 8 bytes.

##### Implicit Feedback

Your device can support implicit feedback if it has input and output streams and both are on the same clock. If the data endpoint on the input stream has a Usage Type of Implicit feedback Data endpoint, the host uses the data rate on the audio input stream to provide the data rate on the audio output stream. It is important that your device produces input data at a consistent rate as quickly as possible after the stream starts. The Apple USB Audio driver does not begin transmitting data on the output stream until it has received consistent clock data from the input stream.

#### Audio Device Class Entity Support

The following section outlines Audio Device Class entities, the version of the specification that describes them, and the Apple operating system support.

##### Input and Output Terminals

Terminals are the interface between the physical world and the logical audio function. Terminals are fully supported by macOS, iOS and iPadOS.

##### Terminal Controls

| Control name | ADC version | Apple OS support | Description |
| --- | --- | --- | --- |
| Copy protect | ADC1-4 | None |  |
| Connector | ADC2-4 | macOS, iOS, iPadOS | See [`Terminal Connector Control`](tn3190-usb-audio-device-design-considerations#Terminal-Connector-Control.md) below for more details. |
| Overload | ADC2-4 | None |  |
| Cluster | ADC2-4 | None | Input Terminals only |
| Underflow | ADC2-4 | None |  |
| Overflow | ADC2-4 | None |  |
| Phantom Power | ADC2 with ECN through April 2, 2025 | macOS | See [`Input Terminal Phantom Power Control`](tn3190-usb-audio-device-design-considerations#Input-Terminal-Phantom-Power-Control.md) below for more details. |

##### Terminal Connector Control

If your audio device has a headset connector with jack detection, use this control to indicate to the OS that input or output channels are in use by the customer. This is used by the operating system to automatically route audio to or from the device.

> **Note**: If you do not provide this control, iOS or iPadOS may automatically route audio to a connector with no physical device attached, resulting in a poor customer experience. For example, a Thunderbolt dock with a built in USB Audio device and a headset jack would get audio routed to it using "last-in-wins" logic, unless the Connector Control is implemented to inform the OS that there is nothing connected. With macOS, if the Connector Control is implemented and there is nothing connected to the physical interface, the audio device will not be able to be selected as an input or output device until the physical device is connected. If a selected device has the physical device removed, the OS will automatically change the audio route if possible.

##### Input Terminal Phantom Power Control

Input Terminals only. Your device can expose phantom power control to macOS. Customers can enable or disable this control through apps like Audio MIDI Setup or Logic Pro for Mac. This is implemented using the Core Audio control `kAudioPhantomPowerControlClassID`.

##### Feature Units

Feature Units describe signal processing capabilities on channels in an audio cluster.

##### Feature Unit Controls

| Control name | ADC version | Apple OS support | Description |
| --- | --- | --- | --- |
| Mute | ADC1-4 | macOS, iOS, iPadOS | See [`Mute Control`](tn3190-usb-audio-device-design-considerations#Mute-Control.md) below for more details. |
| Volume | ADC1-4 | macOS, iOS, iPadOS | See [`Volume Control`](tn3190-usb-audio-device-design-considerations#Volume-Control.md) below for more details. |
| Bass | ADC1-4 | None |  |
| Mid | ADC1-4 | None |  |
| Treble | ADC1-4 | None |  |
| GEQ | ADC1-4 | None |  |
| AGC | ADC1-4 | None |  |
| Delay | ADC1-4 | None |  |
| Bass Boost | ADC1-4 | None |  |
| Loudness | ADC1-4 | None |  |
| Input Gain | ADC1-4 | None | Unsupported. Use Volume control instead. |
| Input Gain Pad | ADC1-4 | None |  |
| Phase Inverter | ADC2-4 | macOS | See [`Phase Inverter Control`](tn3190-usb-audio-device-design-considerations#Phase-Inverter-Control.md) below for more details. |
| Underflow | ADC1-4 | None |  |
| Overflow | ADC1-4 | None |  |
| High‑Pass Filter | ADC2 with ECN through April 2, 2025 | macOS | See [`High-Pass Filter Control`](tn3190-usb-audio-device-design-considerations#High-Pass-Filter-Control.md) below for more details. |

##### Mute Control

The user interface on macOS, iOS, and iPadOS exposes the Mute control on the Feature Unit closest to the physical output of the audio function. If a Feature Unit is immediately upstream of a Mixer Unit, between a physical input (for example, a microphone) and a physical output (for example, speakers), it is used to create a control to enable mixing of audio from the input with other audio flowing to the output. This is published to customers as a **Thru** control in Audio MIDI Setup on macOS, or as a programmable side tone control with no user interface on iOS.

##### Volume Control

The user interface on macOS, iOS, and iPadOS exposes the Volume control on the Feature Unit closest to the physical output of the audio function. If a Feature Unit is immediately upstream of a Mixer Unit, between a physical input (for example, a microphone) and a physical output (for example, speakers), it controls the gain on the physical input signal going into the Mixer Unit. macOS, iOS, or iPadOS does not provide a user interface for sidetone gain.

##### Phase Inverter Control

Supported on macOS for ADC2 and ADC3 devices only. Supported on macOS Tahoe 26 and later, and can be accessed by applications using the Core Audio control  `kAudioPhaseInvertControlClassID`.

##### High Pass Filter Control

Supported on macOS for ADC2 devices only. Support is new with macOS Tahoe 26 and can be implemented by applications using the Core Audio control `kAudioHighPassFilterControlClassID`.

##### Mixer Unit

Mixer Units mix multiple input cluster channels into a single output cluster. Given *N* input channels and *M* output channels, a Mixer Unit provides *N × M* controls to describe how each input channel is mixed to an output channel.

Apple operating systems will not manipulate Mixer Units in your device and they will remain in their default state.

##### Mixer Unit Controls

| Control name | ADC version | Apple OS support |
| --- | --- | --- |
| Mixer | ADC1-4 | None |
| Cluster | ADC2, ADC4 | None |
| Underflow | ADC1-4 | None |
| Overflow | ADC1-4 | None |

##### Selector Unit

Selector Units have multiple input clusters and a single output cluster. The Selector Unit selects one of the input clusters to be sent on the output cluster. On macOS, you can make a selection in the Audio MIDI Setup app. If you use this functionality in your USB audio device, provide a name for each of the clusters entering the Selector Unit by naming the entity, usually the Input Terminal, from which the cluster originates.

##### Selector Unit Controls

| Control name | ADC version | Apple OS support | Description |
| --- | --- | --- | --- |
| Selector | ADC1-4 | macOS | See [`Selector Unit Selector Control`](tn3190-usb-audio-device-design-considerations#Selector-Unit-Selector-Control.md) below for more details. |

##### Selector Unit Selector Control

The Selector Control determines which of the input clusters is presented on the output cluster.

> **Note**: This control is explicit in ADC2 and ADC3, but implicit in ADC1 and ADC4. The Selector Unit does not provide a function if the control is not present.

##### Processing Unit

Apple operating systems do not support Processing Units or controls on them. Processing Units in an active data path will remain in their default state, which should be disabled. There are multiple Processing Units defined in the ADC specifications (Up/Down Mix, Dolby Prologic, etc.).

##### Extension Unit

Apple operating systems do not support Extension Units. Extension Units in an active data path will remain in their default state, which should be disabled. Extension Units cannot be enabled through the Apple USB Audio driver.

##### Effect Unit

Apple operating systems do not support Effect Units or controls on them. Effect Units in an active data path will remain in their default state, which should be disabled. There are multiple Effect Units defined in the ADC specifications (Parametric Equalizer, Reverberation, etc.).

##### Clock Source

Clock Sources were introduced in the ADC2 specification and describe the behavior of a clock. They are fully supported by Apple operating systems.

##### Clock Source Controls

| Control name | ADC version | Apple OS support | Description |
| --- | --- | --- | --- |
| Frequency | ADC2-4 | macOS, iOS, iPadOS | See [`Clock Source Frequency Control`](tn3190-usb-audio-device-design-considerations#Clock-Source-Frequency-Control.md) below for more details. |
| Validity | ADC2-4 | macOS, iOS, iPadOS | See [`Clock Source Validity Control`](tn3190-usb-audio-device-design-considerations#Clock-Source-Validity-Control.md) below for more details. |

##### Clock Source Frequency Control

Sets the frequency of the Clock Source. For Read Only clocks (for example, an external SPDIF clock), use this control to report the current frequency setting of the Clock Source.

##### Clock Source Validity Control

Use the Validity control to describe if a Clock Source has a valid clock on its output pin.

> **Note**: For programmable clocks, your device should not complete the control transaction setting the clock frequency until the clock is valid. For example, if the clock requires a phase-locked loop to stabilize before the clock is valid, your device should wait until that process is complete before returning from the SET CUR request on the frequency.

##### Clock Selector

Clock Selectors were introduced in the ADC2 specification and provide a selection between different Clock Source entities and a Terminal. On macOS, you can make a selection in the Audio MIDI Setup app.

##### Clock Selector Controls

| Control name | ADC version | Apple OS support | Description |
| --- | --- | --- | --- |
| Selector | ADC2-4 | macOS | See [`Clock Selector Selector Control`](tn3190-usb-audio-device-design-considerations#Clock-Selector-Selector-Control.md) below for more details. |

##### Clock Selector Selector Control

Use a Selector control to select one of the input pins on the Clock Selector of your device. Changing a selection removes and recreates the Core Audio formats associated with the Core Audio device.

##### Clock Multiplier

The Clock Multplier is described in ADC1-3 and has been deprecated in ADC4. Apple operating systems do not support Clock Multipliers.

##### Sampling Rate Converter

Apple operating systems do not support Sample Rate Converter (SRC) entities. SRC entities provide a mechanism to describe that data is being converted in your device from one clock domain to another.

##### Connectors Descriptor Adc3 and Connector Entity Descriptor Adc4

Apple operating systems do not support these descriptors.

> **Note**: Don’t confuse an ADC3 Connectors descriptor or an ADC4 Connector Entity Descriptor with the *Connector* control in an Input or Output Terminal, which is supported.

##### Power Domain

Apple operating systems do not support Power Domains. This concept was introduced in the ADC3 specification, to allow for entities to be grouped into Power Domains which can be placed into a low power mode.

#### Audio Streaming Interface Class Specific Descriptors

The USB Audio Device Class Specification describes the following descriptors.

##### Class Specific As Encoder Descriptor

The Class-Specific AS Encoder Descriptor is not supported by Apple operating systems. If present, it will be ignored.

##### Class Specific As Decoder Descriptor

The Class-Specific AS Decoder Descriptor is not supported by Apple operating systems. If present, it will be ignored.

##### Class Specific As Valid Frequency Range Descriptor

The Class-Specific AS Valid Frequency Range Descriptor is not supported by Apple operating systems. This descriptor, introduced in ADC3, allows your device to specify available *Clock Source* frequency ranges on each Alternate Setting of a Streaming Interface.

#### Audio Streaming Interface Controls

The USB Audio Device Class Specification describes the following controls.

##### Active Alternate Setting Control

The Active Alternate Setting Control was introduced in ADC2 and is fully supported by Apple operating systems.

##### Valid Alternate Settings Control

The Valid Alternate Settings Control was introduced in ADC2 and is fully supported by Apple operating systems.

##### Audio Data Format Control

The Audio Data Format Control is not supported by Apple operating systems.

#### Device Naming

Each audio device attached to an Apple host has two name properties associated with it:

- **`kAudioDevicePropertyDeviceUID`**: Core Audio uses a Unique Identifier (UID) string to save and restore customer preferences such as volume, mute, and sample rate.
- **`kAudioDevicePropertyDeviceName`**: The visible name of your device is displayed to customers via user interface elements on macOS, iOS, and iPadOS.

The construction of these properties is described further below.

##### Device Uid Kaudiodevicepropertydeviceuid

For USB audio devices, the `kAudioDevicePropertyDeviceUID` property conforms to the following layout:

AppleUSBAudioEngine:<Company Name>:<Device Name>:<Serial # or LocationID>:N[,M]

- **AppleUSBAudioEngine**: Identifies that this device was published by Apple’s USB Audio driver.
- **<Company Name>**: The *iManufacturer* string in your Device Descriptor. If no *iManufacturer* string is provided, “Unknown Manufacturer” is used.
- **<Device Name>**: The *iProduct* string in your Device Descriptor. If no *iProduct* string is provided, “Unknown USB Audio Device” is used.
- **<Serial Number or LocationID>**: The *iSerialNumber* string in your Device Descriptor. If no *iSerialNumber* string is provided, a unique number based on the USB hub connection tree is used. If two identical USB audio device models are connected to a Mac, iPad, or iPhone, a different number in this part of the Device UID is used.

> **Note**: To achieve the best customer experience, if a device supplies a serial number in the *iSerialNumber* string, that string should be unique for every instance of the device.

- **N[,M]**: The Interface numbers of the streaming interfaces for this audio function. If your device contains a single stream, only *N* will be present. For 2 or more streams, the interface number of each of the additional interfaces will be present in the string.

##### Customer Visible Name Kaudiodevicepropertydevicename

The Apple USB audio driver determines the name string of your devices using the following sequence:

1. If all of the streaming interfaces in an audio function are on the same clock, **and** there is more than one streaming interface, **and** the Control Interface has a string represented in the *iInterface* field of that Control Interface, then that string is used to name the device.
2. If that fails, and there is at least one Output Streaming Interface, then the *iInterface* string of the **first** Output Streaming Interface is used.
3. If that fails, and there is at least one Input Streaming Interface, then the *iInterface* string of the **first** Input Streaming Interface is used.
4. If that fails and the Control Interface has an *iInterface* string, it is used.
5. If that fails, the *iProduct* name from the Device Descriptor is used.
6. If all of the above fails, the name “USB Audio Device” is used.

You should avoid generic names like “USB Audio Device”.

#### Supported Audio Formats

The Apple USB Audio driver supports the following audio data formats.

| Format | Defined in the ADC1 spec *(Universal Serial Bus Device Class Definitions for Audio Data Formats Release 1.0)* | Defined in the ADC2 spec *(Universal Serial Bus Device Class Definitions for Audio Data Formats Release 2.0)* |
| --- | --- | --- |
| Type I PCM | Section 2.2.6.1 | Section 2.3.1.7.1 |
| Type I PCM8 | Section 2.2.6.2 | Section 2.3.1.7.2 |
| Type I IEEE_FLOAT | Section 2.2.6.3 | Section 2.3.1.7.3 |
| Type I ALaw and µLaw | Section 2.2.6.4 | Section 2.3.1.7.4 |
| Type III IEC1937AC3 | Section 2.4.1 | Section 2.3.3 |

#### Specifying Channel Locations to Core Audio

##### Adc1adc2 Spatial Designations to Core Audio Channel Labels

ADC1 provides 12 spatial location positions for Clusters. ADC2 preserves those same 12 locations and provides 15 more, for a total of 27 spatial locations. The following table shows the mapping between USB ADC1 and ADC2 spatial locations and the Audio Channel Labels used in Core Audio.

| ADC1/ADC2 Designation (note: ADC2 designations are in bold) | Core Audio Channel Label |
| --- | --- |
| **FL** - Front Left | `kAudioChannelLabel_Left` |
| **FR** - Front Right | `kAudioChannelLabel_Right` |
| **FC** - Front Center | `kAudioChannelLabel_Center` |
| **LFE** - Low Frequency Enhancement/Effects | `kAudioChannelLabel_LFEScreen` |
| Ls/**BL** - Left Surround/Back Left | `kAudioChannelLabel_LeftSurround` |
| Rs/**BR** - Right Surround/Back Right | `kAudioChannelLabel_RightSurround` |
| Lc/**FLC** - (Front) Left of Center | `kAudioChannelLabel_LeftCenter` |
| Rc/**FRC** - (Front) Right of Center | `kAudioChannelLabel_RightCenter` |
| S/**BC** - Surround/Back Center | `kAudioChannelLabel_CenterSurround` |
| Sl/**SL** - Side Left | `kAudioChannelLabel_LeftWide` |
| Sr/**SR** - Side Right | `kAudioChannelLabel_RightWide` |
| T/**TC** - Top (Center) | Unmapped |

| ADC2 Designation (note: ADC1 does not have these) | Core Audio Channel Label |
| --- | --- |
| **TFL** - Top Front Left | `kAudioChannelLabel_LeftTopFront` |
| **TFC** - Top Front Center | `kAudioChannelLabel_CenterTopFront` |
| **TFR** - Top Front Right | `kAudioChannelLabel_RightTopFront` |
| **TBL** - Top Back Left | `kAudioChannelLabel_LeftTopRear` |
| **TBC** - Top Back Center | `kAudioChannelLabel_CenterTopRear` |
| **TBR** - Top Back Right | `kAudioChannelLabel_RightTopRear` |
| **TFLC** - Top Front Left of Center | Unmapped |
| **TFRC** - Top Front Right of Center | Unmapped |
| **LLFE** - Left Low Frequency Effects | Unmapped |
| **RLFE** - Right Low Frequency Effects | Unmapped |
| **TSL** - Top Side Left | `kAudioChannelLabel_LeftTopMiddle` |
| **TSR** - Top Side Right | `kAudioChannelLabel_RightTopMiddle` |
| **BC** - Bottom Center | Unmapped |
| **BLC** - Back Left of Center | `kAudioChannelLabel_RearSurroundLeft` |
| **BRC** - Back Right of Center | `kAudioChannelLabel_RearSurroundRight` |

##### Designing a Device to Meet Predefined Layouts in Core Audio

Core Audio has predefined Layout Tags (see *AudioChannelLayoutTag*). Your device can specify its output channels such that it will automatically be recognized as one of the following predefined layouts.

##### Kaudiochannellayouttagatmos512

| Core Audio Designation | ADC2 Designation |
| --- | --- |
| `kAudioChannelLabel_Left` | **FL** |
| `kAudioChannelLabel_Right` | **FR** |
| `kAudioChannelLabel_Center` | **FC** |
| `kAudioChannelLabel_LFEScreen` | **LFE** |
| `kAudioChannelLabel_LeftSurround` | **BL** |
| `kAudioChannelLabel_RightSurround` | **BR** |
| `kAudioChannelLabel_LeftTopMiddle` | **TSL** |
| `kAudioChannelLabel_RightTopMiddle` | **TSR** |

##### Kaudiochannellayouttagatmos514

| Core Audio Designation | ADC2 Designation |
| --- | --- |
| `kAudioChannelLabel_Left` | **FL** |
| `kAudioChannelLabel_Right` | **FR** |
| `kAudioChannelLabel_Center` | **FC** |
| `kAudioChannelLabel_LFEScreen` | **LFE** |
| `kAudioChannelLabel_LeftSurround` | **BL** |
| `kAudioChannelLabel_RightSurround` | **BR** |
| `kAudioChannelLabel_LeftTopFront` | **TFL** |
| `kAudioChannelLabel_RightTopFront` | **TFR** |
| `kAudioChannelLabel_LeftTopRear` | **TBL** |
| `kAudioChannelLabel_RightTopRear` | **TBR** |

##### Kaudiochannellayouttagatmos712

| Core Audio Designation | ADC2 Designation |
| --- | --- |
| `kAudioChannelLabel_Left` | **FL** |
| `kAudioChannelLabel_Right` | **FR** |
| `kAudioChannelLabel_Center` | **FC** |
| `kAudioChannelLabel_LFEScreen` | **LFE** |
| `kAudioChannelLabel_LeftSurround` | **BL** |
| `kAudioChannelLabel_RightSurround` | **BR** |
| `kAudioChannelLabel_RearSurroundLeft` | **BLC** |
| `kAudioChannelLabel_RearSurroundRight` | **BRC** |
| `kAudioChannelLabel_LeftTopMiddle` | **TSL** |
| `kAudioChannelLabel_RightTopMiddle` | **TSR** |

##### Kaudiochannellayouttagatmos714

| Core Audio Designation | ADC2 Designation |
| --- | --- |
| `kAudioChannelLabel_Left` | **FL** |
| `kAudioChannelLabel_Right` | **FR** |
| `kAudioChannelLabel_Center` | **FC** |
| `kAudioChannelLabel_LFEScreen` | **LFE** |
| `kAudioChannelLabel_LeftSurround` | **BL** |
| `kAudioChannelLabel_RightSurround` | **BR** |
| `kAudioChannelLabel_RearSurroundLeft` | **BLC** |
| `kAudioChannelLabel_RearSurroundRight` | **BRC** |
| `kAudioChannelLabel_LeftTopFront` | **TFL** |
| `kAudioChannelLabel_RightTopFront` | **TFR** |
| `kAudioChannelLabel_LeftTopRear` | **TBL** |
| `kAudioChannelLabel_RightTopRear` | **TBR** |

##### Kaudiochannellayouttagatmos916

| Core Audio Designation | ADC2 Designation |
| --- | --- |
| `kAudioChannelLabel_Left` | **FL** |
| `kAudioChannelLabel_Right` | **FR** |
| `kAudioChannelLabel_Center` | **FC** |
| `kAudioChannelLabel_LFEScreen` | **LFE** |
| `kAudioChannelLabel_LeftSurround` | **BL** |
| `kAudioChannelLabel_RightSurround` | **BR** |
| `kAudioChannelLabel_RearSurroundLeft` | **BLC** |
| `kAudioChannelLabel_RearSurroundRight` | **BRC** |
| `kAudioChannelLabel_LeftWide` | **SL** |
| `kAudioChannelLabel_RightWide` | **SR** |
| `kAudioChannelLabel_LeftTopFront` | **TFL** |
| `kAudioChannelLabel_RightTopFront` | **TFR** |
| `kAudioChannelLabel_LeftTopMiddle` | **TSL** |
| `kAudioChannelLabel_RightTopMiddle` | **TSR** |
| `kAudioChannelLabel_LeftTopRear` | **TBL** |
| `kAudioChannelLabel_RightTopRear` | **TBR** |

#### Extending the Apple Usb Audio Class Driver

You can augment the Apple USB Audio class driver by providing a codeless driver extension (dext) with a property list file that uses the `com.apple.driver.AppleUSBMergeNub` driver in the kernel to add one or more of these properties to the [`IOUSBHostDevice`](https://developer.apple.comhttps://developer.apple.com/documentation/usbdriverkit/iousbhostdevice) service or the [`IOUSBHostInterface`](https://developer.apple.comhttps://developer.apple.com/documentation/usbdriverkit/iousbhostinterface) service for your device:

- `IOAudioDeviceConfigurationApplication`
- `IOAudioEngineInputSampleLatency`
- `IOAudioEngineOutputSampleLatency`
- `IOAudioEngineIsHidden`
- `InhibitAudioClassDriver`

##### Ioaudiodeviceconfigurationapplication

This property, attached to the `IOUSBHostDevice` service, specifies the Bundle ID of your device’s configuration app. Customers can use this to launch your app via Audio MIDI Setup’s “*Configure device…*” pop-up menu.

```xml
<key>IOAudioDeviceConfigurationApplication</key>
<string>com.example.configuration.application.bundleid</string>
```

##### Latency Controls

The Apple USB audio driver supports the standard Latency Control defined in ADC2 **Section 5.2.4.8**. Your device should report latency using the Latency Control instead of the following mechanism. For existing devices that do not support the Latency Control, you can specify your device’s latency using the `IOAudioEngineInputSampleLatency` and `IOAudioEngineOutputSampleLatency` properties.

##### Ioaudioengineinputsamplelatency

This property, attached to the `IOUSBHostInterface` service, specifies the time delay, in samples, between an audio signal being received on a device physical input connector and the sample being transferred to the host over USB. It should be specified for each sample rate that the device supports.

```xml
<key>IOAudioEngineInputSampleLatency</key>
<dict>
    <key>192000</key>
    <integer>100</integer>
    <key>176400</key>
    <integer>100</integer>
    <key>96000</key>
    <integer>50</integer>
    <key>88200</key>
    <integer>50</integer>
    <key>48000</key>
    <integer>25</integer>
    <key>44100</key>
    <integer>25</integer>
</dict>
```

##### Ioaudioengineoutputsamplelatency

This property, attached to the `IOUSBHostInterface` service, specifies the time delay, in samples, between an audio sample being received on the device over USB to the signal being presented on a device physical output connector. It should be specified for each sample rate that the device supports.

```xml
<key>IOAudioEngineOutputSampleLatency</key>
<dict>
    <key>192000</key>
    <integer>100</integer>
    <key>176400</key>
    <integer>100</integer>
    <key>96000</key>
    <integer>50</integer>
    <key>88200</key>
    <integer>50</integer>
    <key>48000</key>
    <integer>25</integer>
    <key>44100</key>
    <integer>25</integer>
</dict>
```

##### Ioaudioengineishidden

This legacy property is deprecated and will be removed in a future operating system release.

##### Inhibitaudioclassdriver

Apple recommends using the built-in audio class driver provided with macOS, iOS, and iPadOS. If your device requires a custom driver, a driver extension (dext) can inhibit the loading of Apple’s USB Audio class driver using standard driver matching. If your driver is an AudioServerPlugin with no dext, you must provide and install a codeless dext to inhibit loading of the Apple USB audio driver.

This property is attached to the `IOUSBHostDevice` service. The Apple USB Audio driver will not load or provide audio services for the device if this key is set to true.

```xml
<key>InhibitAudioClassDriver</key>
<true/>
```

##### Example Codeless Dext Plist

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>CFBundleDevelopmentRegion</key>
    <string>$(DEVELOPMENT_LANGUAGE)</string>
    <key>CFBundleExecutable</key>
    <string>$(EXECUTABLE_NAME)</string>
    <key>CFBundleIdentifier</key>
    <string>$(PRODUCT_BUNDLE_IDENTIFIER)</string>
    <key>CFBundleInfoDictionaryVersion</key>
    <string>6.0</string>
    <key>CFBundleName</key>
    <string>$(PRODUCT_NAME)</string>
    <key>CFBundlePackageType</key>
    <string>$(PRODUCT_BUNDLE_PACKAGE_TYPE)</string>
    <key>CFBundleShortVersionString</key>
    <string>1.0</string>
    <key>CFBundleVersion</key>
    <string>1</string>
    <key>IOKitPersonalities</key>
    <dict>
        <key>Example_Override_IOUSBHostDevice</key>
        <dict>
            <key>CFBundleIdentifier</key>
            <string>$(PRODUCT_BUNDLE_IDENTIFIER)</string>
            <key>CFBundleIdentifierKernel</key>
            <string>com.apple.driver.AppleUSBMergeNub</string>
            <key>IOClass</key>
            <string>AppleUSBMergeNub</string>
            <key>IOProviderClass</key>
            <string>IOUSBHostDevice</string>
            <key>IOProviderMergeProperties</key>
            <dict>
                <key>USB Product Name</key>
                <string>Example Overridden Product Name</string>
                <key>IOAudioDeviceConfigurationApplication</key>
                <string>com.example.configuration.application.bundleid</string>
                <key>InhibitAudioClassDriver</key>
                <true/>
            </dict>
            <key>IOUserClass</key>
            <string>ExampleUACOverridesCodelessDext</string>
            <key>idProduct</key>
            <integer>XXXX</integer>
            <key>idVendor</key>
            <integer>XXXX</integer>
        </dict>
        <key>Example_Override_IOUSBHostInterface_Streaming_In</key>
        <dict>
            <key>CFBundleIdentifier</key>
            <string>$(PRODUCT_BUNDLE_IDENTIFIER)</string>
            <key>CFBundleIdentifierKernel</key>
            <string>com.apple.driver.AppleUSBMergeNub</string>
            <key>IOClass</key>
            <string>AppleUSBMergeNub</string>
            <key>IOProviderClass</key>
            <string>IOUSBHostInterface</string>
            <key>IOProviderMergeProperties</key>
            <dict>
                <key>IOAudioEngineInputSampleLatency</key>
                <dict>
                    <key>192000</key>
                    <integer>100</integer>
                    <key>176400</key>
                    <integer>100</integer>
                    <key>96000</key>
                    <integer>50</integer>
                    <key>88200</key>
                    <integer>50</integer>
                    <key>48000</key>
                    <integer>25</integer>
                    <key>44100</key>
                    <integer>25</integer>
                </dict>
                <key>USB Interface Name</key>
                <string>Example Overridden Interface Name</string>
            </dict>
            <key>IOUserClass</key>
            <string>ExampleUACOverridesCodelessDext</string>
            <key>bConfigurationValue</key>
            <integer>1</integer>
            <key>bInterfaceNumber</key>
            <integer>2</integer>
            <key>idProduct</key>
            <integer>XXXX</integer>
            <key>idVendor</key>
            <integer>XXXX</integer>
        </dict>
        <key>Example_Override_IOUSBHostInterface_Streaming_Out</key>
        <dict>
            <key>CFBundleIdentifier</key>
            <string>$(PRODUCT_BUNDLE_IDENTIFIER)</string>
            <key>CFBundleIdentifierKernel</key>
            <string>com.apple.driver.AppleUSBMergeNub</string>
            <key>IOClass</key>
            <string>AppleUSBMergeNub</string>
            <key>IOProviderClass</key>
            <string>IOUSBHostInterface</string>
            <key>IOProviderMergeProperties</key>
            <dict>
                <key>IOAudioEngineOutputSampleLatency</key>
                <dict>
                    <key>192000</key>
                    <integer>100</integer>
                    <key>176400</key>
                    <integer>100</integer>
                    <key>96000</key>
                    <integer>50</integer>
                    <key>88200</key>
                    <integer>50</integer>
                    <key>48000</key>
                    <integer>25</integer>
                    <key>44100</key>
                    <integer>25</integer>
                </dict>
                <key>USB Interface Name</key>
                <string>Example Overridden Interface Name</string>
            </dict>
            <key>IOUserClass</key>
            <string>ExampleUACOverridesCodelessDext</string>
            <key>bConfigurationValue</key>
            <integer>1</integer>
            <key>bInterfaceNumber</key>
            <integer>1</integer>
            <key>idProduct</key>
            <integer>XXXX</integer>
            <key>idVendor</key>
            <integer>XXXX</integer>
        </dict>
    </dict>
    <key>OSBundleUsageDescription</key>
    <string></string>
</dict>
</plist>
```

#### Other Matching Considerations

Beginning on macOS Tahoe 26, Apple no longer publishes kernel IOServices based on the deprecated IOAudioFamily. If your audio device provides additional, non-class USB interfaces for control, you may need to update your software.

The following IOServices previously published by AppleUSBAudio.kext are no longer created on macOS Tahoe 26:

- `AppleUSBAudioEngine`
- `AppleUSBAudioDevice`
- `AppleUSBAudioStream`

Any properties previously published by those services in the [`IORegistry`](https://developer.apple.comhttps://developer.apple.com/documentation/installer_js/ioregistry) are no longer available.

If your application depends on AppleUSBAudio.kext IOAudioFamily services, it will need to be updated.

Please see Developer support below if you need further guidance on making associations between a Core Audio device AudioObjectID and its corresponding USB io_service_t.

#### Developer Support

If you have questions regarding USB Audio Class support, please contact Apple through [`Feedback Assistant`](https://developer.apple.comapplefeedback://new?form_identifier=dev.tech&answers%5B%3Aarea%5D=seedmacos%3Ausbaudio) selecting the following option:

Developer Technologies & SDKs > USB Audio

To learn more about how to use Feedback Assistant, see [`Bug Reporting`](https://developer.apple.comhttps://developer.apple.com/bug-reporting/).

#### Revision History

- **2025-10-07** First published. Obsoletes TN2274.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3190-usb-audio-device-design-considerations)*