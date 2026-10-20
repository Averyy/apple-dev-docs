# readValue(completionHandler:)

**Framework**: HomeKit  
**Kind**: method  
**Role**: Instance Method

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
func readValue(completionHandler completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func readValue() async throws
```

```objc
- (void) readValueWithCompletionHandler:(void (^)(NSError *error)) completion;
```

#### Discussion

The value is available from the [`value`](./value.md) property after completion of the request.

## Parameters

- `completion`: The block executed after the request is processed.

  - **error**: `nil` on success; otherwise, error object indicating the reason for failure.

## See Also

### Controlling a characteristic
- [var value: Any?](./value.md)
  The current value of the characteristic.
- [func writeValue(Any?, completionHandler: ((any Error)?) -> Void)](./writevalue%28_,completionhandler%29.md)
  Modifies the value of the characteristic.
- [func updateAuthorizationData(Data?, completionHandler: ((any Error)?) -> Void)](./updateauthorizationdata%28_,completionhandler%29.md)
  Sets or clears authorization data used when writing to the characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcharacteristic/readvalue(completionhandler:))*