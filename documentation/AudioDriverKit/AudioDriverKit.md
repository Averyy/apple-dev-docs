# AudioDriverKit

**Framework**: AudioDriverKit  
**Kind**: module

Develop drivers for audio devices.

**Availability**:
- DriverKit 21.0+

#### Overview

The AudioDriverKit framework supports the development of [`DriverKit`](https://developer.apple.com/documentation/DriverKit)-based audio extensions that communicate with the CoreAudio HAL. AudioDriverKit handles all of the necessary user client communication between the CoreAudio HAL and the driver extension, which eliminates the need to implement an audio server plug-in. You can also integrate with transport-based driver extension frameworks like [`PCIDriverKit`](https://developer.apple.com/documentation/PCIDriverKit).

Develop your driver by subclassing [`IOUserAudioDriver`](iouseraudiodriver.md). On macOS, use the [`System Extensions`](https://developer.apple.com/documentation/SystemExtensions) framework to install and upgrade your driver. On iPadOS, the system automatically discovers and upgrades drivers along with their host apps.

> **Note**:  AudioDriverKit is available on macOS for Intel and Apple Silicon devices, and on iPadOS for devices with an M-series processor.

## Topics

### Essentials
- [IOUserAudioObject](iouseraudioobject.md)
  The base class for most classes in the framework.
- [IOUserAudioDriver](iouseraudiodriver.md)
  A DriverKit provider object that manages communications with an audio device.
- [DriverKit Audio Family](../BundleResources/Entitlements/com.apple.developer.driverkit.family.audio.md)
  A Boolean value that indicates whether the device supports audio functionality.
- [Creating an audio device driver](creating-an-audio-device-driver.md)
  Implement a configurable audio input source as a driver extension that runs in user space in macOS and iPadOS.
### Working with Audio Devices
- [IOUserAudioClockDevice](iouseraudioclockdevice.md)
  An audio clock device object, used to synchronize and perform I/O.
- [IOUserAudioDevice](iouseraudiodevice.md)
  An audio clock device object that handles the configurations for running I/O.
### Containing Audio Objects
- [IOUserAudioBox](iouseraudiobox.md)
  A container for other audio objects, typically audio devices and audio clock devices.
### Working with Audio Streams
- [IOUserAudioStream](iouseraudiostream.md)
  An audio object that performs I/O for an audio device.
### Using Audio Controls
- [IOUserAudioControl](iouseraudiocontrol.md)
  The base class for audio control objects.
- [IOUserAudioBooleanControl](iouseraudiobooleancontrol.md)
  A control object that supports setting a Boolean value.
- [IOUserAudioStereoPanControl](iouseraudiostereopancontrol.md)
  A control object that supports panning between stereo channels.
- [IOUserAudioSliderControl](iouseraudioslidercontrol.md)
  A control object that supports setting a 32-bit integer value.
- [IOUserAudioSelectorControl](iouseraudioselectorcontrol.md)
  A control object that supports selecting from a set of values.
- [IOUserAudioLevelControl](iouseraudiolevelcontrol.md)
  A control object that supports setting an audio level, with either scalar or decibel values.
### Supporting Types
- [IOUserAudioReservedConfigChangeAction](audiodriverkit/iouseraudioreservedconfigchangeaction.md)
  Identifiers for object state changes that require a configuration change.
### Namespaces
- [AudioDriverKit](audiodriverkit.md)
### Macros
- [DebugMsg](debugmsg.md)
- [FailIf](failif.md)
- [FailIfError](failiferror.md)
- [FailIfNULL](failifnull.md)
- [kIOUserAudioDriverUserClientType](kiouseraudiodriveruserclienttype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/AudioDriverKit)*