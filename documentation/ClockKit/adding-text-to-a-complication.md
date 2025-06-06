# Adding text to a complication

**Framework**: ClockKit

Use text in SwiftUI complications.

#### Overview

When creating ClockKit templates with SwiftUI views, [`Text`](https://developer.apple.com/documentation/SwiftUI/Text) views adapt their appearance based on the template’s complication family. The system automatically sets the font and size to match other templates in the same family.

##### Match the Expected Font Size

Use the default font size as a guide for the type of information your complication displays. For example, the [`CLKComplicationTemplateGraphicExtraLargeCircularView`](clkcomplicationtemplategraphicextralargecircularview.md) template provides a large canvas for drawing, but it’s intended to present large, easy-to-read content instead of a lot of small, detailed data.

##### Use Text Formatters

When displaying dates and times, use [`Text.DateStyle`](https://developer.apple.com/documentation/SwiftUI/Text/DateStyle) to create localized strings. [`Text.DateStyle`](https://developer.apple.com/documentation/SwiftUI/Text/DateStyle) also defines formatters such as [`relative`](https://developer.apple.com/documentation/SwiftUI/Text/DateStyle/relative), [`offset`](https://developer.apple.com/documentation/SwiftUI/Text/DateStyle/offset), and [`timer`](https://developer.apple.com/documentation/SwiftUI/Text/DateStyle/timer). ClockKit automatically updates information in these formatters, and you can use these formatters when instantiating a [`Text`](https://developer.apple.com/documentation/SwiftUI/Text) view.

```swift
Text(myEvent.startDate, style: .timer)
```

Or use them inline in an interpolated string.

```swift
Text("\(myEvent.name) starts in \(myEvent.startDate, style: .timer)")
```

![A preview of a large rectangular complication with a text view that displays a timer that automatically counts down to the next event.](https://docs-assets.developer.apple.com/published/2aeb07ea3989a2e71c8c6879a28a474d/media-3666648%402x.png)

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
- [Displaying progress views and gauges](displaying-progress-views-and-gauges.md)
  Add rich visual data to your SwiftUI complications with progress views and gauges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/adding-text-to-a-complication)*