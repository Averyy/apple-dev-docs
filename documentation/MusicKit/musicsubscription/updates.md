# MusicSubscription.Updates

**Framework**: MusicKit  
**Kind**: struct

An asynchronous sequence to use for observing updates to the current state of the user’s subscription to Apple Music.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
struct Updates
```

## Topics

### Structures
- [MusicSubscription.Updates.Iterator](musicsubscription/updates/iterator.md)
  An iterator for the asynchronous sequence to use for observing updates to the current state of the user’s subscription to Apple Music.
### Instance Methods
- [func makeAsyncIterator() -> MusicSubscription.Updates.Iterator](musicsubscription/updates/makeasynciterator.md)
  Creates the asynchronous iterator that produces elements of this asynchronous sequence.
### Type Aliases
- [MusicSubscription.Updates.AsyncIterator](musicsubscription/updates/asynciterator.md)
  The type of asynchronous iterator that produces elements of this asynchronous sequence.
- [MusicSubscription.Updates.Element](musicsubscription/updates/element.md)
  The type of element the asynchronous sequence produces.
### Default Implementations
- [AsyncSequence Implementations](musicsubscription/updates/asyncsequence-implementations.md)

## Relationships

### Conforms To
- [AsyncSequence](../Swift/AsyncSequence.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musicsubscription/updates)*