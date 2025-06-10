# HIDDeviceLocalizationCode

**Framework**: Core HID  
**Kind**: enum

The localization codes that some HID devices declare to specify conformance to a certain format or language.

**Availability**:
- macOS 15.0+

## Declaration

```swift
enum HIDDeviceLocalizationCode
```

#### Overview

This maps to the optional `bCountryCode` value in the HID descriptor.

For more details, see [`Human Interface Devices (HID) Specifications and Tools`](https://developer.apple.comhttps://www.usb.org/hid).

## Topics

### Operators
- [static func == (HIDDeviceLocalizationCode, HIDDeviceLocalizationCode) -> Bool](hiddevicelocalizationcode/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [HIDDeviceLocalizationCode.arabic](hiddevicelocalizationcode/arabic.md)
  This maps to Arabic in the HID specification.
- [HIDDeviceLocalizationCode.belgium](hiddevicelocalizationcode/belgium.md)
  This maps to Belgian in the HID specification.
- [HIDDeviceLocalizationCode.canada](hiddevicelocalizationcode/canada.md)
  This maps to Canadian-bilingual in the HID specification.
- [HIDDeviceLocalizationCode.canadaFrench](hiddevicelocalizationcode/canadafrench.md)
  This maps to Canadian-French in the HID specification.
- [HIDDeviceLocalizationCode.chineseZhuyin](hiddevicelocalizationcode/chinesezhuyin.md)
  This maps to Taiwan in the HID specification.
- [HIDDeviceLocalizationCode.czechia](hiddevicelocalizationcode/czechia.md)
  This maps to Czech Republic in the HID specification.
- [HIDDeviceLocalizationCode.denmark](hiddevicelocalizationcode/denmark.md)
  This maps to Danish in the HID specification.
- [HIDDeviceLocalizationCode.finland](hiddevicelocalizationcode/finland.md)
  This maps to Finnish in the HID specification.
- [HIDDeviceLocalizationCode.france](hiddevicelocalizationcode/france.md)
  This maps to France in the HID specification.
- [HIDDeviceLocalizationCode.germany](hiddevicelocalizationcode/germany.md)
  This maps to German in the HID specification.
- [HIDDeviceLocalizationCode.greece](hiddevicelocalizationcode/greece.md)
  This maps to Greek in the HID specification.
- [HIDDeviceLocalizationCode.hebrew](hiddevicelocalizationcode/hebrew.md)
  This maps to Hebrew in the HID specification.
- [HIDDeviceLocalizationCode.hungary](hiddevicelocalizationcode/hungary.md)
  This maps to Hungary in the HID specification.
- [HIDDeviceLocalizationCode.italy](hiddevicelocalizationcode/italy.md)
  This maps to Italian in the HID specification.
- [HIDDeviceLocalizationCode.japan](hiddevicelocalizationcode/japan.md)
  This maps to Japan (Katakana) in the HID specification.
- [HIDDeviceLocalizationCode.korea](hiddevicelocalizationcode/korea.md)
  This maps to Korean in the HID specification.
- [HIDDeviceLocalizationCode.latinAmerica](hiddevicelocalizationcode/latinamerica.md)
  This maps to Latin America in the HID specification.
- [HIDDeviceLocalizationCode.netherlands](hiddevicelocalizationcode/netherlands.md)
  This maps to Netherlands/Dutch in the HID specification.
- [HIDDeviceLocalizationCode.norway](hiddevicelocalizationcode/norway.md)
  This maps to Norwegian in the HID specification.
- [HIDDeviceLocalizationCode.persian](hiddevicelocalizationcode/persian.md)
  This maps to Persian (Farsi) in the HID specification.
- [HIDDeviceLocalizationCode.poland](hiddevicelocalizationcode/poland.md)
  This maps to Poland in the HID specification.
- [HIDDeviceLocalizationCode.portugal](hiddevicelocalizationcode/portugal.md)
  This maps to Portuguese in the HID specification.
- [HIDDeviceLocalizationCode.russia](hiddevicelocalizationcode/russia.md)
  This maps to Russia in the HID specification.
- [HIDDeviceLocalizationCode.slovakia](hiddevicelocalizationcode/slovakia.md)
  This maps to Slovakia in the HID specification.
- [HIDDeviceLocalizationCode.spain](hiddevicelocalizationcode/spain.md)
  This maps to Spanish in the HID specification.
- [HIDDeviceLocalizationCode.sweden](hiddevicelocalizationcode/sweden.md)
  This maps to Swedish in the HID specification.
- [HIDDeviceLocalizationCode.switzerland](hiddevicelocalizationcode/switzerland.md)
  This maps to Switzerland in the HID specification.
- [HIDDeviceLocalizationCode.switzerlandFrench](hiddevicelocalizationcode/switzerlandfrench.md)
  This maps to Swiss/French in the HID specification.
- [HIDDeviceLocalizationCode.switzerlandGerman](hiddevicelocalizationcode/switzerlandgerman.md)
  This maps to Swiss/German in the HID specification.
- [HIDDeviceLocalizationCode.turkeyQWERTY](hiddevicelocalizationcode/turkeyqwerty.md)
  This maps to Turkish-Q in the HID specification.
- [HIDDeviceLocalizationCode.turkeyStandard](hiddevicelocalizationcode/turkeystandard.md)
  This maps to Turkish-F in the HID specification.
- [HIDDeviceLocalizationCode.unitedKingdom](hiddevicelocalizationcode/unitedkingdom.md)
  This maps to UK in the HID specification.
- [HIDDeviceLocalizationCode.unitedStates](hiddevicelocalizationcode/unitedstates.md)
  This maps to US in the HID specification.
- [HIDDeviceLocalizationCode.unitedStatesISO](hiddevicelocalizationcode/unitedstatesiso.md)
  This maps to International (ISO) in the HID specification.
- [HIDDeviceLocalizationCode.unsupported](hiddevicelocalizationcode/unsupported.md)
  This maps to Not Supported in the HID specification.
- [HIDDeviceLocalizationCode.yugoslavia](hiddevicelocalizationcode/yugoslavia.md)
  This maps to Yugoslavia in the HID specification.
### Instance Properties
- [var hashValue: Int](hiddevicelocalizationcode/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](hiddevicelocalizationcode/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](hiddevicelocalizationcode/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Communicating with human interface devices](communicatingwithhiddevices.md)
  Interact with and obtain data from devices such as keyboards and mice.
- [actor HIDDeviceClient](hiddeviceclient.md)
  A client of a physical or virtual HID compatible peripheral.
- [struct HIDElement](hidelement.md)
  A representation of an item from a report descriptor for a HID device.
- [struct HIDElementCollection](hidelementcollection.md)
  A collection of items from a report descriptor for a HID device.
- [HIDElement.Value](hidelement/value.md)
  Data associated with a HID element.
- [protocol HIDElementUpdate](hidelementupdate.md)
  A base protocol for element update types.
- [enum HIDReportType](hidreporttype.md)
  Types for HID reports.
- [struct HIDReportID](hidreportid.md)
  A type to represent the report IDs of HID reports.
- [enum HIDUsage](hidusage.md)
  A type to represent HID usage pages.
- [enum HIDDeviceError](hiddeviceerror.md)
  Errors that the framework can throw.
- [enum HIDDeviceTransport](hiddevicetransport.md)
  Common transport types that transmit data to or from a HID device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hiddevicelocalizationcode)*