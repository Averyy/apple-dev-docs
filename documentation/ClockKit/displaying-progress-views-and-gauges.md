# Displaying progress views and gauges

**Framework**: ClockKit

Add rich visual data to your SwiftUI complications with progress views and gauges.

#### Overview

Progress views provide a visual depiction of progress on a task by showing the task’s percent complete. You can configure progress views as either a circle or a line, and include an optional label and tint color.

Gauges, on the other hand, depict a value within a given range of values. You configure gauges much as you do progress views, but gauges have even more options, including minimum and maximum value labels and color gradients.

##### Create a Progress View

To instantiate a [`ProgressView`](https://developer.apple.com/documentation/SwiftUI/ProgressView), call the initializer and pass a value.

```swift
// A progress view that is 20% complete.
ProgressView(value: 0.2)
```

By default, the progress view takes a value between 0.0 and 1.0, and visually represents the percentage of the task’s completion.

##### Customize a Progress View

Customize a progress view by selecting a style, adding labels, and setting a tint color. [`ProgressView`](https://developer.apple.com/documentation/SwiftUI/ProgressView) supports linear and circular styles. By default, the SwiftUI selects the style based on the view’s context. However, you can add a `progressViewStyle(_:)` modifier to specify the style.

The following code sets a circular style.

```swift
// A circular progress view.
ProgressView(value: 0.4)
    .progressViewStyle(CircularProgressViewStyle())
```

![A preview of the circular progress view, showing a task that is 40 percent complete.](https://docs-assets.developer.apple.com/published/4678217b2f60ffad7269a219e76e0bd6/media-3686517%402x.png)

The code below sets a linear style.

```swift
// A linear progress view.
ProgressView(value: 0.6)
    .progressViewStyle(LinearProgressViewStyle())
```

![A preview of the linear progress view showing a task that is 60 percent complete.](https://docs-assets.developer.apple.com/published/acba2def2c1bbdb7c649fce880513ab7/media-3686525%402x.png)

[`ProgressView`](https://developer.apple.com/documentation/SwiftUI/ProgressView) also supports a label that describes the task. Pass a closure that returns a [`View`](https://developer.apple.com/documentation/SwiftUI/View) to the progress view’s initializer.

```swift
// A progress view with an image label.
ProgressView(value: 0.8) {
    Image("coffee_template_small")
        .renderingMode(.template)
        .foregroundColor(.yellow)
}
```

![Previews of the circular and linear progress views with a coffee cup image as the label.](https://docs-assets.developer.apple.com/published/2a2066661e45e17c79060f39026681ac/media-3686524%402x.png)

The label appears inside a circular style, and below and to the left of the linear progress bar.

Finally, you can use the `progressViewStyle(_:)` modifier to apply a tint to the progress bar.

```swift
ProgressView(value: 0.4) {
    Image("coffee_template_small")
        .renderingMode(.template)
        .foregroundColor(.yellow)
}
.progressViewStyle(CircularProgressViewStyle(tint: .green))
```

![A preview of the tinted, circular progress view with a green gauge.](https://docs-assets.developer.apple.com/published/3be07fdf6878f851597a960c58993146/media-3686514%402x.png)

##### Create a Gauge

In many ways, the [`Gauge`](https://developer.apple.com/documentation/SwiftUI/Gauge) is similar to the [`ProgressView`](https://developer.apple.com/documentation/SwiftUI/ProgressView). It supports both a linear and circular style, and you can add a label and tinting. The main difference is that the gauge represents a value within a specified range—not the percent complete. It also has additional options, like labels for the range’s minimum, maximum values, and a label for the current value. Finally, it supports color gradients.

##### Customize a Gauge

The following example creates temperature gauge, and then customizes it by adding value labels for the minimum, maximum, and current values. It also assigns a color gradient to the gauge.

```swift
Gauge(value: 76.0, in: 60.0...85.0) {
    Text("ºF")
} currentValueLabel: {
    Text("76")
} minimumValueLabel: {
    Text("60")
} maximumValueLabel: {
    Text("85")
}
.gaugeStyle(
    CircularGaugeStyle(tint:
        Gradient(colors: [.green, .yellow, .orange, .red])))
```

![A preview of the gauge view showing 76 degrees with a high of 85 and a low of 60.](https://docs-assets.developer.apple.com/published/44b5035ff25a6b4640a0d258256c1cf9/media-3686516%402x.png)

Note that the gauge doesn’t show the label (`ºF` in this example) when you specify the minimum and maximum value labels.

## See Also

- [Creating complications for your watchOS app](creating-complications-for-your-watchos-app.md)
  Set up and implement complications for your watchOS app.
- [Declaring complications for your app](declaring-complications-for-your-app.md)
  Define the complications that your app supports.
- [Creating a timeline entry](creating-a-timeline-entry.md)
  Package your app-specific data into a template and create a timeline entry for that template.
- [Loading future timeline events](loading-future-timeline-events.md)
  Preserve battery life and improve performance on the watch by providing a timeline with expected data and updates.
- [Keeping your complications up to date](keeping-your-complications-up-to-date.md)
  Replace or extend the data in your complication’s timeline.
- [Building complications with SwiftUI](building-complications-with-swiftui.md)
  Design the appearance of a graphic complication using SwiftUI.
- [Adding text to a complication](adding-text-to-a-complication.md)
  Use text in SwiftUI complications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/displaying-progress-views-and-gauges)*