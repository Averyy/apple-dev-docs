# Core Audio

**Framework**: Core Audio  
**Kind**: module

Use the Core Audio framework to interact with device’s audio hardware.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Topics

### Drivers
- [Creating an Audio Server Driver Plug-in](creating-an-audio-server-driver-plug-in.md)
  Build a virtual audio device by creating a custom driver plug-in.
- [Building an Audio Server Plug-in and Driver Extension](building-an-audio-server-plug-in-and-driver-extension.md)
  Create a plug-in and driver extension to support an audio device in macOS.
- [Capturing system audio with Core Audio taps](capturing-system-audio-with-core-audio-taps.md)
  Use a Core Audio tap to capture outgoing audio from a process or group of processes.
### Reference
- [Core Audio Structures](core-audio-structures.md)
- [Core Audio Data Types](core-audio-data-types.md)
- [Core Audio Functions](core-audio-functions.md)
- [Core Audio Constants](core-audio-constants.md)
- [Core Audio Enumerations](core-audio-enumerations.md)
### Classes
- [class AudioHardwareAggregateDevice](audiohardwareaggregatedevice.md)
  Instances of the AudioHardwareAggregateDevice class encapsulate a single audio aggregate device, which is a virtual device that combines the input and output streams of multiple real devices or taps. It also synchonizes the clocks of its subdevices and subtaps when running IO to ensure streams are aligned.
- [class AudioHardwareBox](audiohardwarebox.md)
  Instances of the AudioHardwareBox class encapsulate a single audio box, which is a container for other objects (typically device objects). A box publishes identifying information about itself and can be enabled or disabled. A box’s contents are only available to the system when the box is enabled.
- [class AudioHardwareClock](audiohardwareclock.md)
  Instances of the AudioHardwareClock class encapsulate individual audio clocks. All audio devices inherit from the audio clock class, which provides several base properties and contains a list of control objects. Clock objects can be used as a time source when run in an aggregate device, but contain no IO streams.
- [class AudioHardwareControl](audiohardwarecontrol.md)
  Instances of the AudioHardwareControl class encapsulate a single audio control, which provides properties that describe/manipulate a particular aspect of the owning object such as gain, mute, data source selection, etc.
- [class AudioHardwareDevice](audiohardwaredevice.md)
  Instances of the AudioHardwareDevice class encapsulate individual audio devices. An audio device serves as the basic unit of IO. AudioHardwareDevice provides properties and methods to access and manipulate a device’s state and run IO.
- [class AudioHardwareObject](audiohardwareobject.md)
  The audio HAL provides an abstraction through which applications can access audio hardware. To do this, the HAL provides a small set of audio objects that provide access to the various pieces of the system. Audio objects all have a set of properties that describe and manipulate their state. AudioHardwareObject is a base class for all other audio objects. As such, all classes inherit this set of properties.
- [class AudioHardwarePlugin](audiohardwareplugin.md)
  Instances of the AudioHardwarePlugin class encapsulate a single audio HAL plugin, which is a CFBundle loaded by the HAL as a driver to implement device-specific properties and routines.
- [class AudioHardwareProcess](audiohardwareprocess.md)
  Instances of the AudioHardwareProcess class encapsulate a single audio process, which contains information about a client process connected to the HAL.
- [class AudioHardwareStream](audiohardwarestream.md)
  Instances of the AudioHardwareStream class encapsulate a single audio stream, which represents a single buffer of data for transferring across the user/kernel boundary. As such, AudioStreams are the gatekeepers of format information. Each has its own format and list of available formats.
- [class AudioHardwareSystem](audiohardwaresystem.md)
  The audio objects in the HAL are arranged in a containment hierarchy. The root of the hierarchy is the one and only instance of the system class. The properties of the AudioHardwareSystem describe the process global settings such as the various default devices. The system object also contains all the devices that are available.
- [class AudioHardwareTap](audiohardwaretap.md)
  Instances of the AudioHardwareTap class encapsulate a single audio tap, which can capture outgoing audio from a process or group of processes, and be used as an input stream source in an aggregate device.
- [class CATapDescription](catapdescription.md)
### Protocols
- [protocol PropertyListenerDelegate](propertylistenerdelegate.md)
  A delegate protocol for receiving notifications when properties registered with AudioHardwareObject.addPropertyListener change.
### Structures
- [struct AudioHardwareError](audiohardwareerror.md)
  Represents errors returned by the HAL
- [struct ManagedAudioChannelLayout](managedaudiochannellayout.md)
  This structure is used to specify channel layouts in files and hardware.
### Variables
- [var kAudioDevicePropertyWantsControlsRestored: AudioObjectPropertySelector](kaudiodevicepropertywantscontrolsrestored.md)
- [var kAudioDevicePropertyWantsStreamFormatsRestored: AudioObjectPropertySelector](kaudiodevicepropertywantsstreamformatsrestored.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/CoreAudio)*