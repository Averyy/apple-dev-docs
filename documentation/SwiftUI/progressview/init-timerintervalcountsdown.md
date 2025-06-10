# init(timerInterval:countsDown:)

**Framework**: SwiftUI  
**Kind**: init

Creates a progress view for showing continuous progress as time passes.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
init(timerInterval: ClosedRange<Date>, countsDown: Bool = true)
```

#### Discussion

Use this initializer to create a view that shows continuous progress within a date range. The following example initializes a progress view with a range of `start...end`, where `start` is 30 seconds in the past and `end` is 90 seconds in the future. As a result, the progress view begins at 25 percent complete.

```swift
struct ContentView: View {
    let start = Date().addingTimeInterval(-30)
    let end = Date().addingTimeInterval(90)

    var body: some View {
        ProgressView(interval: start...end
                     countsDown: false)
    }
}
```

![A horizontal bar that represents progress, partially filled in from](https://docs-assets.developer.apple.com/published/ae9d9e19ddc35cebb304375cd9f41ff2/ProgressView-8-macOS%402x.png)

By default, the progress view empties as time passes from the start of the date range to the end, but you can use the `countsDown` parameter to create a progress view that fills as time passes, as the above example demonstrates.

The progress view provided by this initializer omits a descriptive label and provides a text label that automatically updates to describe the current time remaining. To provide custom views for these labels, use [`init(value:total:label:currentValueLabel:)`](progressview/init(value:total:label:currentvaluelabel:).md) instead.

> **Note**: Date-relative progress views, such as those created with this initializer, don’t support custom styles.

## Parameters

- `timerInterval`: The date range over which the view progresses.
- `countsDown`: If   (the default), the view empties as time passes.

## See Also

- [init(timerInterval: ClosedRange<Date>, countsDown: Bool, label: () -> Label)](progressview/init(timerinterval:countsdown:label:).md)
  Creates a progress view for showing continuous progress as time passes, with a descriptive label.
- [init(timerInterval: ClosedRange<Date>, countsDown: Bool, label: () -> Label, currentValueLabel: () -> CurrentValueLabel)](progressview/init(timerinterval:countsdown:label:currentvaluelabel:).md)
  Creates a progress view for showing continuous progress as time passes, with descriptive and current progress labels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/progressview/init(timerinterval:countsdown:))*