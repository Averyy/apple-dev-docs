# HIDDeviceClient.RequestElementUpdate

**Framework**: Core HID  
**Kind**: struct

A request to pull the current value from a list of HID elements

**Availability**:
- macOS 15.0+

## Declaration

```swift
struct RequestElementUpdate
```

## Mentions

- [Communicating with human interface devices](communicatingwithhiddevices.md)

#### Overview

Provide this structure to [`updateElements(_:timeout:)`](hiddeviceclient/updateelements(_:timeout:).md) to request the current values for a list of elements. In most cases, this triggers a get report request to the device for all of the reports containing elements in the provided element list.

## Topics

### Operators
- [static func == (HIDDeviceClient.RequestElementUpdate, HIDDeviceClient.RequestElementUpdate) -> Bool](hiddeviceclient/requestelementupdate/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Initializers
- [init(elements: [HIDElement], pollDevice: Bool)](hiddeviceclient/requestelementupdate/init(elements:polldevice:).md)
  Creates a request element update.
### Instance Properties
- [var elements: [HIDElement]](hiddeviceclient/requestelementupdate/elements.md)
  The elements used to request updates.
- [var hashValue: Int](hiddeviceclient/requestelementupdate/hashvalue.md)
  The hash value.
- [var pollDevice: Bool](hiddeviceclient/requestelementupdate/polldevice.md)
  Whether the device should be polled for new updates.
### Instance Methods
- [func hash(into: inout Hasher)](hiddeviceclient/requestelementupdate/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](hiddeviceclient/requestelementupdate/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [HIDElementUpdate](hidelementupdate.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func updateElements([any HIDElementUpdate], timeout: Duration?) async -> HIDDeviceClient.HIDElementUpdateResult](hiddeviceclient/updateelements(_:timeout:).md)
  Provide new update values for, or request current values from, lists of elements.
- [HIDDeviceClient.ProvideElementUpdate](hiddeviceclient/provideelementupdate.md)
  A structure that provides values for a list of HID elements.
- [HIDDeviceClient.HIDElementUpdateResult](hiddeviceclient/hidelementupdateresult.md)
  A class to hold the results of an element update.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hiddeviceclient/requestelementupdate)*