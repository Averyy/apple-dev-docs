# transmit(_:reply:)

**Framework**: CryptoTokenKit  
**Kind**: method

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
func transmit(_ request: Data) async throws -> Data
```

#### Discussion

You should only call this method after a session to the Smart Card has been established using the [`beginSession(reply:)`](tksmartcard/beginsession(reply:).md) method, and before the session is terminated using the [`endSession()`](tksmartcard/endsession().md) method.

## Parameters

- `request`: The APDU request data.
- `reply`: The   object is created in the   domain with a code in the   enumeration.

## See Also

- [func beginSession(reply: (Bool, (any Error)?) -> Void)](tksmartcard/beginsession(reply:).md)
  Begins a session with the Smart Card.
- [func endSession()](tksmartcard/endsession.md)
  Completes any pending transmissions and ends the session to the Smart Card.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcard/transmit(_:reply:))*