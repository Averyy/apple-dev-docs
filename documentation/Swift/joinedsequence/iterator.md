# JoinedSequence.Iterator

**Framework**: Swift  
**Kind**: struct  
**Role**: Structure

An iterator that presents the elements of the sequences traversed by a base iterator, concatenated using a given separator.

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

### Initializers
- [init<Separator>(base: Base.Iterator, separator: Separator)](./iterator/init%28base,separator%29.md)
  Creates an iterator that presents the elements of `base` sequences concatenated using `separator`.
### Default Implementations
- [IteratorProtocol Implementations](./iterator/iteratorprotocol-implementations.md)

## Relationships

### Conforms To
- [Copyable](../copyable.md)
- [Escapable](../escapable.md)
- [IteratorProtocol](../iteratorprotocol.md)
- [Sendable](../sendable.md)
- [SendableMetatype](../sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/joinedsequence/iterator)*