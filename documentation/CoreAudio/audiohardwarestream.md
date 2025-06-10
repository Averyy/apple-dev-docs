# AudioHardwareStream

**Framework**: Core Audio  
**Kind**: class

**Availability**:
- macOS 15.0+

## Declaration

```swift
class AudioHardwareStream
```

## Topics

### Initializers
- [init(id: AudioObjectID)](audiohardwarestream/init(id:).md)
### Instance Properties
- [var availablePhysicalFormats: [AudioStreamRangedDescription]](audiohardwarestream/availablephysicalformats.md)
- [var availableVirtualFormats: [AudioStreamRangedDescription]](audiohardwarestream/availablevirtualformats.md)
- [var direction: AudioHardwareDirection](audiohardwarestream/direction.md)
- [var isActive: Bool](audiohardwarestream/isactive.md)
- [var latency: Int](audiohardwarestream/latency.md)
- [var physicalFormat: AudioStreamBasicDescription](audiohardwarestream/physicalformat.md)
- [var startingChannel: Int](audiohardwarestream/startingchannel.md)
- [var terminalType: UInt32](audiohardwarestream/terminaltype.md)
- [var virtualFormat: AudioStreamBasicDescription](audiohardwarestream/virtualformat.md)
### Instance Methods
- [func setIsActive(Bool) throws](audiohardwarestream/setisactive(_:).md)
- [func setPhysicalFormat(AudioStreamBasicDescription) throws](audiohardwarestream/setphysicalformat(_:).md)
- [func setVirtualFormat(AudioStreamBasicDescription) throws](audiohardwarestream/setvirtualformat(_:).md)

## Relationships

### Inherits From
- [AudioHardwareObject](audiohardwareobject.md)
### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiohardwarestream)*