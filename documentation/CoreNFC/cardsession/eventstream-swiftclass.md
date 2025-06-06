# CardSession.EventStream

**Framework**: Core NFC  
**Kind**: class

An asynchronous sequence of events produced by a card session.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
final class EventStream
```

#### Overview

Get an asychronous sequence of this type from the card session’s [`eventStream`](cardsession/eventstream-swift.property.md) property. Then use the Swift `for-await-in` syntax to receive and process events as the session produces them.

## Topics

### Creating an iterator
- [CardSession.EventStream.Iterator](cardsession/eventstream-swift.class/iterator.md)
  The iterator that produces elements of this asynchronous sequence.

## Relationships

### Conforms To
- [AsyncSequence](../Swift/AsyncSequence.md)

## See Also

- [var eventStream: CardSession.EventStream](cardsession/eventstream-swift.property.md)
  An asynchronous sequence of events from the card session.
- [CardSession.Event](cardsession/event.md)
  A type that enumerates events produced by a card session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/cardsession/eventstream-swift.class)*