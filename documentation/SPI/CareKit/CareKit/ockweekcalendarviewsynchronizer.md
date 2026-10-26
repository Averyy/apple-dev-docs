---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ockweekcalendarviewsynchronizer"
framework: "CareKit/CareKit"
---

# OCKWeekCalendarViewSynchronizer

**Framework**: CareKit/CareKit  
**Kind**: class  
**Role**: Class

A synchronizer that creates and updates a weekly calendar view.

## Declaration

```swift
class OCKWeekCalendarViewSynchronizer
```

## Topics

### Initializers
- [init(weekOfDate: Date)](./ockweekcalendarviewsynchronizer/init%28weekofdate%29.md)
  Initialize by specifying a date. The calendar will show the entire week that the provided date falls within.
### Instance Methods
- [func makeView() -> OCKWeekCalendarView](./ockweekcalendarviewsynchronizer/makeview%28%29.md)
- [func updateView(OCKWeekCalendarView, context: OCKSynchronizationContext<[OCKCompletionState]>)](./ockweekcalendarviewsynchronizer/updateview%28_,context%29.md)

## Relationships

### Conforms To
- [ViewSynchronizing](./viewsynchronizing.md)

## See Also

### Displaying a calendar in UIKit
- [class OCKCalendarViewController](./ockcalendarviewcontroller.md)
  A view controller that displays a calendar view and synchronizes it with a store.
- [class OCKWeekCalendarViewController](./ockweekcalendarviewcontroller.md)
  A view controller that displays a weekly calendar view and synchronizes it with a store.
- [protocol OCKCalendarViewSynchronizerProtocol](./ockcalendarviewsynchronizerprotocol.md)
  A protocol that describes a view synchronizer for calendars.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ockweekcalendarviewsynchronizer)*