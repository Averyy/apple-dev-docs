---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ockcalendarviewsynchronizerprotocol"
framework: "CareKit/CareKit"
---

# OCKCalendarViewSynchronizerProtocol

**Framework**: CareKit/CareKit  
**Kind**: protocol  
**Role**: Protocol

A protocol that describes a view synchronizer for calendars.

## Declaration

```swift
protocol OCKCalendarViewSynchronizerProtocol
```

## Topics

### Associated Types
- [associatedtype View : UIView, OCKCalendarDisplayable](./ockcalendarviewsynchronizerprotocol/view.md)
  The type of the view that will be synchronized
### Instance Methods
- [func makeView() -> View](./ockcalendarviewsynchronizerprotocol/makeview%28%29.md)
  Initialize a view to be synchronized.
- [func updateView(View, context: OCKSynchronizationContext<[OCKCompletionState]>)](./ockcalendarviewsynchronizerprotocol/updateview%28_,context%29.md)
  Update a view using the given context.

## See Also

### Displaying a calendar in UIKit
- [class OCKCalendarViewController](./ockcalendarviewcontroller.md)
  A view controller that displays a calendar view and synchronizes it with a store.
- [class OCKWeekCalendarViewController](./ockweekcalendarviewcontroller.md)
  A view controller that displays a weekly calendar view and synchronizes it with a store.
- [class OCKWeekCalendarViewSynchronizer](./ockweekcalendarviewsynchronizer.md)
  A synchronizer that creates and updates a weekly calendar view.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ockcalendarviewsynchronizerprotocol)*