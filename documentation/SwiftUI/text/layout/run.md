# Text.Layout.Run

**Framework**: SwiftUI  
**Kind**: struct

A run of placed glyphs in a text layout.

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
struct Run
```

## Topics

### Instance Properties
- [var characterIndices: [Text.Layout.CharacterIndex]](text/layout/run/characterindices.md)
  The array of character indices corresponding to the glyphs in `self`.
- [var layoutDirection: LayoutDirection](text/layout/run/layoutdirection.md)
  The layout direction of the text run.
- [var typographicBounds: Text.Layout.TypographicBounds](text/layout/run/typographicbounds.md)
  The typographic bounds of the run of glyphs.
### Subscripts
- [subscript<T>(T.Type) -> T?](text/layout/run/subscript(_:).md)
  The custom attribute of type `T` associated with the run of glyphs, or nil.

## Relationships

### Conforms To
- [BidirectionalCollection](../Swift/BidirectionalCollection.md)
- [Collection](../Swift/Collection.md)
- [Equatable](../Swift/Equatable.md)
- [RandomAccessCollection](../Swift/RandomAccessCollection.md)
- [Sequence](../Swift/Sequence.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/text/layout/run)*