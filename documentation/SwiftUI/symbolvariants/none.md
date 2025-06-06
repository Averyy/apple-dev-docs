# none

**Framework**: SwiftUI  
**Kind**: property

No variant for a symbol.

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
static let none: SymbolVariants
```

#### Discussion

Using this variant with the [`symbolVariant(_:)`](view/symbolvariant(_:).md) modifier doesn’t have any effect. Instead, to show a symbol that ignores the current variant, directly set the [`symbolVariants`](environmentvalues/symbolvariants.md) environment value to `none` using the [`environment(_:_:)`](view/environment(_:_:).md) modifer:

```swift
HStack {
    Image(systemName: "heart")
    Image(systemName: "heart")
        .environment(\.symbolVariants, .none)
}
.symbolVariant(.fill)
```

![A screenshot of two heart symbols. The first is filled while the](https://docs-assets.developer.apple.com/published/0071b4dbd1f82a57559c954e321a4709/SymbolVariants-none-1%402x.png)

## See Also

- [static let circle: SymbolVariants](symbolvariants/circle-swift.type.property.md)
  A variant that encapsulates the symbol in a circle.
- [static let square: SymbolVariants](symbolvariants/square-swift.type.property.md)
  A variant that encapsulates the symbol in a square.
- [static let rectangle: SymbolVariants](symbolvariants/rectangle-swift.type.property.md)
  A variant that encapsulates the symbol in a rectangle.
- [static let fill: SymbolVariants](symbolvariants/fill-swift.type.property.md)
  A variant that fills the symbol.
- [static let slash: SymbolVariants](symbolvariants/slash-swift.type.property.md)
  A variant that draws a slash through the symbol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/symbolvariants/none)*