# fill

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

A variant that fills the symbol.

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
static let fill: SymbolVariants
```

## Discussion

Use this variant with a call to the [`symbolVariant(_:)`](../view/symbolvariant%28_%29.md) modifier to draw filled symbols, for those symbols that have a filled variant:

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
    .symbolVariant(.fill)
}
```

![A screenshot showing two rows of four symbols each. Both rows contain](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/SymbolVariants-fill-1@2x.png)

## See Also

### Getting symbol variants
- [static let none: SymbolVariants](./none.md)
  No variant for a symbol.
- [static let circle: SymbolVariants](./circle-swift.type.property.md)
  A variant that encapsulates the symbol in a circle.
- [static let square: SymbolVariants](./square-swift.type.property.md)
  A variant that encapsulates the symbol in a square.
- [static let rectangle: SymbolVariants](./rectangle-swift.type.property.md)
  A variant that encapsulates the symbol in a rectangle.
- [static let slash: SymbolVariants](./slash-swift.type.property.md)
  A variant that draws a slash through the symbol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/symbolvariants/fill-swift.type.property)*