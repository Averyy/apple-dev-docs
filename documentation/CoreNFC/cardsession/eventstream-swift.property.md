# eventStream

**Framework**: Core NFC  
**Kind**: property  
**Role**: Instance Property

An asynchronous sequence of events from the card session.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
var eventStream: CardSession.EventStream { get }
```

#### Discussion

Use the Swift `for-await-in` syntax to receive and process events as the session produces them.

## See Also

### Handling card events
- [CardSession.EventStream](./eventstream-swift.class.md)
  An asynchronous sequence of events produced by a card session.
- [CardSession.Event](./event.md)
  A type that enumerates events produced by a card session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/cardsession/eventstream-swift.property)*