# HIDElementCollection

**Framework**: Core HID  
**Kind**: struct

A collection of items from a report descriptor for a HID device.

**Availability**:
- macOS 15.0+

## Declaration

```swift
struct HIDElementCollection
```

#### Overview

Collections are a defined part of the HID specification to specify how groupings of data relate to each other, and provide an overall structure for the organization of device functionality.

See the HID specification for more details: [`https://www.usb.org/hid`](https://developer.apple.comhttps://www.usb.org/hid).

## Topics

### Instance Properties
- [var childCollections: [HIDElementCollection]](hidelementcollection/childcollections.md)
  The collections contained by this collection, if there are any.
- [var childElements: [HIDElement]](hidelementcollection/childelements.md)
  The elements contained by this collection, if there are any.
- [var client: HIDDeviceClient](hidelementcollection/client.md)
  The client for the device with which this collection is associated.
- [var parentCollection: HIDElementCollection?](hidelementcollection/parentcollection.md)
  The collection that contains this collection, if there is one.
- [var type: HIDElementCollection.CollectionType](hidelementcollection/type.md)
  The type of this collection.
- [var usage: HIDUsage](hidelementcollection/usage.md)
  The HID specification compliant usage for this collection.
### Enumerations
- [HIDElementCollection.CollectionType](hidelementcollection/collectiontype.md)
  Types of [`HIDElementCollection`](hidelementcollection.md)s.
### Default Implementations
- [CustomStringConvertible Implementations](hidelementcollection/customstringconvertible-implementations.md)
- [Equatable Implementations](hidelementcollection/equatable-implementations.md)
- [Hashable Implementations](hidelementcollection/hashable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Communicating with human interface devices](communicatingwithhiddevices.md)
  Interact with and obtain data from devices such as keyboards and mice.
- [actor HIDDeviceClient](hiddeviceclient.md)
  A client of a physical or virtual HID compatible peripheral.
- [struct HIDElement](hidelement.md)
  A representation of an item from a report descriptor for a HID device.
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
- [enum HIDDeviceLocalizationCode](hiddevicelocalizationcode.md)
  The localization codes that some HID devices declare to specify conformance to a certain format or language.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hidelementcollection)*