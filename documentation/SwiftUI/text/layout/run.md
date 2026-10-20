# Text.Layout.Run

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

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
- [var characterIndices: [Text.Layout.CharacterIndex]](./run/characterindices.md)
  The array of character indices corresponding to the glyphs in `self`.
- [var layoutDirection: LayoutDirection](./run/layoutdirection.md)
  The layout direction of the text run.
- [var typographicBounds: Text.Layout.TypographicBounds](./run/typographicbounds.md)
  The typographic bounds of the run of glyphs.
### Subscripts
- [subscript<T>(T.Type) -> T?](./run/subscript%28_%29.md)
  The custom attribute of type `T` associated with the run of glyphs, or nil. If no run contains the custom attribute we also check its attachment’s runs.

## Relationships

### Conforms To
- [BidirectionalCollection](../../../Swift/bidirectionalcollection.md)
- [Collection](../../../Swift/collection.md)
- [Equatable](../../../Swift/equatable.md)
- [RandomAccessCollection](../../../Swift/randomaccesscollection.md)
- [Sequence](../../../Swift/sequence.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/text/layout/run)*