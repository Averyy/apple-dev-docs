# kMIDIPropertyUniqueID

**Framework**: Core MIDI  
**Kind**: var

The unique identifier of a device, entity, or, endpoint.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.0+
- visionOS 1.0+

## Declaration

```swift
let kMIDIPropertyUniqueID: CFString
```

#### Discussion

The system assigns unique IDs to all objects. You may set this property on virtual endpoints; however, doing so may fail if the ID isn’t unique.

This property value is an integer.

## See Also

- [let kMIDIPropertyName: CFString](kmidipropertyname.md)
  A name for a device, entity, or endpoint.
- [let kMIDIPropertyModel: CFString](kmidipropertymodel.md)
  The model name of a device or endpoint.
- [let kMIDIPropertyManufacturer: CFString](kmidipropertymanufacturer.md)
  The manufacturer name of a device or endpoint.
- [let kMIDIPropertyDeviceID: CFString](kmidipropertydeviceid.md)
  The user-visible System Exclusive (SysEx) identifier of a device or entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/kmidipropertyuniqueid)*