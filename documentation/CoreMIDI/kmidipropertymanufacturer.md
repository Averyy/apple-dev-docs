# kMIDIPropertyManufacturer

**Framework**: Core MIDI  
**Kind**: var

The manufacturer name of a device or endpoint.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.0+
- visionOS 1.0+

## Declaration

```swift
let kMIDIPropertyManufacturer: CFString
```

#### Discussion

Use this property in the following cases:

- MIDI drivers set this property on their devices.
- Studio setup editors may allow the user to set this property on external devices.
- Creators of virtual endpoints may set this property on their endpoints.

## See Also

- [let kMIDIPropertyName: CFString](kmidipropertyname.md)
  A name for a device, entity, or endpoint.
- [let kMIDIPropertyModel: CFString](kmidipropertymodel.md)
  The model name of a device or endpoint.
- [let kMIDIPropertyUniqueID: CFString](kmidipropertyuniqueid.md)
  The unique identifier of a device, entity, or, endpoint.
- [let kMIDIPropertyDeviceID: CFString](kmidipropertydeviceid.md)
  The user-visible System Exclusive (SysEx) identifier of a device or entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/kmidipropertymanufacturer)*