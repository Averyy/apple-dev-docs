# transmit(_:reply:)

**Framework**: CryptoTokenKit  
**Kind**: method  
**Role**: Instance Method

Transmits data in Application Protocol Data Unit (APDU) format to the Smart Card.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
func transmit(_ request: Data, reply: @escaping @Sendable (Data?, (any Error)?) -> Void)
```

```swift
func transmit(_ request: Data) async throws -> Data
```

```objc
- (void) transmitRequest:(NSData *) request reply:(void (^)(NSData *response, NSError *error)) reply;
```

## Discussion

You should only call this method after a session to the Smart Card has been established using the [`beginSession(reply:)`](./beginsession%28reply%29.md) method, and before the session is terminated using the [`endSession()`](./endsession%28%29.md) method.

## Parameters

- `request`: The APDU request data.
- `reply`:

  - **response**: The APDU response data, or `nil` if communication with the Smart Card failed.
  - **error**: Contains information about the the error preventing the transaction from being established.

  The `NSError` object is created in the [`TKErrorDomain`](../tkerrordomain.md) domain with a code in the [`TKError.Code`](../tkerror/code.md) enumeration.

## See Also

### Communicating with the Smart Card
- [func beginSession(reply: (Bool, (any Error)?) -> Void)](./beginsession%28reply%29.md)
  Begins a session with the Smart Card.
- [func endSession()](./endsession%28%29.md)
  Completes any pending transmissions and ends the session to the Smart Card.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcard/transmit(_:reply:))*