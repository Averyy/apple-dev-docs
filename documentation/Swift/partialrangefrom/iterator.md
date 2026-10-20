# PartialRangeFrom.Iterator

**Framework**: Swift  
**Kind**: struct  
**Role**: Structure

The iterator for a `PartialRangeFrom` instance.

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

Available when `Bound` conforms to `Strideable` and `Bound.Stride` conforms to `SignedInteger`.

## Topics

### Instance Methods
- [func next() -> Bound?](./iterator/next%28%29.md)
  Advances to the next element and returns it, or `nil` if no next element exists.
### Type Aliases
- [PartialRangeFrom.Iterator.Element](./iterator/element.md)
  The type of element traversed by the iterator.

## Relationships

### Conforms To
- [BitwiseCopyable](../bitwisecopyable.md)
- [ConvertibleFromBytes](../convertiblefrombytes.md)
- [ConvertibleToBytes](../convertibletobytes.md)
- [Copyable](../copyable.md)
- [Escapable](../escapable.md)
- [IteratorProtocol](../iteratorprotocol.md)
- [Sendable](../sendable.md)
- [SendableMetatype](../sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/partialrangefrom/iterator)*