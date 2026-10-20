# beginSession(reply:)

**Framework**: CryptoTokenKit  
**Kind**: method  
**Role**: Instance Method

Begins a session with the Smart Card.

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
func beginSession(reply: @escaping @Sendable (Bool, (any Error)?) -> Void)
```

```swift
func beginSession() async throws -> Bool
```

```objc
- (void) beginSessionWithReply:(void (^)(BOOL success, NSError *error)) reply;
```

#### Discussion

This method will fail if there is already an existing session for the Smart Card.

Calls to this method must be balanced with calls to [`endSession()`](./endsession%28%29.md).

## Parameters

- `reply`:

  - **success**: Whether the session could be established successfully.
  - **error**: Contains information about the error preventing the transaction from being established.

  The `NSError` object is created in the [`TKErrorDomain`](../tkerrordomain.md) domain with a code in the [`TKError.Code`](../tkerror/code.md) enumeration.

## See Also

### Communicating with the Smart Card
- [func transmit(Data, reply: (Data?, (any Error)?) -> Void)](./transmit%28_,reply%29.md)
  Transmits data in Application Protocol Data Unit (APDU) format to the Smart Card.
- [func endSession()](./endsession%28%29.md)
  Completes any pending transmissions and ends the session to the Smart Card.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcard/beginsession(reply:))*