# multiDateSelection(_:didSelectDate:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Informs the delegate that a user selected a date represented by date components.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
func multiDateSelection(_ selection: UICalendarSelectionMultiDate, didSelectDate dateComponents: DateComponents)
```

```objc
- (void) multiDateSelection:(UICalendarSelectionMultiDate *) selection didSelectDate:(NSDateComponents *) dateComponents;
```

## Parameters

- `selection`: An object that tracks one or more dates that a user selects from a calendar view.
- `dateComponents`: Date components that represent a date the user selected.

## See Also

### Changing selected dates
- [func multiDateSelection(UICalendarSelectionMultiDate, didDeselectDate: DateComponents)](./multidateselection%28_,diddeselectdate%29.md)
  Informs the delegate that a user deselected a date represented by date components.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicalendarselectionmultidatedelegate/multidateselection(_:didselectdate:))*