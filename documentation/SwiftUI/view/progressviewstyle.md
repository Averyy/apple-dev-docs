# progressViewStyle(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets the style for progress views in this view.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
nonisolated
func progressViewStyle<S>(_ style: S) -> some View where S : ProgressViewStyle
```

#### Discussion

For example, the following code creates a progress view that uses the “circular” style:

```swift
ProgressView()
    .progressViewStyle(.circular)
```

## Parameters

- `style`: The progress view style to use for this view.

## See Also

- [struct Gauge](gauge.md)
  A view that shows a value within a range.
- [func gaugeStyle<S>(S) -> some View](view/gaugestyle(_:).md)
  Sets the style for gauges within this view.
- [struct ProgressView](progressview.md)
  A view that shows the progress toward completion of a task.
- [struct DefaultDateProgressLabel](defaultdateprogresslabel.md)
  The default type of the current value label when used by a date-relative progress view.
- [struct DefaultButtonLabel](defaultbuttonlabel.md)
  The default label to use for a button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/progressviewstyle(_:))*