# rectangle

**Framework**: SwiftUI  
**Kind**: property

A version of the variant that’s encapsulated in a rectangle.

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
var rectangle: SymbolVariants { get }
```

#### Discussion

Use this property to modify a variant like [`fill`](symbolvariants/fill-swift.property.md) so that it’s also contained in a rectangle:

```swift
Label("Fill Rectangle", systemImage: "plus")
    .symbolVariant(.fill.rectangle)
```

![A screenshot of a label that shows a plus sign in a filled rectangle](https://docs-assets.developer.apple.com/published/e149c895cf10d709dc7bd7c57ccddd00/SymbolVariants-rectangle-2%402x.png)

## See Also

- [var circle: SymbolVariants](symbolvariants/circle-swift.property.md)
  A version of the variant that’s encapsulated in a circle.
- [var square: SymbolVariants](symbolvariants/square-swift.property.md)
  A version of the variant that’s encapsulated in a square.
- [var fill: SymbolVariants](symbolvariants/fill-swift.property.md)
  A filled version of the variant.
- [var slash: SymbolVariants](symbolvariants/slash-swift.property.md)
  A slashed version of the variant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/symbolvariants/rectangle-swift.property)*