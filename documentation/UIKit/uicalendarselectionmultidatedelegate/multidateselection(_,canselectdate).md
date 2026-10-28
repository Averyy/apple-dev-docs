# multiDateSelection(_:canSelectDate:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns whether a user can select a date represented by date components in the calendar view.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
optional func multiDateSelection(_ selection: UICalendarSelectionMultiDate, canSelectDate dateComponents: DateComponents) -> Bool
```

```objc
- (BOOL) multiDateSelection:(UICalendarSelectionMultiDate *) selection canSelectDate:(NSDateComponents *) dateComponents;
```

## Return Value

A Boolean value that indicates whether the calendar view can select the date you provide.

## Discussion

The calendar view displays non-selectable dates as disabled.

## Parameters

- `selection`: An object that tracks multiple dates that a user selects from a calendar view.
- `dateComponents`: Date components that represent a date to select.

## See Also

### Getting selectable dates
- [func multiDateSelection(UICalendarSelectionMultiDate, canDeselectDate: DateComponents) -> Bool](./multidateselection%28_,candeselectdate%29.md)
  Returns whether a user can deselect a date represented by date components in the calendar view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicalendarselectionmultidatedelegate/multidateselection(_:canselectdate:))*