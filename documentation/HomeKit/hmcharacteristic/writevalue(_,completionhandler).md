# writeValue(_:completionHandler:)

**Framework**: HomeKit  
**Kind**: method  
**Role**: Instance Method

Modifies the value of the characteristic.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func writeValue(_ value: Any?, completionHandler completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func writeValue(_ value: Any?) async throws
```

```objc
- (void) writeValue:(id) value completionHandler:(void (^)(NSError *error)) completion;
```

## Parameters

- `value`: The new value.
- `completion`: The block executed after the request is processed.

  - **error**: `nil` on success; otherwise, error object indicating the reason for failure.

## See Also

### Controlling a characteristic
- [var value: Any?](./value.md)
  The current value of the characteristic.
- [func readValue(completionHandler: ((any Error)?) -> Void)](./readvalue%28completionhandler%29.md)
  Reads the value for the characteristic.
- [func updateAuthorizationData(Data?, completionHandler: ((any Error)?) -> Void)](./updateauthorizationdata%28_,completionhandler%29.md)
  Sets or clears authorization data used when writing to the characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcharacteristic/writevalue(_:completionhandler:))*