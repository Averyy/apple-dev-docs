# LazyCollectionProtocol

**Framework**: Swift  
**Kind**: protocol

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
protocol LazyCollectionProtocol : Collection, LazySequenceProtocol where Self.Elements : Collection
```

## Topics

### Instance Properties
- [var lazy: Self.Elements](lazycollectionprotocol/lazy-7wmso.md)
- [var lazy: LazyCollection<Self.Elements>](lazycollectionprotocol/lazy-9k7qy.md)

## Relationships

### Inherits From
- [Collection](collection.md)
- [LazySequenceProtocol](lazysequenceprotocol.md)
- [Sequence](sequence.md)
### Conforming Types
- [LazyDropWhileSequence](lazydropwhilesequence.md)
- [LazyFilterSequence](lazyfiltersequence.md)
- [LazyMapSequence](lazymapsequence.md)
- [LazyPrefixWhileSequence](lazyprefixwhilesequence.md)
- [LazySequence](lazysequence.md)

## See Also

- [protocol LazySequenceProtocol](lazysequenceprotocol.md)
  A sequence on which normally-eager sequence operations are implemented lazily.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/lazycollectionprotocol)*