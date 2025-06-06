# ProgressView

**Framework**: SwiftUI  
**Kind**: struct

A view that shows the progress toward completion of a task.

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
struct ProgressView<Label, CurrentValueLabel> where Label : View, CurrentValueLabel : View
```

## Mentions

- [Declaring a custom view](declaring-a-custom-view.md)

#### Overview

Use a progress view to show that a task is incomplete but advancing toward completion. A progress view can show both determinate (percentage complete) and indeterminate (progressing or not) types of progress.

Create a determinate progress view by initializing a `ProgressView` with a binding to a numeric value that indicates the progress, and a `total` value that represents completion of the task. By default, the progress is `0.0` and the total is `1.0`.

The example below uses the state property `progress` to show progress in a determinate `ProgressView`. The progress view uses its default total of `1.0`, and because `progress` starts with an initial value of `0.5`, the progress view begins half-complete. A “More” button below the progress view allows people to increment the progress in increments of five percent:

```swift
struct LinearProgressDemoView: View {
    @State private var progress = 0.5

    var body: some View {
        VStack {
            ProgressView(value: progress)
            Button("More") { progress += 0.05 }
        }
    }
}
```

![A horizontal bar that represents progress, with a More button](https://docs-assets.developer.apple.com/published/3456594d290f72e26be845c9f9a84d6d/ProgressView-1-macOS%402x.png)

To create an indeterminate progress view, use an initializer that doesn’t take a progress value:

```swift
var body: some View {
    ProgressView()
}
```

![An indeterminate progress view, presented as a spinning set of gray lines](https://docs-assets.developer.apple.com/published/23f14adddc00728dc65bed3ebbe411e7/ProgressView-2-macOS%402x.png)

You can also create a progress view that covers a closed range of [`Date`](https://developer.apple.com/documentation/Foundation/Date) values. As long as the current date is within the range, the progress view automatically updates, filling or depleting the progress view as it nears the end of the range. The following example shows a five-minute timer whose start time is that of the progress view’s initialization:

```swift
struct DateRelativeProgressDemoView: View {
    let workoutDateRange = Date()...Date().addingTimeInterval(5*60)

    var body: some View {
         ProgressView(timerInterval: workoutDateRange) {
             Text("Workout")
         }
    }
}
```

![A horizontal progress view that shows a bar partially filled with as it](https://docs-assets.developer.apple.com/published/115df9b28ca681ce09da67b5bcbb3e7d/ProgressView-3-macOS%402x.png)

##### Styling Progress Views

You can customize the appearance and interaction of progress views by creating styles that conform to the [`ProgressViewStyle`](progressviewstyle.md) protocol. To set a specific style for all progress view instances within a view, use the [`progressViewStyle(_:)`](view/progressviewstyle(_:).md) modifier. In the following example, a custom style adds a rounded pink border to all progress views within the enclosing [`VStack`](vstack.md):

```swift
struct BorderedProgressViews: View {
    var body: some View {
        VStack {
            ProgressView(value: 0.25) { Text("25% progress") }
            ProgressView(value: 0.75) { Text("75% progress") }
        }
        .progressViewStyle(PinkBorderedProgressViewStyle())
    }
}

struct PinkBorderedProgressViewStyle: ProgressViewStyle {
    func makeBody(configuration: Configuration) -> some View {
        ProgressView(configuration)
            .padding(4)
            .border(.pink, width: 3)
            .cornerRadius(4)
    }
}
```

![Two horizontal progress views, one at 25 percent complete and the other at 75 percent,](https://docs-assets.developer.apple.com/published/dc98a460b4d5e6b5babf527056cf7298/ProgressView-4-macOS%402x.png)

SwiftUI provides two built-in progress view styles, [`linear`](progressviewstyle/linear.md) and [`circular`](progressviewstyle/circular.md), as well as an automatic style that defaults to the most appropriate style in the current context. The following example shows a circular progress view that starts at 60 percent completed.

```swift
struct CircularProgressDemoView: View {
    @State private var progress = 0.6

    var body: some View {
        VStack {
            ProgressView(value: progress)
                .progressViewStyle(.circular)
        }
    }
}
```

![A ring shape, filled to 60 percent completion with a blue](https://docs-assets.developer.apple.com/published/a8e6132e107636866628b393aeccaa93/ProgressView-5-macOS%402x.png)

On platforms other than macOS, the circular style may appear as an indeterminate indicator instead.

## Topics

### Creating an indeterminate progress view
- [init()](progressview/init.md)
  Creates a progress view for showing indeterminate progress, without a label.
- [init(label: () -> Label)](progressview/init(label:).md)
  Creates a progress view for showing indeterminate progress that displays a custom label.
- [init(LocalizedStringKey)](progressview/init(_:)-6k5se.md)
  Creates a progress view for showing indeterminate progress that generates its label from a localized string.
- [init<S>(S)](progressview/init(_:)-3q5nf.md)
  Creates a progress view for showing indeterminate progress that generates its label from a string.
### Creating a determinate progress view
- [init(Progress)](progressview/init(_:)-l5vj.md)
  Creates a progress view for visualizing the given progress instance.
- [init<V>(value: V?, total: V)](progressview/init(value:total:).md)
  Creates a progress view for showing determinate progress.
- [init(_:value:total:)](progressview/init(_:value:total:).md)
  Creates a progress view for showing determinate progress that generates its label from a string.
- [init<V>(value: V?, total: V, label: () -> Label)](progressview/init(value:total:label:).md)
  Creates a progress view for showing determinate progress, with a custom label.
- [init<V>(value: V?, total: V, label: () -> Label, currentValueLabel: () -> CurrentValueLabel)](progressview/init(value:total:label:currentvaluelabel:).md)
  Creates a progress view for showing determinate progress, with a custom label.
### Create a progress view spanning a date range
- [init(timerInterval: ClosedRange<Date>, countsDown: Bool)](progressview/init(timerinterval:countsdown:).md)
  Creates a progress view for showing continuous progress as time passes.
- [init(timerInterval: ClosedRange<Date>, countsDown: Bool, label: () -> Label)](progressview/init(timerinterval:countsdown:label:).md)
  Creates a progress view for showing continuous progress as time passes, with a descriptive label.
- [init(timerInterval: ClosedRange<Date>, countsDown: Bool, label: () -> Label, currentValueLabel: () -> CurrentValueLabel)](progressview/init(timerinterval:countsdown:label:currentvaluelabel:).md)
  Creates a progress view for showing continuous progress as time passes, with descriptive and current progress labels.
### Initializers
- [init(_:)](progressview/init(_:).md)
  Creates a progress view based on a style configuration.

## Relationships

### Conforms To
- [View](view.md)

## See Also

- [struct Gauge](gauge.md)
  A view that shows a value within a range.
- [func gaugeStyle<S>(S) -> some View](view/gaugestyle(_:).md)
  Sets the style for gauges within this view.
- [func progressViewStyle<S>(S) -> some View](view/progressviewstyle(_:).md)
  Sets the style for progress views in this view.
- [struct DefaultDateProgressLabel](defaultdateprogresslabel.md)
  The default type of the current value label when used by a date-relative progress view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/progressview)*