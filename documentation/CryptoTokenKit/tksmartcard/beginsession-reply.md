# beginSession(reply:)

**Framework**: CryptoTokenKit  
**Kind**: method

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
func beginSession() async throws -> Bool
```

#### Discussion

This method will fail if there is already an existing session for the Smart Card.

Calls to this method must be balanced with calls to [`endSession()`](tksmartcard/endsession().md).

## Parameters

- `reply`: The   object is created in the   domain with a code in the   enumeration.

## See Also

- [func transmit(Data, reply: (Data?, (any Error)?) -> Void)](tksmartcard/transmit(_:reply:).md)
  Transmits data in Application Protocol Data Unit (APDU) format to the Smart Card.
- [func endSession()](tksmartcard/endsession.md)
  Completes any pending transmissions and ends the session to the Smart Card.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcard/beginsession(reply:))*