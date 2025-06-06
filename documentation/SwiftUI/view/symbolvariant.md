# symbolVariant(_:)

**Framework**: SwiftUI  
**Kind**: method

Makes symbols within the view show a particular variant.

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
nonisolated
func symbolVariant(_ variant: SymbolVariants) -> some View
```

#### Return Value

A view that applies the specified symbol variant or variants to itself and its child views.

#### Discussion

When you want all the [`SF Symbols`](https://developer.apple.com/design/Human-Interface-Guidelines/sf-symbols) in a part of your app’s user interface to use the same variant, use the `symbolVariant(_:)` modifier with a [`SymbolVariants`](symbolvariants.md) value, like [`fill`](symbolvariants/fill-swift.type.property.md):

```swift
VStack(spacing: 20) {
    HStack(spacing: 20) {
        Image(systemName: "person")
        Image(systemName: "folder")
        Image(systemName: "gearshape")
        Image(systemName: "list.bullet")
    }

    HStack(spacing: 20) {
        Image(systemName: "person")
        Image(systemName: "folder")
        Image(systemName: "gearshape")
        Image(systemName: "list.bullet")
    }
    .symbolVariant(.fill) // Shows filled variants, when available.
}
```

A symbol that doesn’t have the specified variant remains unaffected. In the example above, the `list.bullet` symbol doesn’t have a filled variant, so the `symbolVariant(_:)` modifer has no effect.

![A screenshot showing two rows of four symbols. Both rows contain a](https://docs-assets.developer.apple.com/published/101616116d85f2d65120a60c8df2c8c5/View-symbolVariant-1%402x.png)

If you apply the modifier more than once, its effects accumulate. Alternatively, you can apply multiple variants in one call:

```swift
Label("Airplane", systemImage: "airplane.circle.fill")

Label("Airplane", systemImage: "airplane")
    .symbolVariant(.circle)
    .symbolVariant(.fill)

Label("Airplane", systemImage: "airplane")
    .symbolVariant(.circle.fill)
```

All of the labels in the code above produce the same output:

![A screenshot of a label that shows an airplane in a filled circle](https://docs-assets.developer.apple.com/published/a5f6c4ed259fb2c02438f67a3dc5e9a1/View-symbolVariant-2%402x.png)

You can apply all these variants in any order, but if you apply more than one shape variant, the one closest to the symbol takes precedence. For example, the following image uses the [`square`](symbolvariants/square-swift.type.property.md) shape:

```swift
Image(systemName: "arrow.left")
    .symbolVariant(.square) // This shape takes precedence.
    .symbolVariant(.circle)
    .symbolVariant(.fill)
```

![A screenshot of a left arrow symbol in a filled](https://docs-assets.developer.apple.com/published/b522e834c28745be154c9812b0e1971f/View-symbolVariant-3%402x.png)

To cause a symbol to ignore the variants currently in the environment, directly set the [`symbolVariants`](environmentvalues/symbolvariants.md) environment value to [`none`](symbolvariants/none.md) using the [`environment(_:_:)`](view/environment(_:_:).md) modifer.

## Parameters

- `variant`: The variant to use for symbols. Use the values in   .

## See Also

- [var symbolVariants: SymbolVariants](environmentvalues/symbolvariants.md)
  The symbol variant to use in this environment.
- [struct SymbolVariants](symbolvariants.md)
  A variant of a symbol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/symbolvariant(_:))*