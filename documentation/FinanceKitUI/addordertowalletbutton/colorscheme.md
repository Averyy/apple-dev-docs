# colorScheme(_:)

**Framework**: FinanceKitUI  
**Kind**: method

Sets this view’s color scheme.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func colorScheme(_ colorScheme: ColorScheme) -> some View
```

#### Return Value

A view that sets this view’s color scheme.

#### Discussion

Use `colorScheme(_:)` to set the color scheme for the view to which you apply it and any subviews. If you want to set the color scheme for all views in the presentation, use `View/preferredColorScheme(_:)` instead.

## Parameters

- `colorScheme`: The color scheme for this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekitui/addordertowalletbutton/colorscheme(_:))*