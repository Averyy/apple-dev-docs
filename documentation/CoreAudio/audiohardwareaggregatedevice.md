# AudioHardwareAggregateDevice

**Framework**: Core Audio  
**Kind**: class

Instances of the AudioHardwareAggregateDevice class encapsulate a single audio aggregate device, which is a virtual device that combines the input and output streams of multiple real devices or taps. It also synchonizes the clocks of its subdevices and subtaps when running IO to ensure streams are aligned.

**Availability**:
- Mac Catalyst ?+
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
  An array of AudioHardwareClocks for all the active subdevices in the aggregate device.
- [var activeSubtaps: [AudioHardwareTap]](audiohardwareaggregatedevice/activesubtaps.md)
  An array of AudioHardwareTaps for all the active subtaps in the aggregate device.
- [var clockSource: AudioHardwareObject?](audiohardwareaggregatedevice/clocksource.md)
  The device, clock, or tap that is currently serving as the time base of the aggregate device.
- [var composition: [String : Any]](audiohardwareaggregatedevice/composition.md)
  A Dictionary that describes the composition of the aggregate device. The keys for this CFDicitionary are defined in the AudioAggregateDevice Constants section of AudioHardware.h
- [var subdevices: [AudioHardwareClock]](audiohardwareaggregatedevice/subdevices.md)
  An array of AudioHardwareClocks representing all the devices and clocks, active or inactive, contained in the aggregate device. The order of the items in the array is significant and is used to determine the order of the streams of the aggregate device.
- [var subtaps: [AudioHardwareTap]](audiohardwareaggregatedevice/subtaps.md)
  An array of AudioHardwareTaps for all the subtaps contained in the aggregate device.
### Instance Methods
- [func setClockSource(AudioHardwareObject) throws](audiohardwareaggregatedevice/setclocksource(_:).md)
  Set the clockSource property.
- [func setComposition([String : Any]) throws](audiohardwareaggregatedevice/setcomposition(_:).md)
  Set the composition property.
- [func setSubdevices([AudioHardwareClock]) throws](audiohardwareaggregatedevice/setsubdevices(_:).md)
  Set the subdevices property.
- [func setSubtaps([AudioHardwareTap]) throws](audiohardwareaggregatedevice/setsubtaps(_:).md)
  Set the subtaps property.

## Relationships

### Inherits From
- [AudioHardwareDevice](audiohardwaredevice.md)
### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiohardwareaggregatedevice)*