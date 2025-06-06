# square

**Framework**: SwiftUI  
**Kind**: property

A version of the variant that’s encapsulated in a square.

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
var square: SymbolVariants { get }
```

#### Discussion

Use this property to modify a variant like [`fill`](symbolvariants/fill-swift.property.md) so that it’s also contained in a square:

```swift
Label("Fill Square", systemImage: "star")
    .symbolVariant(.fill.square)
```

![A screenshot of a label that shows a star in a filled square](https://docs-assets.developer.apple.com/published/591d44c3cb28ab6dd1362093cff5fbd7/SymbolVariants-square-2%402x.png)

## See Also

- [var circle: SymbolVariants](symbolvariants/circle-swift.property.md)
  A version of the variant that’s encapsulated in a circle.
- [var rectangle: SymbolVariants](symbolvariants/rectangle-swift.property.md)
  A version of the variant that’s encapsulated in a rectangle.
- [var fill: SymbolVariants](symbolvariants/fill-swift.property.md)
  A filled version of the variant.
- [var slash: SymbolVariants](symbolvariants/slash-swift.property.md)
  A slashed version of the variant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/symbolvariants/square-swift.property)*