# CardSession.EventStream

**Framework**: Core NFC  
**Kind**: class  
**Role**: Class

An asynchronous sequence of events produced by a card session.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
final class EventStream
```

#### Overview

Get an asychronous sequence of this type from the card session’s [`eventStream`](./eventstream-swift.property.md) property. Then use the Swift `for-await-in` syntax to receive and process events as the session produces them.

## Topics

### Creating an iterator
- [CardSession.EventStream.Iterator](./eventstream-swift.class/iterator.md)
  The iterator that produces elements of this asynchronous sequence.

## Relationships

### Conforms To
- [AsyncSequence](../../Swift/asyncsequence.md)

## See Also

### Handling card events
- [var eventStream: CardSession.EventStream](./eventstream-swift.property.md)
  An asynchronous sequence of events from the card session.
- [CardSession.Event](./event.md)
  A type that enumerates events produced by a card session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/cardsession/eventstream-swift.class)*