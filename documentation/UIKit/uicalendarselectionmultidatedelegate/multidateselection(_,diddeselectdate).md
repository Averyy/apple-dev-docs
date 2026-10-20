# multiDateSelection(_:didDeselectDate:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Informs the delegate that a user deselected a date represented by date components.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
func multiDateSelection(_ selection: UICalendarSelectionMultiDate, didDeselectDate dateComponents: DateComponents)
```

```objc
- (void) multiDateSelection:(UICalendarSelectionMultiDate *) selection didDeselectDate:(NSDateComponents *) dateComponents;
```

## Parameters

- `selection`: An object that tracks multiple dates that a user selects from a calendar view.
- `dateComponents`: Date components that represent a date the user deselected.

## See Also

### Changing selected dates
- [func multiDateSelection(UICalendarSelectionMultiDate, didSelectDate: DateComponents)](./multidateselection%28_,didselectdate%29.md)
  Informs the delegate that a user selected a date represented by date components.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicalendarselectionmultidatedelegate/multidateselection(_:diddeselectdate:))*