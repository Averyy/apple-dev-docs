# square

**Framework**: SwiftUI  
**Kind**: property

A variant that encapsulates the symbol in a square.

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
static let square: SymbolVariants
```

#### Discussion

Use this variant with a call to the [`symbolVariant(_:)`](view/symbolvariant(_:).md) modifier to draw symbols in a square, for those symbols that have a square variant:

```swift
VStack(spacing: 20) {
    HStack(spacing: 20) {
        Image(systemName: "flag")
        Image(systemName: "heart")
        Image(systemName: "bolt")
        Image(systemName: "star")
    }
    HStack(spacing: 20) {
        Image(systemName: "flag")
        Image(systemName: "heart")
        Image(systemName: "bolt")
        Image(systemName: "star")
    }
    .symbolVariant(.square)
}
```

![A screenshot showing two rows of four symbols each. Both rows contain](https://docs-assets.developer.apple.com/published/b7f04f50126637808d0319b25fa43b61/SymbolVariants-square-1%402x.png)

## See Also

- [static let none: SymbolVariants](symbolvariants/none.md)
  No variant for a symbol.
- [static let circle: SymbolVariants](symbolvariants/circle-swift.type.property.md)
  A variant that encapsulates the symbol in a circle.
- [static let rectangle: SymbolVariants](symbolvariants/rectangle-swift.type.property.md)
  A variant that encapsulates the symbol in a rectangle.
- [static let fill: SymbolVariants](symbolvariants/fill-swift.type.property.md)
  A variant that fills the symbol.
- [static let slash: SymbolVariants](symbolvariants/slash-swift.type.property.md)
  A variant that draws a slash through the symbol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/symbolvariants/square-swift.type.property)*