# statusBarHidden(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets the visibility of the status bar.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
func statusBarHidden(_ hidden: Bool = true) -> some View
```

## Parameters

- `hidden`: A Boolean value that indicates whether to hide the   status bar.

## See Also

- [func labelsHidden() -> some View](view/labelshidden.md)
  Hides the labels of any controls contained within this view.
- [func labelsVisibility(Visibility) -> some View](view/labelsvisibility(_:).md)
  Controls the visibility of labels of any controls contained within this view.
- [var labelsVisibility: Visibility](environmentvalues/labelsvisibility.md)
  The labels visibility set by [`labelsVisibility(_:)`](view/labelsvisibility(_:).md).
- [func menuIndicator(Visibility) -> some View](view/menuindicator(_:).md)
  Sets the menu indicator visibility for controls within this view.
- [func persistentSystemOverlays(Visibility) -> some View](view/persistentsystemoverlays(_:).md)
  Sets the preferred visibility of the non-transient system views overlaying the app.
- [enum Visibility](visibility.md)
  The visibility of a UI element, chosen automatically based on the platform, current context, and other factors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/statusbarhidden(_:))*