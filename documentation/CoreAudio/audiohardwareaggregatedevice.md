# AudioHardwareAggregateDevice

**Framework**: Core Audio  
**Kind**: class

**Availability**:
- macOS 15.0+

## Declaration

```swift
class AudioHardwareAggregateDevice
```

## Topics

### Initializers
- [init(id: AudioObjectID)](audiohardwareaggregatedevice/init(id:).md)
### Instance Properties
- [var activeSubdevices: [AudioHardwareClock]](audiohardwareaggregatedevice/activesubdevices.md)
- [var activeSubtaps: [AudioHardwareTap]](audiohardwareaggregatedevice/activesubtaps.md)
- [var clockSource: AudioHardwareObject?](audiohardwareaggregatedevice/clocksource.md)
- [var composition: [String : Any]](audiohardwareaggregatedevice/composition.md)
- [var subdevices: [AudioHardwareClock]](audiohardwareaggregatedevice/subdevices.md)
- [var subtaps: [AudioHardwareTap]](audiohardwareaggregatedevice/subtaps.md)
### Instance Methods
- [func setClockSource(AudioHardwareObject) throws](audiohardwareaggregatedevice/setclocksource(_:).md)
- [func setComposition([String : Any]) throws](audiohardwareaggregatedevice/setcomposition(_:).md)
- [func setSubdevices([AudioHardwareClock]) throws](audiohardwareaggregatedevice/setsubdevices(_:).md)
- [func setSubtaps([AudioHardwareTap]) throws](audiohardwareaggregatedevice/setsubtaps(_:).md)

## Relationships

### Inherits From
- [AudioHardwareDevice](audiohardwaredevice.md)
### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiohardwareaggregatedevice)*