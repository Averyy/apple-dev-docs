# Text.Layout.RunSlice

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

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
- [init(run: Text.Layout.Run, indices: Range<Int>)](./runslice/init%28run,indices%29.md)
### Instance Properties
- [var characterIndices: [Text.Layout.CharacterIndex]](./runslice/characterindices.md)
  The array of character indices corresponding to the glyphs in `self`.
- [var run: Text.Layout.Run](./runslice/run.md)
- [var typographicBounds: Text.Layout.TypographicBounds](./runslice/typographicbounds.md)
  The typographic bounds of the partial run of glyphs.
### Subscripts
- [subscript<T>(T.Type) -> T?](./runslice/subscript%28_%29.md)
  The custom attribute of type `T` associated with the run of glyphs, or nil.

## Relationships

### Conforms To
- [BidirectionalCollection](../../../Swift/bidirectionalcollection.md)
- [Collection](../../../Swift/collection.md)
- [Equatable](../../../Swift/equatable.md)
- [RandomAccessCollection](../../../Swift/randomaccesscollection.md)
- [Sequence](../../../Swift/sequence.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/text/layout/runslice)*