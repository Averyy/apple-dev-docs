# endSession()

**Framework**: CryptoTokenKit  
**Kind**: method

Completes any pending transmissions and ends the session to the Smart Card.

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
func endSession()
```

#### Discussion

Calls to this method should balance calls to [`beginSession(reply:)`](tksmartcard/beginsession(reply:).md).

## See Also

- [func beginSession(reply: (Bool, (any Error)?) -> Void)](tksmartcard/beginsession(reply:).md)
  Begins a session with the Smart Card.
- [func transmit(Data, reply: (Data?, (any Error)?) -> Void)](tksmartcard/transmit(_:reply:).md)
  Transmits data in Application Protocol Data Unit (APDU) format to the Smart Card.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcard/endsession())*