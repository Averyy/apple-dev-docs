# HIDDeviceClient.HIDElementUpdateResult

**Framework**: Core HID  
**Kind**: struct  
**Role**: Structure

A class to hold the results of an element update.

**Availability**:
- macOS 15.0+

## Declaration

```swift
struct HIDElementUpdateResult
```

## Overview

This class is received as the return value from [`updateElements(_:timeout:)`](./updateelements%28_,timeout%29.md). The results of the transactions can be received by subscripting the results object with [`HIDDeviceClient.ProvideElementUpdate`](./provideelementupdate.md) and [`HIDDeviceClient.RequestElementUpdate`](./requestelementupdate.md) originally passed to [`updateElements(_:timeout:)`](./updateelements%28_,timeout%29.md).

For an example, see [`updateElements(_:timeout:)`](./updateelements%28_,timeout%29.md).

## Topics

### Subscripts
- [subscript(HIDDeviceClient.ProvideElementUpdate) -> Result<Void, any Error>?](./hidelementupdateresult/subscript%28_%29-56db0.md)
  Receive the result of a element update.
- [subscript(HIDDeviceClient.RequestElementUpdate) -> Result<[HIDElement.Value], any Error>?](./hidelementupdateresult/subscript%28_%29-7mvq2.md)
  Receive the result of a request element update.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Update element values
- [func updateElements([any HIDElementUpdate], timeout: Duration?) async -> HIDDeviceClient.HIDElementUpdateResult](./updateelements%28_,timeout%29.md)
  Provide new update values for, or request current values from, lists of elements.
- [HIDDeviceClient.RequestElementUpdate](./requestelementupdate.md)
  A request to pull the current value from a list of HID elements
- [HIDDeviceClient.ProvideElementUpdate](./provideelementupdate.md)
  A structure that provides values for a list of HID elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hiddeviceclient/hidelementupdateresult)*