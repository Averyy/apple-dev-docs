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
  An iterator over a sequence of session events.
### Instance Methods
- [func makeAsyncIterator() -> ARKitSession.Events.Iterator](./events-swift.struct/makeasynciterator%28%29.md)
  Creates an asynchronous iterator that produces `Event` elements on this asynchronous sequence.
### Type Aliases
- [ARKitSession.Events.Element](./events-swift.struct/element.md)
  The type of element produced by this asynchronous sequence: ARKitSession.Event.

## Relationships

### Conforms To
- [AsyncSequence](../../Swift/asyncsequence.md)

## See Also

### Observing a session
- [var events: ARKitSession.Events](./events-swift.property.md)
  An asynchronous sequence of events that describe changes to the session, such as authorization changes and data-provider state changes.
- [ARKitSession.Event](./event.md)
  Enumeration of possible session events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arkitsession/events-swift.struct)*