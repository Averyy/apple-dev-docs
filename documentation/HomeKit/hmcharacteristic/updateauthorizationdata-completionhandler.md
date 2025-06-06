# updateAuthorizationData(_:completionHandler:)

**Framework**: HomeKit  
**Kind**: method

Sets or clears authorization data used when writing to the characteristic.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- visionOS 1.0+

## Declaration

```swift
func updateAuthorizationData(_ data: Data?) async throws
```

## Parameters

- `data`: New authorization data to use. Pass   to remove authorization data.
- `completion`: The block executed after the request is processed.

## See Also

- [var value: Any?](hmcharacteristic/value.md)
  The current value of the characteristic.
- [func readValue(completionHandler: ((any Error)?) -> Void)](hmcharacteristic/readvalue(completionhandler:).md)
  Reads the value for the characteristic.
- [func writeValue(Any?, completionHandler: ((any Error)?) -> Void)](hmcharacteristic/writevalue(_:completionhandler:).md)
  Modifies the value of the characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcharacteristic/updateauthorizationdata(_:completionhandler:))*