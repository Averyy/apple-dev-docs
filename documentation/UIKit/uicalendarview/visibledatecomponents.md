# visibleDateComponents

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The date components that represent the visible date in the calendar view.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
var visibleDateComponents: DateComponents { get set }
```

```objc
@property (nonatomic, copy, nonnull) NSDateComponents * visibleDateComponents;
```

#### Discussion

If `visibleDateComponents.calendar` is `nil` or isn’t equal to [`calendar`](./calendar.md), the calendar view uses [`calendar`](./calendar.md), which may result in an invalid date from the date components.

## See Also

### Setting the visible date and range
- [func setVisibleDateComponents(DateComponents, animated: Bool)](./setvisibledatecomponents%28_,animated%29.md)
  Sets the date components that represent the date for the calendar view to make visible, with an option to animate the date change.
- [var availableDateRange: DateInterval](./availabledaterange.md)
  The range of dates that the calendar view displays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicalendarview/visibledatecomponents)*