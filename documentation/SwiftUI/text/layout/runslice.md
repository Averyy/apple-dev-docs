# Text.Layout.RunSlice

**Framework**: SwiftUI  
**Kind**: struct

A slice of a run of placed glyphs in a text layout.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
struct RunSlice
```

## Topics

### Initializers
- [init(run: Text.Layout.Run, indices: Range<Int>)](text/layout/runslice/init(run:indices:).md)
### Instance Properties
- [var characterIndices: [Text.Layout.CharacterIndex]](text/layout/runslice/characterindices.md)
  The array of character indices corresponding to the glyphs in `self`.
- [var run: Text.Layout.Run](text/layout/runslice/run.md)
- [var typographicBounds: Text.Layout.TypographicBounds](text/layout/runslice/typographicbounds.md)
  The typographic bounds of the partial run of glyphs.
### Subscripts
- [subscript<T>(T.Type) -> T?](text/layout/runslice/subscript(_:).md)
  The custom attribute of type `T` associated with the run of glyphs, or nil.

## Relationships

### Conforms To
- [BidirectionalCollection](../Swift/BidirectionalCollection.md)
- [Collection](../Swift/Collection.md)
- [Equatable](../Swift/Equatable.md)
- [RandomAccessCollection](../Swift/RandomAccessCollection.md)
- [Sequence](../Swift/Sequence.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/text/layout/runslice)*