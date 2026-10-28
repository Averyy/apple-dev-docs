# UICalendarSelection

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

A base object that tracks one or more dates a user selects from a calendar view.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UICalendarSelection
```

```objc
@interface UICalendarSelection : NSObject
```

## Overview

Don’t use this object directly in your calendar view to track date selection. Use the subclass [`UICalendarSelectionSingleDate`](./uicalendarselectionsingledate.md) to track a single date selection, or [`UICalendarSelectionMultiDate`](./uicalendarselectionmultidate.md) to track multiple date selections.

## Topics

### Updating selectable dates
- [func updateSelectableDates()](./uicalendarselection/updateselectabledates%28%29.md)
  Informs the calendar view to update the view for selectable dates.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [UICalendarSelectionMultiDate](./uicalendarselectionmultidate.md)
- [UICalendarSelectionSingleDate](./uicalendarselectionsingledate.md)
- [UICalendarSelectionWeekOfYear](./uicalendarselectionweekofyear.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Handling date selections
- [var selectionBehavior: UICalendarSelection?](./uicalendarview/selectionbehavior.md)
  The current date selection method of the calendar view.
- [class UICalendarSelectionSingleDate](./uicalendarselectionsingledate.md)
  An object that tracks a date the user selects from a calendar view.
- [class UICalendarSelectionMultiDate](./uicalendarselectionmultidate.md)
  An object that tracks multiple dates the user selects from a calendar view.
- [class UICalendarSelectionWeekOfYear](./uicalendarselectionweekofyear.md)
  An object that tracks a specific week a person selects from a calendar view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicalendarselection)*