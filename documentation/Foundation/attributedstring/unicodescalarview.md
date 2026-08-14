# AttributedString.UnicodeScalarView

**Framework**: Foundation  
**Kind**: struct

A view into the underlying storage of the attributed string, as Unicode scalars.

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
struct UnicodeScalarView
```

## Topics

### Default Implementations
- [Collection Implementations](attributedstring/unicodescalarview/collection-implementations.md)

## Relationships

### Conforms To
- [BidirectionalCollection](../swift/bidirectionalcollection.md)
- [Collection](../swift/collection.md)
- [Copyable](../swift/copyable.md)
- [Escapable](../swift/escapable.md)
- [RangeReplaceableCollection](../swift/rangereplaceablecollection.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [Sequence](../swift/sequence.md)

## See Also

- [var characters: AttributedString.CharacterView](attributedstring/characters.md)
  The characters of the attributed string, as a view into the underlying string.
- [AttributedString.CharacterView](attributedstring/characterview.md)
  A view into the underlying storage of the attributed string, as Unicode characters.
- [var unicodeScalars: AttributedString.UnicodeScalarView](attributedstring/unicodescalars.md)
  The Unicode scalars of the attributed string, as a view into the underlying string.
- [var runs: AttributedString.Runs](attributedstring/runs-swift.property.md)
  The attributed runs of the attributed string, as a view into the underlying string.
- [AttributedString.Runs](attributedstring/runs-swift.struct.md)
  An iterable view into segments of the attributed string, each of which indicates where a run of identical attributes begins or ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstring/unicodescalarview)*