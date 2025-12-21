# AudioHardwareControl

**Framework**: Core Audio  
**Kind**: class

Instances of the AudioHardwareControl class encapsulate a single audio control, which provides properties that describe/manipulate a particular aspect of the owning object such as gain, mute, data source selection, etc.

**Availability**:
- Mac Catalyst ?+
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
  An array of UInt32s that represent the IDs of all the items available.
- [var booleanValue: Bool](audiohardwarecontrol/booleanvalue.md)
  A Bool that represents the value of the boolean control.
- [var selectedItems: [UInt32]](audiohardwarecontrol/selecteditems.md)
  An array of UInt32s that are the IDs of the items currently selected.
- [var sliderRange: [UInt32]](audiohardwarecontrol/sliderrange.md)
  An array of two UInt32s that represents the inclusive range of values the slider control can take.
- [var sliderValue: UInt32](audiohardwarecontrol/slidervalue.md)
  A UInt32 that represents the value of the slider control.
- [var stereoPanChannels: [UInt32]](audiohardwarecontrol/stereopanchannels.md)
  An array of two UInt32s that indicate which elements of the device the signal is being panned between.
- [var stereoPanValue: Float](audiohardwarecontrol/stereopanvalue.md)
  A Float where 0.0 is full left, 1.0 is full right, and 0.5 is center.
- [var volumeDecibelRange: AudioValueRange](audiohardwarecontrol/volumedecibelrange.md)
  An AudioValueRange that contains the minimum and maximum dB values the control can have.
- [var volumeDecibelValue: Float](audiohardwarecontrol/volumedecibelvalue.md)
  A Float that represents the value of the volume control in dB.
- [var volumeScalarValue: Float](audiohardwarecontrol/volumescalarvalue.md)
  A Float that represents the value of the volume control. The range is between 0.0 and 1.0 (inclusive).
### Instance Methods
- [func convertToDecibels(fromScalar: Float) throws -> Float](audiohardwarecontrol/converttodecibels(fromscalar:).md)
  Convert a volume scalar value to the equivalent dB value.
- [func convertToScalar(fromDecibels: Float) throws -> Float](audiohardwarecontrol/converttoscalar(fromdecibels:).md)
  Convert a volume dB value to the equivalent scalar value.
- [func selectorItemKind(fromID: UInt32) throws -> UInt32](audiohardwarecontrol/selectoritemkind(fromid:).md)
  This property returns a UInt32 that identifies the kind of selector item the item ID refers to.
- [func selectorItemName(fromID: UInt32) throws -> String](audiohardwarecontrol/selectoritemname(fromid:).md)
  Translates the given item ID into a human readable name.
- [func setBooleanValue(Bool) throws](audiohardwarecontrol/setbooleanvalue(_:).md)
  Set the booleanValue property.
- [func setSelectedItems([UInt32]) throws](audiohardwarecontrol/setselecteditems(_:).md)
  Set the selectedItems property.
- [func setSliderValue(UInt32) throws](audiohardwarecontrol/setslidervalue(_:).md)
  Set the sliderValue property.
- [func setStereoPanValue(Float) throws](audiohardwarecontrol/setstereopanvalue(_:).md)
  Set the stereoPanValue property.
- [func setVolumeDecibelValue(Float) throws](audiohardwarecontrol/setvolumedecibelvalue(_:).md)
  Set the decibelScalarValue property.
- [func setVolumeScalarValue(Float) throws](audiohardwarecontrol/setvolumescalarvalue(_:).md)
  Set the volumeScalarValue property.

## Relationships

### Inherits From
- [AudioHardwareObject](audiohardwareobject.md)
### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiohardwarecontrol)*