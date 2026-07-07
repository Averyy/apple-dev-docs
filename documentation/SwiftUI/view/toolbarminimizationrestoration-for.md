# toolbarMinimizationRestoration(_:for:)

**Framework**: SwiftUI  
**Kind**: method

Sets the restoration behavior for the specified bars during minimization.

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
func toolbarMinimizationRestoration(_ restoration: ToolbarMinimizationRestoration, for bars: ToolbarPlacement...) -> some View
```

#### Discussion

Use this modifier alongside [`toolbarMinimizationBehavior(_:for:)`](view/toolbarminimizationbehavior(_:for:).md) to customize when a minimized bar restores. By default, the bar restores when the user reverses scroll direction. Use [`atScrollEdge`](toolbarminimizationrestoration/atscrolledge.md) to restrict restoration to when the scroll view’s content reaches the scroll edge – appropriate for screens where the bar is mostly chrome that doesn’t need to follow the user.

```swift
NavigationStack {
    ScrollView {
        // ...
    }
    .toolbarMinimizationBehavior(
        .onScrollDown, for: .navigationBar)
    .toolbarMinimizationRestoration(
        .atScrollEdge, for: .navigationBar)
}
```

Currently, only [`navigationBar`](toolbarplacement/navigationbar.md) supports customizing the restoration behavior, and only when used in combination with [`onScrollDown`](toolbarminimizationbehavior/onscrolldown.md).

## Parameters

- `restoration`: The restoration behavior.
- `bars`: The bars to apply the restoration behavior to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/toolbarminimizationrestoration(_:for:))*