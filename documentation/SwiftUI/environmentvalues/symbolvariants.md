# symbolVariants

**Framework**: SwiftUI  
**Kind**: property

The symbol variant to use in this environment.

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
var symbolVariants: SymbolVariants { get set }
```

#### Discussion

You set this environment value indirectly by using the [`symbolVariant(_:)`](view/symbolvariant(_:).md) view modifier. However, you access the environment variable directly using the [`environment(_:_:)`](view/environment(_:_:).md) modifier. Do this when you want to use the [`none`](symbolvariants/none.md) variant to ignore the value that’s already in the environment:

```swift
HStack {
    Image(systemName: "heart")
    Image(systemName: "heart")
        .environment(\.symbolVariants, .none)
}
.symbolVariant(.fill)
```

![A screenshot of two heart symbols. The first is filled while the](/images/com.apple.SwiftUI/SymbolVariants-none-1@2x.png)

## See Also

- [func symbolVariant(SymbolVariants) -> some View](view/symbolvariant(_:).md)
  Makes symbols within the view show a particular variant.
- [struct SymbolVariants](symbolvariants.md)
  A variant of a symbol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/symbolvariants)*