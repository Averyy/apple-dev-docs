# HIDDeviceClient.HIDElementUpdateResult

**Framework**: Core HID  
**Kind**: struct

A class to hold the results of an element update.

**Availability**:
- macOS 15.0+

## Declaration

```swift
struct HIDElementUpdateResult
```

#### Overview

This class is received as the return value from [`updateElements(_:timeout:)`](hiddeviceclient/updateelements(_:timeout:).md). The results of the transactions can be received by subscripting the results object with [`HIDDeviceClient.ProvideElementUpdate`](hiddeviceclient/provideelementupdate.md) and [`HIDDeviceClient.RequestElementUpdate`](hiddeviceclient/requestelementupdate.md) originally passed to [`updateElements(_:timeout:)`](hiddeviceclient/updateelements(_:timeout:).md).

For an example, see [`updateElements(_:timeout:)`](hiddeviceclient/updateelements(_:timeout:).md).

## Topics

### Subscripts
- [subscript(HIDDeviceClient.ProvideElementUpdate) -> Result<Void, any Error>?](hiddeviceclient/hidelementupdateresult/subscript(_:)-56db0.md)
  Receive the result of a element update.
- [subscript(HIDDeviceClient.RequestElementUpdate) -> Result<[HIDElement.Value], any Error>?](hiddeviceclient/hidelementupdateresult/subscript(_:)-7mvq2.md)
  Receive the result of a request element update.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [func updateElements([any HIDElementUpdate], timeout: Duration?) async -> HIDDeviceClient.HIDElementUpdateResult](hiddeviceclient/updateelements(_:timeout:).md)
  Provide new update values for, or request current values from, lists of elements.
- [HIDDeviceClient.RequestElementUpdate](hiddeviceclient/requestelementupdate.md)
  A request to pull the current value from a list of HID elements
- [HIDDeviceClient.ProvideElementUpdate](hiddeviceclient/provideelementupdate.md)
  A structure that provides values for a list of HID elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hiddeviceclient/hidelementupdateresult)*