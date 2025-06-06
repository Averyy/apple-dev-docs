# readValue(completionHandler:)

**Framework**: HomeKit  
**Kind**: method

Reads the value for the characteristic.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func readValue() async throws
```

#### Discussion

The value is available from the [`value`](hmcharacteristic/value.md) property after completion of the request.

## Parameters

- `completion`: The block executed after the request is processed.

## See Also

- [var value: Any?](hmcharacteristic/value.md)
  The current value of the characteristic.
- [func writeValue(Any?, completionHandler: ((any Error)?) -> Void)](hmcharacteristic/writevalue(_:completionhandler:).md)
  Modifies the value of the characteristic.
- [func updateAuthorizationData(Data?, completionHandler: ((any Error)?) -> Void)](hmcharacteristic/updateauthorizationdata(_:completionhandler:).md)
  Sets or clears authorization data used when writing to the characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcharacteristic/readvalue(completionhandler:))*