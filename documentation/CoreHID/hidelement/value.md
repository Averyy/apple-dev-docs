# HIDElement.Value

**Framework**: Core HID  
**Kind**: struct  
**Role**: Structure

Data associated with a HID element.

**Availability**:
- macOS 15.0+

## Declaration

```swift
struct Value
```

## Mentions

- [Communicating with human interface devices](../communicatingwithhiddevices.md)

## Overview

Elements can have data associated with them. This data could be received as an update from the device to indicate user interaction, or could be provided to the device to alter functionality, such as turning on an LED. As the data for an element could be constantly changing, values should be seen as a snapshot of the element’s data at a specific time, and not valid at any other times.

Element values can be received by a [`HIDDeviceClient`](../hiddeviceclient.md) using [`HIDDeviceClient.Notification.elementUpdates(values:)`](../hiddeviceclient/notification/elementupdates%28values%29.md) after the device issues an input report, or requested from the device by providing a [`HIDDeviceClient.RequestElementUpdate`](../hiddeviceclient/requestelementupdate.md) to [`updateElements(_:timeout:)`](../hiddeviceclient/updateelements%28_,timeout%29.md). Element values can be sent to a device by providing a [`HIDDeviceClient.ProvideElementUpdate`](../hiddeviceclient/provideelementupdate.md) to [`updateElements(_:timeout:)`](../hiddeviceclient/updateelements%28_,timeout%29.md).

## Topics

### Create a HID element from a value
- [init(element: HIDElement, fromBytes: Data, timestamp: SuspendingClock.Instant)](./value/init%28element,frombytes,timestamp%29.md)
  Creates a value for an HID element.
- [init?<FloatingPointType>(element: HIDElement, fromPhysicalValue: FloatingPointType, timestamp: SuspendingClock.Instant)](./value/init%28element,fromphysicalvalue,timestamp%29.md)
  Creates a HID element value from a physical value.
- [init?<IntegerType>(element: HIDElement, fromLogicalValueTruncatingIfNeeded: IntegerType, timestamp: SuspendingClock.Instant)](./value/init%28element,fromlogicalvaluetruncatingifneeded,timestamp%29.md)
  Creates a HID element value from a logical value.
- [init<IntegerType>(element: HIDElement, fromIntegerTruncatingIfNeeded: IntegerType, timestamp: SuspendingClock.Instant)](./value/init%28element,fromintegertruncatingifneeded,timestamp%29.md)
  Creates an HID element value from an integer.
- [var element: HIDElement](./value/element.md)
  The [`HIDElement`](../hidelement.md) associated with this value.
### Get element data and values
- [var bytes: Data](./value/bytes.md)
  The data as an array of bytes.
- [func integerValue<IntegerType>(asTypeTruncatingIfNeeded: IntegerType.Type) -> IntegerType](./value/integervalue%28astypetruncatingifneeded%29.md)
  The raw value of the data cast as an integer type, with no transformations applied.
- [func logicalValue<IntegerType>(asTypeTruncatingIfNeeded: IntegerType.Type) -> IntegerType?](./value/logicalvalue%28astypetruncatingifneeded%29.md)
  The raw value of the data cast as an integer type and bound by the [`HIDElement`](../hidelement.md)’s logical minimum and logical maximum values.
- [func physicalValue<IntegerType, FloatingType>(fromTypeTruncatingIfNeeded: IntegerType.Type, as: FloatingType.Type) -> FloatingType?](./value/physicalvalue%28fromtypetruncatingifneeded,as%29.md)
  The logical value of the data, shifted and scaled by the [`HIDElement`](../hidelement.md)’s physical minimum, physical maximum and exponent.
- [var timestamp: SuspendingClock.Instant](./value/timestamp.md)
  The time that this data was received by the system.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Interaction
- [Communicating with human interface devices](../communicatingwithhiddevices.md)
  Interact with and obtain data from devices such as keyboards and mice.
- [actor HIDDeviceClient](../hiddeviceclient.md)
  A client of a physical or virtual HID compatible peripheral.
- [struct HIDElement](../hidelement.md)
  A representation of an item from a report descriptor for a HID device.
- [struct HIDElementCollection](../hidelementcollection.md)
  A collection of items from a report descriptor for a HID device.
- [protocol HIDElementUpdate](../hidelementupdate.md)
  A base protocol for element update types.
- [enum HIDReportType](../hidreporttype.md)
  Types for HID reports.
- [struct HIDReportID](../hidreportid.md)
  A type to represent the report IDs of HID reports.
- [enum HIDUsage](../hidusage.md)
  A type to represent HID usage pages.
- [enum HIDDeviceError](../hiddeviceerror.md)
  Errors that the framework can throw.
- [enum HIDDeviceTransport](../hiddevicetransport.md)
  Common transport types that transmit data to or from a HID device.
- [enum HIDDeviceLocalizationCode](../hiddevicelocalizationcode.md)
  The localization codes that some HID devices declare to specify conformance to a certain format or language.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hidelement/value)*