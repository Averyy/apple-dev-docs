# HIDDeviceClient.ProvideElementUpdate

**Framework**: Core HID  
**Kind**: struct

A structure that provides values for a list of HID elements.

**Availability**:
- macOS 15.0+

## Declaration

```swift
struct ProvideElementUpdate
```

## Mentions

- [Communicating with human interface devices](communicatingwithhiddevices.md)

#### Overview

Provide this structure to [`updateElements(_:timeout:)`](hiddeviceclient/updateelements(_:timeout:).md) to update the current values for a list of elements. In most cases, this triggers a set report request to the device for all of the reports containing elements in the provided element list.

## Topics

### Initializers
- [init(values: [HIDElement.Value])](hiddeviceclient/provideelementupdate/init(values:).md)
  Creates a [`HIDDeviceClient.ProvideElementUpdate`](hiddeviceclient/provideelementupdate.md).
### Instance Properties
- [var values: [HIDElement.Value]](hiddeviceclient/provideelementupdate/values.md)
  The values used to update the elements.

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
- [HIDDeviceClient.RequestElementUpdate](hiddeviceclient/requestelementupdate.md)
  A request to pull the current value from a list of HID elements
- [HIDDeviceClient.HIDElementUpdateResult](hiddeviceclient/hidelementupdateresult.md)
  A class to hold the results of an element update.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hiddeviceclient/provideelementupdate)*