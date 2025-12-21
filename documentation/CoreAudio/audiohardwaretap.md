# AudioHardwareTap

**Framework**: Core Audio  
**Kind**: class

Instances of the AudioHardwareTap class encapsulate a single audio tap, which can capture outgoing audio from a process or group of processes, and be used as an input stream source in an aggregate device.

**Availability**:
- macOS 15.0+

## Declaration

```swift
class AudioHardwareTap
```

## Topics

### Initializers
- [init(id: AudioObjectID)](audiohardwaretap/init(id:).md)
### Instance Properties
- [var description: CATapDescription](audiohardwaretap/description.md)
  The CATapDescription that describes the configuration of this tap.
- [var format: AudioStreamBasicDescription](audiohardwaretap/format.md)
  An AudioStreamBasicDescription that describes the current data format for the tap. This is the format of the data that will be accessible in any aggregate device that contains the tap.
- [var uid: String](audiohardwaretap/uid.md)
  A String that contains a persistent identifier for the tap. A tap’s UID persists until the tap is destroyed.
### Instance Methods
- [func setDescription(CATapDescription) throws](audiohardwaretap/setdescription(_:).md)
  Set the description property.

## Relationships

### Inherits From
- [AudioHardwareObject](audiohardwareobject.md)
### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiohardwaretap)*