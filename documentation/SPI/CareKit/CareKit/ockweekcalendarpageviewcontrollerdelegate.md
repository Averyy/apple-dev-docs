---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ockweekcalendarpageviewcontrollerdelegate"
framework: "CareKit/CareKit"
---

# OCKWeekCalendarPageViewControllerDelegate

**Framework**: CareKit/CareKit  
**Kind**: protocol  
**Role**: Protocol

A protocol that handles events related to a weekly calendar page view controller.

## Declaration

```swift
protocol OCKWeekCalendarPageViewControllerDelegate : AnyObject
```

## Topics

### Instance Methods
- [func weekCalendarPageViewController(OCKWeekCalendarPageViewController, didChangeDateInterval: DateInterval)](./ockweekcalendarpageviewcontrollerdelegate/weekcalendarpageviewcontroller%28_,didchangedateinterval%29.md)
  Called when the date interval in the calendar has been changed.
- [func weekCalendarPageViewController(OCKWeekCalendarPageViewController, didSelectDate: Date, previousDate: Date)](./ockweekcalendarpageviewcontrollerdelegate/weekcalendarpageviewcontroller%28_,didselectdate,previousdate%29.md)
  Called when a person selects a date in the calendar.

## Relationships

### Conforming Types
- [OCKDailyPageViewController](./ockdailypageviewcontroller.md)
- [OCKDailyTasksPageViewController](./ockdailytaskspageviewcontroller.md)

## See Also

### Displaying care data over time in UIKit
- [class OCKDailyTasksPageViewController](./ockdailytaskspageviewcontroller.md)
  A view controller that displays a calendar page view controller in the header and a collection of tasks in the body.
- [protocol OCKDailyTasksPageViewControllerDelegate](./ockdailytaskspageviewcontrollerdelegate.md)
  A protocol that handles events related to a daily tasks page view controller.
- [class OCKDailyPageViewController](./ockdailypageviewcontroller.md)
  A view controller that displays a calendar page view controller in the header and a view controller in the body.
- [protocol OCKDailyPageViewControllerDataSource](./ockdailypageviewcontrollerdatasource.md)
  A protocol for classes that provides content to a page view controller.
- [protocol OCKDailyPageViewControllerDelegate](./ockdailypageviewcontrollerdelegate.md)
  A protocol that provides callbacks when important events occur in a page view controller.
- [class OCKWeekCalendarPageViewController](./ockweekcalendarpageviewcontroller.md)
  A view controller that allows paging through adjacent weeks of task adherence content.
- [class OCKListViewController](./ocklistviewcontroller.md)
  A view controller displaying views in a list view.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ockweekcalendarpageviewcontrollerdelegate)*