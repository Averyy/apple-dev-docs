# fill

**Framework**: SwiftUI  
**Kind**: property

A filled version of the variant.

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
var fill: SymbolVariants { get }
```

#### Discussion

Use this property to modify a shape variant like [`circle`](symbolvariants/circle-swift.type.property.md) so that it’s also filled:

```swift
Label("Circle Fill", systemImage: "flag")
    .symbolVariant(.circle.fill)
```

![A screenshot of a label that shows a flag in a filled circle](https://docs-assets.developer.apple.com/published/bfe960b3acc307e9c52f35cbe25c29c7/SymbolVariants-fill-2%402x.png)

## See Also

- [var circle: SymbolVariants](symbolvariants/circle-swift.property.md)
  A version of the variant that’s encapsulated in a circle.
- [var square: SymbolVariants](symbolvariants/square-swift.property.md)
  A version of the variant that’s encapsulated in a square.
- [var rectangle: SymbolVariants](symbolvariants/rectangle-swift.property.md)
  A version of the variant that’s encapsulated in a rectangle.
- [var slash: SymbolVariants](symbolvariants/slash-swift.property.md)
  A slashed version of the variant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/symbolvariants/fill-swift.property)*