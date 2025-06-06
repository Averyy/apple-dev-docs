# SymbolVariants

**Framework**: SwiftUI  
**Kind**: struct

A variant of a symbol.

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
struct SymbolVariants
```

#### Overview

Many of the [`SF Symbols`](https://developer.apple.com/design/Human-Interface-Guidelines/sf-symbols) that you can add to your app using an [`Image`](image.md) or a [`Label`](label.md) instance have common variants, like a filled version or a version that’s contained within a circle. The symbol’s name indicates the variant:

```swift
VStack(alignment: .leading) {
    Label("Default", systemImage: "heart")
    Label("Fill", systemImage: "heart.fill")
    Label("Circle", systemImage: "heart.circle")
    Label("Circle Fill", systemImage: "heart.circle.fill")
}
```

![A screenshot showing an outlined heart, a filled heart, a heart in](https://docs-assets.developer.apple.com/published/8cf2af925aa53e568847c8f7e4f67777/SymbolVariants-1%402x.png)

You can configure a part of your view hierarchy to use a particular variant for all symbols in that view and its child views using `SymbolVariants`. Add the [`symbolVariant(_:)`](view/symbolvariant(_:).md) modifier to a view to set a variant for that view’s environment. For example, you can use the modifier to create the same set of labels as in the example above, using only the base name of the symbol in the label declarations:

```swift
VStack(alignment: .leading) {
    Label("Default", systemImage: "heart")
    Label("Fill", systemImage: "heart")
        .symbolVariant(.fill)
    Label("Circle", systemImage: "heart")
        .symbolVariant(.circle)
    Label("Circle Fill", systemImage: "heart")
        .symbolVariant(.circle.fill)
}
```

Alternatively, you can set the variant in the environment directly by passing the [`symbolVariants`](environmentvalues/symbolvariants.md) environment value to the [`environment(_:_:)`](view/environment(_:_:).md) modifier:

```swift
Label("Fill", systemImage: "heart")
    .environment(\.symbolVariants, .fill)
```

SwiftUI sets a variant for you in some environments. For example, SwiftUI automatically applies the [`fill`](symbolvariants/fill-swift.type.property.md) symbol variant for items that appear in the `content` closure of the [`swipeActions(edge:allowsFullSwipe:content:)`](view/swipeactions(edge:allowsfullswipe:content:).md) method, or as the tab bar items of a [`TabView`](tabview.md).

## Topics

### Getting symbol variants
- [static let none: SymbolVariants](symbolvariants/none.md)
  No variant for a symbol.
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
### Modifying a variant
- [var circle: SymbolVariants](symbolvariants/circle-swift.property.md)
  A version of the variant that’s encapsulated in a circle.
- [var square: SymbolVariants](symbolvariants/square-swift.property.md)
  A version of the variant that’s encapsulated in a square.
- [var rectangle: SymbolVariants](symbolvariants/rectangle-swift.property.md)
  A version of the variant that’s encapsulated in a rectangle.
- [var fill: SymbolVariants](symbolvariants/fill-swift.property.md)
  A filled version of the variant.
- [var slash: SymbolVariants](symbolvariants/slash-swift.property.md)
  A slashed version of the variant.
### Comparing variants
- [func contains(SymbolVariants) -> Bool](symbolvariants/contains(_:).md)
  Returns a Boolean value that indicates whether the current variant contains the specified variant.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func symbolVariant(SymbolVariants) -> some View](view/symbolvariant(_:).md)
  Makes symbols within the view show a particular variant.
- [var symbolVariants: SymbolVariants](environmentvalues/symbolvariants.md)
  The symbol variant to use in this environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/symbolvariants)*