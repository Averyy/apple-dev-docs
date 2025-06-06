# kMIDIPropertyName

**Framework**: Core MIDI  
**Kind**: var

A name for a device, entity, or endpoint.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.0+
- visionOS 1.0+

## Declaration

```swift
let kMIDIPropertyName: CFString
```

#### Discussion

Devices, entities, and endpoints may all have names. The standard way to display an endpoint’s name is to ask it for its name and display it only if unique. If not, prepend the device name.

A studio setup editor may allow the user to set the names of both driver-owned and external devices.

## See Also

- [let kMIDIPropertyModel: CFString](kmidipropertymodel.md)
  The model name of a device or endpoint.
- [let kMIDIPropertyManufacturer: CFString](kmidipropertymanufacturer.md)
  The manufacturer name of a device or endpoint.
- [let kMIDIPropertyUniqueID: CFString](kmidipropertyuniqueid.md)
  The unique identifier of a device, entity, or, endpoint.
- [let kMIDIPropertyDeviceID: CFString](kmidipropertydeviceid.md)
  The user-visible System Exclusive (SysEx) identifier of a device or entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/kmidipropertyname)*