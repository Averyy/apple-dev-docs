# toolbarMinimizationSafeAreaAdjustment(_:for:)

**Framework**: SwiftUI  
**Kind**: method

Sets the safe area adjustment for the specified bars during minimization.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
nonisolated
func toolbarMinimizationSafeAreaAdjustment(_ adjustment: ToolbarMinimizationSafeAreaAdjustment, for bars: ToolbarPlacement...) -> some View
```

#### Discussion

By default, the safe area adjusts as bars minimize, allowing content to reflow into the space vacated by the bar. Use this modifier to disable that adjustment when content should remain in place – for example, when displaying full-bleed media beneath a minimizing bar.

Currently, only [`navigationBar`](toolbarplacement/navigationbar.md) supports customizing the safe area adjustment.

Use this modifier alongside [`toolbarMinimizeBehavior(_:for:)`](view/toolbarminimizebehavior(_:for:).md):

```swift
NavigationStack {
    ScrollView {
        // ...
    }
    .toolbarMinimizeBehavior(
        .onScrollDown, for: .navigationBar)
    .toolbarMinimizationSafeAreaAdjustment(
        .disabled, for: .navigationBar)
}
```

## Parameters

- `adjustment`: The safe area adjustment.
- `bars`: The bars to apply the adjustment to.

## See Also

- [func toolbarMinimizeBehavior(ToolbarMinimizeBehavior, for: ToolbarPlacement...) -> some View](view/toolbarminimizebehavior(_:for:).md)
  Sets the minimize behavior for the specified bars.
- [struct ToolbarMinimizeBehavior](toolbarminimizebehavior.md)
  The minimize behavior of a toolbar.
- [struct ToolbarMinimizationSafeAreaAdjustment](toolbarminimizationsafeareaadjustment.md)
  The safe area adjustment during toolbar minimization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/toolbarminimizationsafeareaadjustment(_:for:))*