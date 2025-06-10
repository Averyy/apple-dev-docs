# AudioHardwareControl

**Framework**: Core Audio  
**Kind**: class

**Availability**:
- macOS 15.0+

## Declaration

```swift
class AudioHardwareControl
```

## Topics

### Initializers
- [init(id: AudioObjectID)](audiohardwarecontrol/init(id:).md)
### Instance Properties
- [var availableItems: [UInt32]](audiohardwarecontrol/availableitems.md)
- [var booleanValue: Bool](audiohardwarecontrol/booleanvalue.md)
- [var selectedItems: [UInt32]](audiohardwarecontrol/selecteditems.md)
- [var sliderRange: [UInt32]](audiohardwarecontrol/sliderrange.md)
- [var sliderValue: UInt32](audiohardwarecontrol/slidervalue.md)
- [var stereoPanChannels: [UInt32]](audiohardwarecontrol/stereopanchannels.md)
- [var stereoPanValue: Float](audiohardwarecontrol/stereopanvalue.md)
- [var volumeDecibelRange: AudioValueRange](audiohardwarecontrol/volumedecibelrange.md)
- [var volumeDecibelValue: Float](audiohardwarecontrol/volumedecibelvalue.md)
- [var volumeScalarValue: Float](audiohardwarecontrol/volumescalarvalue.md)
### Instance Methods
- [func convertToDecibels(fromScalar: Float) throws -> Float](audiohardwarecontrol/converttodecibels(fromscalar:).md)
- [func convertToScalar(fromDecibels: Float) throws -> Float](audiohardwarecontrol/converttoscalar(fromdecibels:).md)
- [func selectorItemKind(fromID: UInt32) throws -> UInt32](audiohardwarecontrol/selectoritemkind(fromid:).md)
- [func selectorItemName(fromID: UInt32) throws -> String](audiohardwarecontrol/selectoritemname(fromid:).md)
- [func setBooleanValue(Bool) throws](audiohardwarecontrol/setbooleanvalue(_:).md)
- [func setSelectedItems([UInt32]) throws](audiohardwarecontrol/setselecteditems(_:).md)
- [func setSliderValue(UInt32) throws](audiohardwarecontrol/setslidervalue(_:).md)
- [func setStereoPanValue(Float) throws](audiohardwarecontrol/setstereopanvalue(_:).md)
- [func setVolumeDecibelValue(Float) throws](audiohardwarecontrol/setvolumedecibelvalue(_:).md)
- [func setVolumeScalarValue(Float) throws](audiohardwarecontrol/setvolumescalarvalue(_:).md)

## Relationships

### Inherits From
- [AudioHardwareObject](audiohardwareobject.md)
### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiohardwarecontrol)*