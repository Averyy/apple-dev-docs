# scrollIndicatorsFlash(onAppear:)

**Framework**: SwiftUI  
**Kind**: method

Flashes the scroll indicators of a scrollable view when it appears.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
nonisolated
func scrollIndicatorsFlash(onAppear: Bool) -> some View
```

#### Return Value

A view that flashes any visible scroll indicators when it first appears.

#### Discussion

Use this modifier to control whether the scroll indicators of a scroll view briefly flash when the view first appears. For example, you can make the indicators flash by setting the `onAppear` parameter to `true`:

```swift
ScrollView {
    // ...
}
.scrollIndicatorsFlash(onAppear: true)
```

Only scroll indicators that you configure to be visible flash. To flash scroll indicators when a value changes, use [`scrollIndicatorsFlash(trigger:)`](view/scrollindicatorsflash(trigger:).md) instead.

## Parameters

- `onAppear`: A Boolean value that indicates whether the scroll   indicators flash when the scroll view appears.

## See Also

- [func scrollIndicatorsFlash(trigger: some Equatable) -> some View](view/scrollindicatorsflash(trigger:).md)
  Flashes the scroll indicators of scrollable views when a value changes.
- [func scrollIndicators(ScrollIndicatorVisibility, axes: Axis.Set) -> some View](view/scrollindicators(_:axes:).md)
  Sets the visibility of scroll indicators within this view.
- [var horizontalScrollIndicatorVisibility: ScrollIndicatorVisibility](environmentvalues/horizontalscrollindicatorvisibility.md)
  The visibility to apply to scroll indicators of any horizontally scrollable content.
- [var verticalScrollIndicatorVisibility: ScrollIndicatorVisibility](environmentvalues/verticalscrollindicatorvisibility.md)
  The visiblity to apply to scroll indicators of any vertically scrollable content.
- [struct ScrollIndicatorVisibility](scrollindicatorvisibility.md)
  The visibility of scroll indicators of a UI element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/scrollindicatorsflash(onappear:))*