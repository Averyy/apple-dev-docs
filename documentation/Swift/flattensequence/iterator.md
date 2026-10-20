# FlattenSequence.Iterator

**Framework**: Swift  
**Kind**: struct  
**Role**: Structure

A type that provides the sequence’s iteration interface and encapsulates its iteration state.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
@frozen
struct Iterator
```

Available when `Base` conforms to `Sequence` and `Base.Element` conforms to `Sequence`.

## Topics

### Default Implementations
- [IteratorProtocol Implementations](./iterator/iteratorprotocol-implementations.md)
- [Sequence Implementations](./iterator/sequence-implementations.md)

## Relationships

### Conforms To
- [Copyable](../copyable.md)
- [Escapable](../escapable.md)
- [IteratorProtocol](../iteratorprotocol.md)
- [Sendable](../sendable.md)
- [SendableMetatype](../sendablemetatype.md)
- [Sequence](../sequence.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/flattensequence/iterator)*