# rectangle

**Framework**: SwiftUI  
**Kind**: property

A variant that encapsulates the symbol in a rectangle.

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
static let rectangle: SymbolVariants
```

#### Discussion

Use this variant with a call to the [`symbolVariant(_:)`](view/symbolvariant(_:).md) modifier to draw symbols in a rectangle, for those symbols that have a rectangle variant:

```swift
VStack(spacing: 20) {
    HStack(spacing: 20) {
        Image(systemName: "plus")
        Image(systemName: "minus")
        Image(systemName: "xmark")
        Image(systemName: "checkmark")
    }
    HStack(spacing: 20) {
        Image(systemName: "plus")
        Image(systemName: "minus")
        Image(systemName: "xmark")
        Image(systemName: "checkmark")
    }
    .symbolVariant(.rectangle)
}
```

![A screenshot showing two rows of four symbols each. Both rows contain](https://docs-assets.developer.apple.com/published/2494a548c163c3f2b07cf16fdbad8fd1/SymbolVariants-rectangle-1%402x.png)

## See Also

- [static let none: SymbolVariants](symbolvariants/none.md)
  No variant for a symbol.
- [static let circle: SymbolVariants](symbolvariants/circle-swift.type.property.md)
  A variant that encapsulates the symbol in a circle.
- [static let square: SymbolVariants](symbolvariants/square-swift.type.property.md)
  A variant that encapsulates the symbol in a square.
- [static let fill: SymbolVariants](symbolvariants/fill-swift.type.property.md)
  A variant that fills the symbol.
- [static let slash: SymbolVariants](symbolvariants/slash-swift.type.property.md)
  A variant that draws a slash through the symbol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/symbolvariants/rectangle-swift.type.property)*