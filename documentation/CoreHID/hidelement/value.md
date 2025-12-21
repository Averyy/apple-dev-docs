# HIDElement.Value

**Framework**: Core HID  
**Kind**: struct

Data associated with a HID element.

**Availability**:
- macOS 15.0+

## Declaration

```swift
struct Value
```

## Mentions

- [Communicating with human interface devices](communicatingwithhiddevices.md)

#### Overview

Elements can have data associated with them. This data could be received as an update from the device to indicate user interaction, or could be provided to the device to alter functionality, such as turning on an LED. As the data for an element could be constantly changing, values should be seen as a snapshot of the element’s data at a specific time, and not valid at any other times.

Element values can be received by a [`HIDDeviceClient`](hiddeviceclient.md) using [`HIDDeviceClient.Notification.elementUpdates(values:)`](hiddeviceclient/notification/elementupdates(values:).md) after the device issues an input report, or requested from the device by providing a [`HIDDeviceClient.RequestElementUpdate`](hiddeviceclient/requestelementupdate.md) to [`updateElements(_:timeout:)`](hiddeviceclient/updateelements(_:timeout:).md). Element values can be sent to a device by providing a [`HIDDeviceClient.ProvideElementUpdate`](hiddeviceclient/provideelementupdate.md) to [`updateElements(_:timeout:)`](hiddeviceclient/updateelements(_:timeout:).md).

## Topics

### Create a HID element from a value
- [init(element: HIDElement, fromBytes: Data, timestamp: SuspendingClock.Instant)](hidelement/value/init(element:frombytes:timestamp:).md)
  Creates a value for an HID element.
- [init?<FloatingPointType>(element: HIDElement, fromPhysicalValue: FloatingPointType, timestamp: SuspendingClock.Instant)](hidelement/value/init(element:fromphysicalvalue:timestamp:).md)
  Creates a HID element value from a physical value.
- [init?<IntegerType>(element: HIDElement, fromLogicalValueTruncatingIfNeeded: IntegerType, timestamp: SuspendingClock.Instant)](hidelement/value/init(element:fromlogicalvaluetruncatingifneeded:timestamp:).md)
  Creates a HID element value from a logical value.
- [init<IntegerType>(element: HIDElement, fromIntegerTruncatingIfNeeded: IntegerType, timestamp: SuspendingClock.Instant)](hidelement/value/init(element:fromintegertruncatingifneeded:timestamp:).md)
  Creates an HID element value from an integer.
- [var element: HIDElement](hidelement/value/element.md)
  The [`HIDElement`](hidelement.md) associated with this value.
### Get element data and values
- [var bytes: Data](hidelement/value/bytes.md)
  The data as an array of bytes.
- [func integerValue<IntegerType>(asTypeTruncatingIfNeeded: IntegerType.Type) -> IntegerType](hidelement/value/integervalue(astypetruncatingifneeded:).md)
  The raw value of the data cast as an integer type, with no transformations applied.
- [func logicalValue<IntegerType>(asTypeTruncatingIfNeeded: IntegerType.Type) -> IntegerType?](hidelement/value/logicalvalue(astypetruncatingifneeded:).md)
  The raw value of the data cast as an integer type and bound by the [`HIDElement`](hidelement.md)’s logical minimum and logical maximum values.
- [func physicalValue<IntegerType, FloatingType>(fromTypeTruncatingIfNeeded: IntegerType.Type, as: FloatingType.Type) -> FloatingType?](hidelement/value/physicalvalue(fromtypetruncatingifneeded:as:).md)
  The logical value of the data, shifted and scaled by the [`HIDElement`](hidelement.md)’s physical minimum, physical maximum and exponent.
- [var timestamp: SuspendingClock.Instant](hidelement/value/timestamp.md)
  The time that this data was received by the system.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hidelement/value)*