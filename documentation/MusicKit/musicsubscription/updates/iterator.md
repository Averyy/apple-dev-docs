# MusicSubscription.Updates.Iterator

**Framework**: MusicKit  
**Kind**: struct

An iterator for the asynchronous sequence to use for observing updates to the current state of the user’s subscription to Apple Music.

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
struct Iterator
```

## Topics

### Instance Methods
- [func next() async -> MusicSubscription?](musicsubscription/updates/iterator/next.md)
  Asynchronously advances to the next element and returns it, or ends the sequence if there is no next element.
### Type Aliases
- [MusicSubscription.Updates.Iterator.Element](musicsubscription/updates/iterator/element.md)
### Default Implementations
- [AsyncIteratorProtocol Implementations](musicsubscription/updates/iterator/asynciteratorprotocol-implementations.md)

## Relationships

### Conforms To
- [AsyncIteratorProtocol](../Swift/AsyncIteratorProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musicsubscription/updates/iterator)*