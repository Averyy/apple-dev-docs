# none

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

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

Using this variant with the [`symbolVariant(_:)`](../view/symbolvariant%28_%29.md) modifier doesn’t have any effect. Instead, to show a symbol that ignores the current variant, directly set the [`symbolVariants`](../environmentvalues/symbolvariants.md) environment value to `none` using the [`environment(_:_:)`](../view/environment%28_,_%29.md) modifer:

```swift
HStack {
    Image(systemName: "heart")
    Image(systemName: "heart")
        .environment(\.symbolVariants, .none)
}
.symbolVariant(.fill)
```

![A screenshot of two heart symbols. The first is filled while the](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/SymbolVariants-none-1@2x.png)

## See Also

### Getting symbol variants
- [static let circle: SymbolVariants](./circle-swift.type.property.md)
  A variant that encapsulates the symbol in a circle.
- [static let square: SymbolVariants](./square-swift.type.property.md)
  A variant that encapsulates the symbol in a square.
- [static let rectangle: SymbolVariants](./rectangle-swift.type.property.md)
  A variant that encapsulates the symbol in a rectangle.
- [static let fill: SymbolVariants](./fill-swift.type.property.md)
  A variant that fills the symbol.
- [static let slash: SymbolVariants](./slash-swift.type.property.md)
  A variant that draws a slash through the symbol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/symbolvariants/none)*