# rectangle

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

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

Use this variant with a call to the [`symbolVariant(_:)`](../view/symbolvariant%28_%29.md) modifier to draw symbols in a rectangle, for those symbols that have a rectangle variant:

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

![A screenshot showing two rows of four symbols each. Both rows contain](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/SymbolVariants-rectangle-1@2x.png)

## See Also

### Getting symbol variants
- [static let none: SymbolVariants](./none.md)
  No variant for a symbol.
- [static let circle: SymbolVariants](./circle-swift.type.property.md)
  A variant that encapsulates the symbol in a circle.
- [static let square: SymbolVariants](./square-swift.type.property.md)
  A variant that encapsulates the symbol in a square.
- [static let fill: SymbolVariants](./fill-swift.type.property.md)
  A variant that fills the symbol.
- [static let slash: SymbolVariants](./slash-swift.type.property.md)
  A variant that draws a slash through the symbol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/symbolvariants/rectangle-swift.type.property)*