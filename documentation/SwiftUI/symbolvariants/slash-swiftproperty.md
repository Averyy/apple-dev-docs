# slash

**Framework**: SwiftUI  
**Kind**: property

A slashed version of the variant.

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
var slash: SymbolVariants { get }
```

#### Discussion

Use this property to modify a shape variant like [`circle`](symbolvariants/circle-swift.type.property.md) so that it’s also covered by a slash:

```swift
Label("Circle Slash", systemImage: "flag")
    .symbolVariant(.circle.slash)
```

![A screenshot of a label that shows a flag in a circle with a](https://docs-assets.developer.apple.com/published/1c6f71949288c728089e2dd937cb61dd/SymbolVariants-slash-2%402x.png)

## See Also

- [var circle: SymbolVariants](symbolvariants/circle-swift.property.md)
  A version of the variant that’s encapsulated in a circle.
- [var square: SymbolVariants](symbolvariants/square-swift.property.md)
  A version of the variant that’s encapsulated in a square.
- [var rectangle: SymbolVariants](symbolvariants/rectangle-swift.property.md)
  A version of the variant that’s encapsulated in a rectangle.
- [var fill: SymbolVariants](symbolvariants/fill-swift.property.md)
  A filled version of the variant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/symbolvariants/slash-swift.property)*