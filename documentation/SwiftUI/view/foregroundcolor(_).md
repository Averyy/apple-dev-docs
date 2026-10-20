# foregroundColor(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Sets the color of the foreground elements displayed by this view.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2 (renamed: foregroundStyle(_:))
- iPadOS 13.0+ - Deprecated in 27.2 (renamed: foregroundStyle(_:))
- Mac Catalyst 13.0+ - Deprecated in 27.2 (renamed: foregroundStyle(_:))
- macOS 10.15+ - Deprecated in 27.2 (renamed: foregroundStyle(_:))
- tvOS 13.0+ - Deprecated in 27.2 (renamed: foregroundStyle(_:))
- visionOS 1.0+ - Deprecated in 27.2 (renamed: foregroundStyle(_:))
- watchOS 6.0+ - Deprecated in 27.2 (renamed: foregroundStyle(_:))

> **Deprecated**: Use [`foregroundStyle(_:)`](./foregroundstyle%28_%29.md) instead.

## Declaration

```swift
nonisolated
func foregroundColor(_ color: Color?) -> some View
```

#### Return Value

A view that uses the foreground color you supply.

## Parameters

- `color`: The foreground color to use when displaying this view. Pass `nil` to remove any custom foreground color and to allow the system or the container to provide its own foreground color. If a container-specific override doesn’t exist, the system uses the primary color.

## See Also

### Appearance modifiers
- [func colorScheme(ColorScheme) -> some View](./colorscheme%28_%29.md)
  Sets this view’s color scheme.
- [func listRowPlatterColor(Color?) -> some View](./listrowplattercolor%28_%29.md)
  Sets the color that the system applies to the row background when this view is placed in a list.
- [func background<Background>(Background, alignment: Alignment) -> some View](./background%28_,alignment%29.md)
  Layers the given view behind this view.
- [func overlay<Overlay>(Overlay, alignment: Alignment) -> some View](./overlay%28_,alignment%29.md)
  Layers a secondary view in front of this view.
- [func complicationForeground() -> some View](./complicationforeground%28%29.md)
  Promotes this view to the foreground in a complication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/foregroundcolor(_:))*