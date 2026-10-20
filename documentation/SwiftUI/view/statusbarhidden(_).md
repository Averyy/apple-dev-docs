# statusBarHidden(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Sets the visibility of the status bar.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use .toolbarVisibility(_, for: .statusBar) instead

## Declaration

```swift
@export(implementation)
nonisolated func statusBarHidden(_ hidden: Bool = true) -> some View
```

## Parameters

- `hidden`: A Boolean value that indicates whether to hide the status bar.

## See Also

### Hiding system elements
- [func labelsHidden() -> some View](./labelshidden%28%29.md)
  Hides the labels of any controls contained within this view.
- [func labelsVisibility(Visibility) -> some View](./labelsvisibility%28_%29.md)
  Controls the visibility of labels of any controls contained within this view.
- [var labelsVisibility: Visibility](../environmentvalues/labelsvisibility.md)
  The labels visibility set by [`labelsVisibility(_:)`](./labelsvisibility%28_%29.md).
- [func menuIndicator(Visibility) -> some View](./menuindicator%28_%29.md)
  Sets the menu indicator visibility for controls within this view.
- [func persistentSystemOverlays(Visibility) -> some View](./persistentsystemoverlays%28_%29.md)
  Sets the preferred visibility of the non-transient system views overlaying the app.
- [enum Visibility](../visibility.md)
  The visibility of a UI element, chosen automatically based on the platform, current context, and other factors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/statusbarhidden(_:))*