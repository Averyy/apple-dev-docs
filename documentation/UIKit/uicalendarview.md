# UICalendarView

**Framework**: UIKit  
**Kind**: class

A view that displays a calendar with date-specific decorations, and provides for user selection of a single date or multiple dates.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UICalendarView
```

#### Overview

Use a calendar view to show users specific dates that have additional information (for example, scheduled events) using decorations that you customize. You can also use a calendar view for users to select one specific date, multiple dates, or no date.

To add a calendar view to your interface:

- Configure the Calendar and Locale for your calendar view to display.
- Set a date for the calendar view to initially make visible.
- Create a delegate to provide decorations on specific dates, if desired.
- Set a selection method and delegate to handle date selection.
- Set up Auto Layout to position the calendar view in your interface.

You use a calendar view only for the display and selection of dates. If you want to handle date and time selection, use [`UIDatePicker`](uidatepicker.md).

##### Configure a Calendar View

Configure your calendar view to display the type of calendar appropriate to the user’s location and cultural preference, in the user’s preferred language. By default, a calendar view selects the user’s current [`Calendar`](https://developer.apple.com/documentation/Foundation/Calendar) and [`Locale`](https://developer.apple.com/documentation/Foundation/Locale). If users can select a different calendar or locale in your app, configure the calendar view to use those selections.

```swift
// Create the calendar view.
let calendarView = UICalendarView()

// Create an instance of the Gregorian calendar.
let gregorianCalendar = Calendar(identifier: .gregorian)

// Set the calendar displayed by the view.
calendarView.calendar = gregorianCalendar

// Set the calendar view's locale.
calendarView.locale = Locale(identifier: "zh_TW")

// Set the font design to the rounded system font.
calendarView.fontDesign = .rounded
```

Then, set the calendar view’s initial display to a starting date that’s appropriate for your use case.

```swift
// Set the date to display.
calendarView.visibleDateComponents = DateComponents(
    calendar: gregorianCalendar,
    year: 2024,
    month: 2,
    day: 1
)
```

If you want to restrict the earliest or latest dates a user can view or select in your calendar view, set the [`availableDateRange`](uicalendarview/availabledaterange.md).

```swift
// Specify the starting date.
let fromDateComponents = DateComponents(
    calendar: gregorianCalendar,
    year: 2024,
    month: 1,
    day: 1
)

// Specify the ending date.
let toDateComponents = DateComponents(
    calendar: gregorianCalendar,
    year: 2024,
    month: 12,
    day: 31
)

// Verify that you have valid start and end dates.
guard let fromDate = fromDateComponents.date, let toDate = toDateComponents.date else {
    // Handle the error here.
    fatalError("Invalid date components: \(fromDateComponents) and \(toDateComponents)")
}

// Set the range of dates that people can view.
let calendarViewDateRange = DateInterval(start: fromDate, end: toDate)
calendarView.availableDateRange = calendarViewDateRange
```

##### Display Decorations for Specific Dates

Use decorations to show users which specific dates have additional information. Add meaning or emphasis to the decorations by setting the color, size, image, or custom view that you display for a specific date. To display decorations in your calendar view, create a custom [`UICalendarViewDelegate`](uicalendarviewdelegate.md) object, implement [`calendarView(_:decorationFor:)`](uicalendarviewdelegate/calendarview(_:decorationfor:).md), and set your custom object as the calendar view’s delegate.

```swift
// Define a calendar view delegate.
class CalendarViewDelegate: NSObject, UICalendarViewDelegate {
    
    var calendarView: UICalendarView? = nil
    var decorations: [Date?: UICalendarView.Decoration]
    
    override init() {
        // Create the date components for Valentine's day that
        // contain the calendar, year, month, and day.
        let valentinesDay = DateComponents(
            calendar: Calendar(identifier: .gregorian),
            year: 2024,
            month: 2,
            day: 14
        )
        
        // Create a calendar decoration for Valentine's day.
        let heart = UICalendarView.Decoration.image(
            UIImage(systemName: "heart.fill"),
            color: UIColor.red,
            size: .large
        )
        
        decorations = [valentinesDay.date: heart]
    }
    
    // Return a decoration (if any) for the specified day.
    func calendarView(_ calendarView: UICalendarView, decorationFor dateComponents: DateComponents) -> UICalendarView.Decoration? {
        // Get a copy of the date components that only contain
        // the calendar, year, month, and day.
        let day = DateComponents(
            calendar: dateComponents.calendar,
            year: dateComponents.year,
            month: dateComponents.month,
            day: dateComponents.day
        )
        
        // Return any decoration saved for that date.
        return decorations[day.date]
    }
}

```

In your implementation, you can decide which type of [`UICalendarView.Decoration`](uicalendarview/decoration.md) best illustrates your user’s events:

- The default decoration, which displays a filled circle you can customize with a color and relative size
- An image decoration, which you can customize with a system symbol or image, color, and relative size
- A custom decoration, which you can customize with a closure that returns your custom view

When your data changes, tell the calendar view to reload decoration views.

```swift
// Add a decoration to the specified date.
func add(decoration: UICalendarView.Decoration, on date: Date) {
    // Get the calendar, year, month, and day date components for
    // the specified date.
    let dateComponents = Calendar.current.dateComponents(
        [.calendar, .year, .month, .day ],
        from: date
    )
    
    // Add the decoration to the decorations dictionary.
    decorations[dateComponents.date] = decoration
    
    // Reload the calendar view's decorations.
    if let calendarView {
        calendarView.reloadDecorations(
            forDateComponents: [dateComponents],
            animated: true
        )
    }
}
```

##### Handle Date Selection

Let users select a single date, multiple dates, or no date with your calendar view. First, decide which type of date selection you want. Then create a selection object and delegate for that type, and assign it to the calendar view’s [`selectionBehavior`](uicalendarview/selectionbehavior.md).

```swift
let dateSelection = UICalendarSelectionSingleDate(delegate: self)
calendarView.selectionBehavior = dateSelection
```

The user can then select a date from the calendar view. You can set a selected date programmatically as the following example shows:

```swift
let date = DateComponents(
    calendar: Calendar(identifier: .gregorian),
    year: 2024,
    month: 2,
    day: 14
)

// Programmatically set the selected date.
dateSelection.selectedDate = date
```

Next, implement the delegate methods for the selection method to customize your date selection handling.

```swift
// Control whether a person can select a given date.
func dateSelection(
    _ selection: UICalendarSelectionSingleDate,
    canSelectDate dateComponents: DateComponents?
) -> Bool {
    // Allow all dates by returning true if the selection parameter contains
    // a date component instance. Prevent someone from clearing the selection
    // by returning false if the selection parameter is nil.
    return dateComponents != nil
}

// Respond when someone selects or deselects a date. If they selected 
// a date, the dateComponent parameter contains the selected date. If they 
// cleared the selection, the parameter is nil.
func dateSelection(_ selection: UICalendarSelectionSingleDate, didSelectDate dateComponents: DateComponents?) {
    // Update your app.
}
```

## Topics

### Setting calendar details
- [var calendar: Calendar](uicalendarview/calendar.md)
  The calendar that the calendar view illustrates.
- [var locale: Locale](uicalendarview/locale.md)
  The locale the calendar view uses for calendar conventions.
- [var timeZone: TimeZone?](uicalendarview/timezone.md)
  The time zone from the date the calendar view displays.
### Setting the visible date and range
- [var visibleDateComponents: DateComponents](uicalendarview/visibledatecomponents.md)
  The date components that represent the visible date in the calendar view.
- [func setVisibleDateComponents(DateComponents, animated: Bool)](uicalendarview/setvisibledatecomponents(_:animated:).md)
  Sets the date components that represent the date for the calendar view to make visible, with an option to animate the date change.
- [var availableDateRange: DateInterval](uicalendarview/availabledaterange.md)
  The range of dates that the calendar view displays.
### Customizing the calendar display
- [var fontDesign: UIFontDescriptor.SystemDesign](uicalendarview/fontdesign.md)
  A font design that the calendar view uses for displaying calendar text.
- [var delegate: (any UICalendarViewDelegate)?](uicalendarview/delegate.md)
  A delegate object the calendar view calls for decoration views.
- [protocol UICalendarViewDelegate](uicalendarviewdelegate.md)
  An object that a calendar view uses to display decorations for dates.
- [UICalendarView.Decoration](uicalendarview/decoration.md)
  A view that a calendar view displays for a specific date.
- [UICalendarView.DecorationSize](uicalendarview/decorationsize.md)
  Constants that indicate the relative size of a decoration in a calendar view.
- [var wantsDateDecorations: Bool](uicalendarview/wantsdatedecorations.md)
  A Boolean value that indicates whether the calendar view displays date decorations.
- [func reloadDecorations(forDateComponents: [DateComponents], animated: Bool)](uicalendarview/reloaddecorations(fordatecomponents:animated:).md)
  Reloads the decorations for the dates you provide, with an option to animate the decoration reload.
### Handling date selections
- [var selectionBehavior: UICalendarSelection?](uicalendarview/selectionbehavior.md)
  The current date selection method of the calendar view.
- [class UICalendarSelectionSingleDate](uicalendarselectionsingledate.md)
  An object that tracks a date the user selects from a calendar view.
- [class UICalendarSelectionMultiDate](uicalendarselectionmultidate.md)
  An object that tracks multiple dates the user selects from a calendar view.
- [class UICalendarSelectionWeekOfYear](uicalendarselectionweekofyear.md)
  An object that tracks a specific week a person selects from a calendar view.
- [class UICalendarSelection](uicalendarselection.md)
  A base object that tracks one or more dates a user selects from a calendar view.

## Relationships

### Inherits From
- [UIView](uiview.md)
### Conforms To
- [CALayerDelegate](../QuartzCore/CALayerDelegate.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [UIAccessibilityIdentification](uiaccessibilityidentification.md)
- [UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md)
- [UIAppearance](uiappearance.md)
- [UIAppearanceContainer](uiappearancecontainer.md)
- [UICoordinateSpace](uicoordinatespace.md)
- [UIDynamicItem](uidynamicitem.md)
- [UIFocusEnvironment](uifocusenvironment.md)
- [UIFocusItem](uifocusitem.md)
- [UIFocusItemContainer](uifocusitemcontainer.md)
- [UILargeContentViewerItem](uilargecontentvieweritem.md)
- [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md)
- [UIPopoverPresentationControllerSourceItem](uipopoverpresentationcontrollersourceitem.md)
- [UIResponderStandardEditActions](uiresponderstandardeditactions.md)
- [UITraitChangeObservable](uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](uitraitenvironment.md)
- [UIUserActivityRestoring](uiuseractivityrestoring.md)

## See Also

- [class UIActivityIndicatorView](uiactivityindicatorview.md)
  A view that shows that a task is in progress.
- [class UIContentUnavailableView](uicontentunavailableview.md)
  A view that indicates there’s no content to display.
- [class UIImageView](uiimageview.md)
  A view that displays a single image or a sequence of animated images in your interface.
- [class UIPickerView](uipickerview.md)
  A view that uses a spinning-wheel or slot-machine metaphor to show one or more sets of values.
- [class UIProgressView](uiprogressview.md)
  A view that depicts the progress of a task over time.
- [class UIWebView](uiwebview.md)
  A view that embeds web content in your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicalendarview)*