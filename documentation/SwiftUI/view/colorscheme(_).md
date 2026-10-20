# colorScheme(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Sets this view’s color scheme.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2 (renamed: preferredColorScheme(_:))
- iPadOS 13.0+ - Deprecated in 27.2 (renamed: preferredColorScheme(_:))
- Mac Catalyst 13.0+ - Deprecated in 27.2 (renamed: preferredColorScheme(_:))
- macOS 10.15+ - Deprecated in 27.2 (renamed: preferredColorScheme(_:))
- tvOS 13.0+ - Deprecated in 27.2 (renamed: preferredColorScheme(_:))
- visionOS 1.0+ - Deprecated in 27.2 (renamed: preferredColorScheme(_:))
- watchOS 6.0+ - Deprecated in 27.2 (renamed: preferredColorScheme(_:))

> **Deprecated**: Use [`preferredColorScheme(_:)`](./preferredcolorscheme%28_%29.md) instead.

## Declaration

```swift
nonisolated
func colorScheme(_ colorScheme: ColorScheme) -> some View
```

#### Return Value

A view that sets this view’s color scheme.

#### Discussion

Use `colorScheme(_:)` to set the color scheme for the view to which you apply it and any subviews.

## Parameters

- `colorScheme`: The color scheme for this view.

## See Also

### Appearance modifiers
- [func listRowPlatterColor(Color?) -> some View](./listrowplattercolor%28_%29.md)
  Sets the color that the system applies to the row background when this view is placed in a list.
- [func background<Background>(Background, alignment: Alignment) -> some View](./background%28_,alignment%29.md)
  Layers the given view behind this view.
- [func overlay<Overlay>(Overlay, alignment: Alignment) -> some View](./overlay%28_,alignment%29.md)
  Layers a secondary view in front of this view.
- [func foregroundColor(Color?) -> some View](./foregroundcolor%28_%29.md)
  Sets the color of the foreground elements displayed by this view.
- [func complicationForeground() -> some View](./complicationforeground%28%29.md)
  Promotes this view to the foreground in a complication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/colorscheme(_:))*