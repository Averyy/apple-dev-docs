# automatic

**Framework**: SwiftUI  
**Kind**: property

Applies the system’s default effect when selected.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
static let automatic: PaletteSelectionEffect
```

#### Discussion

When using un-tinted SF Symbols or template images, the current tint color is applied to the selected items’ image. If the provided SF Symbols have custom tints, a stroke is drawn around selected items.

## See Also

- [static let custom: PaletteSelectionEffect](paletteselectioneffect/custom.md)
  Does not apply any system effect when selected.
- [static func symbolVariant(SymbolVariants) -> PaletteSelectionEffect](paletteselectioneffect/symbolvariant(_:).md)
  Applies the specified symbol variant when selected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/paletteselectioneffect/automatic)*