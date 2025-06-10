# custom

**Framework**: SwiftUI  
**Kind**: property

Does not apply any system effect when selected.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
static let custom: PaletteSelectionEffect
```

#### Discussion

> **Note**: Make sure to manually implement a way to indicate selection when using this case. For example, you could dynamically resolve the item’s image based on the selection state.

## See Also

- [static let automatic: PaletteSelectionEffect](paletteselectioneffect/automatic.md)
  Applies the system’s default effect when selected.
- [static func symbolVariant(SymbolVariants) -> PaletteSelectionEffect](paletteselectioneffect/symbolvariant(_:).md)
  Applies the specified symbol variant when selected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/paletteselectioneffect/custom)*