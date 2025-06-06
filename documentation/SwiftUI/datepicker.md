# DatePicker

**Framework**: SwiftUI  
**Kind**: struct

A control for selecting an absolute date.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
struct DatePicker<Label> where Label : View
```

## Mentions

- [Laying out a simple view](laying-out-a-simple-view.md)

#### Overview

Use a `DatePicker` when you want to provide a view that allows the user to select a calendar date, and optionally a time. The view binds to a [`Date`](https://developer.apple.com/documentation/Foundation/Date) instance.

The following example creates a basic `DatePicker`, which appears on iOS as text representing the date. This example limits the display to only the calendar date, not the time. When the user taps or clicks the text, a calendar view animates in, from which the user can select a date. When the user dismisses the calendar view, the view updates the bound [`Date`](https://developer.apple.com/documentation/Foundation/Date).

```swift
@State private var date = Date()

var body: some View {
    DatePicker(
        "Start Date",
        selection: $date,
        displayedComponents: [.date]
    )
}
```

![An iOS date picker, consisting of a label that says Start Date, and a](https://docs-assets.developer.apple.com/published/ed0862721b31a474967e7049f9543333/SwiftUI-DatePicker-basic%402x.png)

For cases where adding a subtitle to the label is desired, use a view builder that creates multiple `Text` views where the first text represents the title and the second text represents the subtitle:

```swift
@State private var date = Date()

var body: some View {
    DatePicker(selection: $date) {
        Text("Start Date")
        Text("Select the starting date for the event")
    }
}
```

You can limit the `DatePicker` to specific ranges of dates, allowing selections only before or after a certain date, or between two dates. The following example shows a date-and-time picker that only permits selections within the year 2021 (in the `UTC` time zone).

```swift
@State private var date = Date()
let dateRange: ClosedRange<Date> = {
    let calendar = Calendar.current
    let startComponents = DateComponents(year: 2021, month: 1, day: 1)
    let endComponents = DateComponents(year: 2021, month: 12, day: 31, hour: 23, minute: 59, second: 59)
    return calendar.date(from:startComponents)!
        ...
        calendar.date(from:endComponents)!
}()

var body: some View {
    DatePicker(
        "Start Date",
         selection: $date,
         in: dateRange,
         displayedComponents: [.date, .hourAndMinute]
    )
}
```

![A SwiftUI standard date picker on iOS, with the label Start Date, and](https://docs-assets.developer.apple.com/published/811b3c52683f9dd68a1b3851be4a16f9/SwiftUI-DatePicker-selectFromRange%402x.png)

##### Styling Date Pickers

To use a different style of date picker, use the [`datePickerStyle(_:)`](view/datepickerstyle(_:).md) view modifier. The following example shows the graphical date picker style.

```swift
@State private var date = Date()

var body: some View {
    DatePicker(
        "Start Date",
        selection: $date,
        displayedComponents: [.date]
    )
    .datePickerStyle(.graphical)
}
```

![A SwiftUI date picker using the graphical style, with the label Start Date](https://docs-assets.developer.apple.com/published/1f0eadb9ff4b7e560414a63daf82ff2a/SwiftUI-DatePicker-graphicalStyle%402x.png)

## Topics

### Creating a date picker for any date
- [init(_:selection:displayedComponents:)](datepicker/init(_:selection:displayedcomponents:).md)
  Creates an instance that selects a `Date` with an unbounded range.
- [init(selection: Binding<Date>, displayedComponents: DatePicker<Label>.Components, label: () -> Label)](datepicker/init(selection:displayedcomponents:label:).md)
  Creates an instance that selects a `Date` with an unbounded range.
### Creating a date picker for specific dates
- [init(_:selection:in:displayedComponents:)](datepicker/init(_:selection:in:displayedcomponents:).md)
  Creates an instance that selects a `Date` in a closed range.
- [init(selection:in:displayedComponents:label:)](datepicker/init(selection:in:displayedcomponents:label:).md)
  Creates an instance that selects a `Date` in a closed range.
### Setting date picker components
- [DatePicker.Components](datepicker/components.md)
- [struct DatePickerComponents](datepickercomponents.md)

## Relationships

### Conforms To
- [View](view.md)

## See Also

- [func datePickerStyle<S>(S) -> some View](view/datepickerstyle(_:).md)
  Sets the style for date pickers within this view.
- [struct MultiDatePicker](multidatepicker.md)
  A control for picking multiple dates.
- [var calendar: Calendar](environmentvalues/calendar.md)
  The current calendar that views should use when handling dates.
- [var timeZone: TimeZone](environmentvalues/timezone.md)
  The current time zone that views should use when handling dates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/datepicker)*