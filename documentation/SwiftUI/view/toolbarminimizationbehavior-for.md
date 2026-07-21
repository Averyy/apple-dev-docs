# toolbarMinimizationBehavior(_:for:)

**Framework**: SwiftUI  
**Kind**: method

Sets the minimize behavior for the specified bars.

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
func toolbarMinimizationBehavior(_ behavior: ToolbarMinimizationBehavior, for bars: ToolbarPlacement...) -> some View
```

#### Discussion

Use this modifier to enable toolbar minimization in response to scrolling. The supported placement is [`navigationBar`](toolbarplacement/navigationbar.md). When the navigation bar minimizes, an integrated top tab bar will also minimize.

By default, the safe area adjusts as the navigation bar minimizes. Use [`toolbarMinimizationSafeAreaAdjustment(_:for:)`](view/toolbarminimizationsafeareaadjustment(_:for:).md) to customize this.

```swift
NavigationStack {
    ScrollView {
        ForEach(0 ..< 50) { index in
            Text("\(index)").padding()
        }
    }
    .navigationTitle("Minimizing Title")
    .toolbarMinimizationBehavior(.onScrollDown, for: .navigationBar)
}
```

## Parameters

- `behavior`: The minimize behavior.
- `bars`: The bars to apply the behavior to.

## See Also

- [struct ToolbarMinimizationBehavior](toolbarminimizationbehavior.md)
  The minimization behavior of a toolbar.
- [func toolbarMinimizationRestoration(ToolbarMinimizationRestoration, for: ToolbarPlacement...) -> some View](view/toolbarminimizationrestoration(_:for:).md)
  Sets the restoration behavior for the specified bars during minimization.
- [struct ToolbarMinimizationRestoration](toolbarminimizationrestoration.md)
  The restoration behavior during toolbar minimization.
- [func toolbarMinimizationSafeAreaAdjustment(ToolbarMinimizationSafeAreaAdjustment, for: ToolbarPlacement...) -> some View](view/toolbarminimizationsafeareaadjustment(_:for:).md)
  Sets the safe area adjustment for the specified bars during minimization.
- [struct ToolbarMinimizationSafeAreaAdjustment](toolbarminimizationsafeareaadjustment.md)
  The safe area adjustment during toolbar minimization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/toolbarminimizationbehavior(_:for:))*