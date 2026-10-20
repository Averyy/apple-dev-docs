# updateAuthorizationData(_:completionHandler:)

**Framework**: HomeKit  
**Kind**: method  
**Role**: Instance Method

Sets or clears authorization data used when writing to the characteristic.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- visionOS 1.0+

## Declaration

```swift
func updateAuthorizationData(_ data: Data?, completionHandler completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func updateAuthorizationData(_ data: Data?) async throws
```

```objc
- (void) updateAuthorizationData:(NSData *) data completionHandler:(void (^)(NSError *error)) completion;
```

## Parameters

- `data`: New authorization data to use. Pass `nil` to remove authorization data.
- `completion`: The block executed after the request is processed.

  - **error**: `nil` on success; otherwise, error object indicating the reason for failure.

## See Also

### Controlling a characteristic
- [var value: Any?](./value.md)
  The current value of the characteristic.
- [func readValue(completionHandler: ((any Error)?) -> Void)](./readvalue%28completionhandler%29.md)
  Reads the value for the characteristic.
- [func writeValue(Any?, completionHandler: ((any Error)?) -> Void)](./writevalue%28_,completionhandler%29.md)
  Modifies the value of the characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcharacteristic/updateauthorizationdata(_:completionhandler:))*