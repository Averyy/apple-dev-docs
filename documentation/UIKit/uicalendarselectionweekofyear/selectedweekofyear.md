# selectedWeekOfYear

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The current week-of-year selection in the calendar view.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
var selectedWeekOfYear: DateComponents? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSDateComponents * selectedWeekOfYear;
```

## Discussion

The components need to include `[.yearForWeekOfYear, .weekOfYear]`.

## See Also

### Updating the selected week
- [func setSelected(DateComponents?, animated: Bool)](./setselected%28_,animated%29.md)
  Updates the date component object that represents a selected week in a calendar view, with an option to animate the change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicalendarselectionweekofyear/selectedweekofyear)*