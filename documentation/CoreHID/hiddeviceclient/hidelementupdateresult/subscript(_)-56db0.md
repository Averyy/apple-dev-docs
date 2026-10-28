# subscript(_:)

**Framework**: Core HID  
**Kind**: subscript  
**Role**: Instance Subscript

Receive the result of a element update.

**Availability**:
- macOS 15.0+

## Declaration

```swift
subscript(originalRequest: HIDDeviceClient.ProvideElementUpdate) -> Result<Void, any Error>? { get }
```

## Return Value

The result for the specified request that contain Void if successful; otherwise, an error if unsuccessful. Access the results using  [`get()`](../../../Swift/result/get%28%29.md).

## Overview

For an example, see [`updateElements(_:timeout:)`](../updateelements%28_,timeout%29.md).

## Parameters

- `originalRequest`: A request that was initially passed to [`updateElements(_:timeout:)`](../updateelements%28_,timeout%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hiddeviceclient/hidelementupdateresult/subscript(_:)-56db0)*