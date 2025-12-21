# AudioHardwareBox

**Framework**: Core Audio  
**Kind**: class

Instances of the AudioHardwareBox class encapsulate a single audio box, which is a container for other objects (typically device objects). A box publishes identifying information about itself and can be enabled or disabled. A box’s contents are only available to the system when the box is enabled.

**Availability**:
- Mac Catalyst ?+
- macOS 15.0+

## Declaration

```swift
class AudioHardwareBox
```

## Topics

### Initializers
- [init(id: AudioObjectID)](audiohardwarebox/init(id:).md)
### Instance Properties
- [var clocks: [AudioHardwareClock]](audiohardwarebox/clocks.md)
  An array of AudioHardwareClocks that represent all the clock objects that came out of the given box. Note that until a box is enabled, this list will be empty.
- [var devices: [AudioHardwareDevice]](audiohardwarebox/devices.md)
  An array of AudioHardwareDevices that represent all the device objects that came out of the given box. Note that until a box is enabled, this list will be empty.
- [var enabled: Bool](audiohardwarebox/enabled.md)
  A Bool where a value of true indicates that the box’s contents are available to the system.
- [var hasAudio: Bool](audiohardwarebox/hasaudio.md)
  A Bool where a value of true indicates that the box supports audio.
- [var hasMIDI: Bool](audiohardwarebox/hasmidi.md)
  A Bool where a value of true indicates that the box supports MIDI.
- [var hasVideo: Bool](audiohardwarebox/hasvideo.md)
  A Bool where a value of true indicates that the box supports video.
- [var isProtected: Bool](audiohardwarebox/isprotected.md)
  A Bool where a value of true indicates that the box requires authentication to use.
- [var transportType: UInt32](audiohardwarebox/transporttype.md)
  A UInt32 whose value indicates how the box is connected to the system. Constants for some of the values for this property can be found in the enum in the AudioDevice Constants section of AudioHardwareBase.h
- [var uid: String](audiohardwarebox/uid.md)
  A String that contains a persistent identifier for the box object. A box’s UID is persistent across boots. The content of the UID string is a black box and may contain information that is unique to a particular instance of an box’s hardware or unique to the CPU. Therefore they are not suitable for passing between CPUs or for identifying similar models of hardware.
### Instance Methods
- [func disable() throws](audiohardwarebox/disable.md)
  Make the box’s contents unavailable to the system.
- [func enable() throws](audiohardwarebox/enable.md)
  Make the box’s contents available to the system.

## Relationships

### Inherits From
- [AudioHardwareObject](audiohardwareobject.md)
### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiohardwarebox)*