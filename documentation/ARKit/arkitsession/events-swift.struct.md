# ARKitSession.Events

**Framework**: ARKit  
**Kind**: struct  
**Role**: Structure

A sequence of events.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```swift
struct Events
```

## Topics

### Structures
- [ARKitSession.Events.Iterator](./events-swift.struct/iterator.md)
  A type that provides a sequence’s iteration interface and encapsulates its iteration state.
### Instance Methods
- [func makeAsyncIterator() -> ARKitSession.Events.Iterator](./events-swift.struct/makeasynciterator%28%29.md)
  Creates an asynchronous iterator that produces `Event` elements on this asynchronous sequence.
### Type Aliases
- [ARKitSession.Events.Element](./events-swift.struct/element.md)
  A type representing a sequence’s elements.

## Relationships

### Conforms To
- [AsyncSequence](../../Swift/asyncsequence.md)

## See Also

### Observing a session
- [var events: ARKitSession.Events](./events-swift.property.md)
  An asynchronous sequence of events that provide updates to the current authorization status of the session.
- [ARKitSession.Event](./event.md)
  Enumeration of possible session events.
- [var description: String](./description.md)
  A textual representation of this session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arkitsession/events-swift.struct)*