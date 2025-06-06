# subscript(_:)

**Framework**: Core HID  
**Kind**: subscript

Receive the result of a request element update.

**Availability**:
- macOS 15.0+

## Declaration

```swift
subscript(originalRequest: HIDDeviceClient.RequestElementUpdate) -> Result<[HIDElement.Value], any Error>? { get }
```

#### Return Value

The result for the specified request which contains a list of updated [`HIDElement.Value`](hidelement/value.md) objects. Access the results using  [`get()`](https://developer.apple.com/documentation/Swift/Result/get()).

#### Overview

For an example, see [`updateElements(_:timeout:)`](hiddeviceclient/updateelements(_:timeout:).md).

## Parameters

- `originalRequest`: A request that was initially passed to  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hiddeviceclient/hidelementupdateresult/subscript(_:)-7mvq2)*