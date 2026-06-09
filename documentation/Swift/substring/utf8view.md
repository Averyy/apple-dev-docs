# Substring.UTF8View

**Framework**: Swift  
**Kind**: struct

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
struct UTF8View
```

## Topics

### Instance Properties
- [var span: Span<UTF8.CodeUnit>](substring/utf8view/span.md)
  A span over the UTF8 code units that make up this substring.
### Instance Methods
- [func isTriviallyIdentical(to: Substring.UTF8View) -> Bool](substring/utf8view/istriviallyidentical(to:).md)
  Returns a boolean value indicating whether this UTF8 view is trivially identical to `other`.
### Default Implementations
- [BidirectionalCollection Implementations](substring/utf8view/bidirectionalcollection-implementations.md)
- [Collection Implementations](substring/utf8view/collection-implementations.md)
- [Sequence Implementations](substring/utf8view/sequence-implementations.md)

## Relationships

### Conforms To
- [BidirectionalCollection](bidirectionalcollection.md)
- [Collection](collection.md)
- [Copyable](copyable.md)
- [Escapable](escapable.md)
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)
- [Sequence](sequence.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/substring/utf8view)*