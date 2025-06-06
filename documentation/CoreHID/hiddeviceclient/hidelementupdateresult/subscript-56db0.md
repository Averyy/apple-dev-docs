# subscript(_:)

**Framework**: Core HID  
**Kind**: subscript

Receive the result of a element update.

**Availability**:
- macOS 15.0+

## Declaration

```swift
subscript(originalRequest: HIDDeviceClient.ProvideElementUpdate) -> Result<Void, any Error>? { get }
```

#### Return Value

The result for the specified request that contain Void if successful; otherwise, an error if unsuccessful. Access the results using  [`get()`](https://developer.apple.com/documentation/Swift/Result/get()).

#### Overview

For an example, see [`updateElements(_:timeout:)`](hiddeviceclient/updateelements(_:timeout:).md).

## Parameters

- `originalRequest`: A request that was initially passed to  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hiddeviceclient/hidelementupdateresult/subscript(_:)-56db0)*