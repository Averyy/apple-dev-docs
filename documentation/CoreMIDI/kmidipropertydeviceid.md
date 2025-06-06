# kMIDIPropertyDeviceID

**Framework**: Core MIDI  
**Kind**: var

The user-visible System Exclusive (SysEx) identifier of a device or entity.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.0+
- visionOS 1.0+

## Declaration

```swift
let kMIDIPropertyDeviceID: CFString
```

#### Discussion

MIDI drivers can set this property on their devices or entities. Studio setup editors can allow the user to set this property on external devices.

## See Also

- [let kMIDIPropertyName: CFString](kmidipropertyname.md)
  A name for a device, entity, or endpoint.
- [let kMIDIPropertyModel: CFString](kmidipropertymodel.md)
  The model name of a device or endpoint.
- [let kMIDIPropertyManufacturer: CFString](kmidipropertymanufacturer.md)
  The manufacturer name of a device or endpoint.
- [let kMIDIPropertyUniqueID: CFString](kmidipropertyuniqueid.md)
  The unique identifier of a device, entity, or, endpoint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/kmidipropertydeviceid)*