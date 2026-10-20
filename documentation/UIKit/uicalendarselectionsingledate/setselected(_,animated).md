# setSelected(_:animated:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Updates the date component object that represents a selected date in a calendar view, with an option to animate the change.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
func setSelected(_ selectedDate: DateComponents?, animated: Bool)
```

```objc
- (void) setSelectedDate:(NSDateComponents *) selectedDate animated:(BOOL) animated;
```

## Parameters

- `selectedDate`: A date component object that represents a date to select in a calendar view.
- `animated`: A Boolean value that indicates whether the calendar view should animate changing the selected date.

## See Also

### Updating the selected date
- [var selectedDate: DateComponents?](./selecteddate.md)
  A date component object that represents a selected date in a calendar view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicalendarselectionsingledate/setselected(_:animated:))*