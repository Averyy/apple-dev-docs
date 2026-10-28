# endSession()

**Framework**: CryptoTokenKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) endSession;
```

## Discussion

Calls to this method should balance calls to [`beginSession(reply:)`](./beginsession%28reply%29.md).

## See Also

### Communicating with the Smart Card
- [func beginSession(reply: (Bool, (any Error)?) -> Void)](./beginsession%28reply%29.md)
  Begins a session with the Smart Card.
- [func transmit(Data, reply: (Data?, (any Error)?) -> Void)](./transmit%28_,reply%29.md)
  Transmits data in Application Protocol Data Unit (APDU) format to the Smart Card.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcard/endsession())*