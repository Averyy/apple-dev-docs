# AttributedString.UnicodeScalarView

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

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
- [Collection Implementations](./unicodescalarview/collection-implementations.md)

## Relationships

### Conforms To
- [BidirectionalCollection](../../Swift/bidirectionalcollection.md)
- [Collection](../../Swift/collection.md)
- [Copyable](../../Swift/copyable.md)
- [Escapable](../../Swift/escapable.md)
- [RangeReplaceableCollection](../../Swift/rangereplaceablecollection.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [Sequence](../../Swift/sequence.md)

## See Also

### Accessing Views into the Attributed String
- [var characters: AttributedString.CharacterView](./characters.md)
  The characters of the attributed string, as a view into the underlying string.
- [AttributedString.CharacterView](./characterview.md)
  A view into the underlying storage of the attributed string, as Unicode characters.
- [var unicodeScalars: AttributedString.UnicodeScalarView](./unicodescalars.md)
  The Unicode scalars of the attributed string, as a view into the underlying string.
- [var runs: AttributedString.Runs](./runs-swift.property.md)
  The attributed runs of the attributed string, as a view into the underlying string.
- [AttributedString.Runs](./runs-swift.struct.md)
  An iterable view into segments of the attributed string, each of which indicates where a run of identical attributes begins or ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstring/unicodescalarview)*