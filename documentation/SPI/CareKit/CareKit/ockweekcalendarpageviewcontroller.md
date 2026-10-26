---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ockweekcalendarpageviewcontroller"
framework: "CareKit/CareKit"
---

# OCKWeekCalendarPageViewController

**Framework**: CareKit/CareKit  
**Kind**: class  
**Role**: Class

A view controller that allows paging through adjacent weeks of task adherence content.

## Declaration

```swift
@MainActor
class OCKWeekCalendarPageViewController
```

## Topics

### Initializers
- [init(store: OCKAnyStoreProtocol, computeProgress: (OCKAnyEvent) -> CareTaskProgress)](./ockweekcalendarpageviewcontroller/init%28store,computeprogress%29.md)
  A view controller that allows paging through adjacent weeks of task adherence content.
### Instance Properties
- [var calendarDelegate: OCKWeekCalendarPageViewControllerDelegate?](./ockweekcalendarpageviewcontroller/calendardelegate.md)
  An object that handles events related to a weekly calendar page view controller.
- [var dateInterval: DateInterval?](./ockweekcalendarpageviewcontroller/dateinterval.md)
  The date interval currently being displayed.
- [var selectedDate: Date](./ockweekcalendarpageviewcontroller/selecteddate.md)
  The currently selected date in the calendar.
- [let store: OCKAnyStoreProtocol](./ockweekcalendarpageviewcontroller/store.md)
  The store the view controller uses for synchronization.
### Instance Methods
- [func calendarView(UIView & OCKCalendarDisplayable, didSelectDate: Date, at: Int, sender: Any?)](./ockweekcalendarpageviewcontroller/calendarview%28_,didselectdate,at,sender%29.md)
  Called when a particular date in the calendar was selected.
- [func pageViewController(UIPageViewController, didFinishAnimating: Bool, previousViewControllers: [UIViewController], transitionCompleted: Bool)](./ockweekcalendarpageviewcontroller/pageviewcontroller%28_,didfinishanimating,previousviewcontrollers,transitioncompleted%29.md)
- [func pageViewController(UIPageViewController, viewControllerAfter: UIViewController) -> UIViewController?](./ockweekcalendarpageviewcontroller/pageviewcontroller%28_,viewcontrollerafter%29.md)
- [func pageViewController(UIPageViewController, viewControllerBefore: UIViewController) -> UIViewController?](./ockweekcalendarpageviewcontroller/pageviewcontroller%28_,viewcontrollerbefore%29.md)
- [func pageViewController(UIPageViewController, willTransitionTo: [UIViewController])](./ockweekcalendarpageviewcontroller/pageviewcontroller%28_,willtransitionto%29.md)
- [func selectDate(Date, animated: Bool)](./ockweekcalendarpageviewcontroller/selectdate%28_,animated%29.md)
  Select a date in the calendar. If the date is not in the current date interval being displayed, the view controller will automatically page to the date interval that contains the new date.
- [func viewDidLoad()](./ockweekcalendarpageviewcontroller/viewdidload%28%29.md)

## Relationships

### Inherits From
- UIKit.UIPageViewController
### Conforms To
- CareKitUI.OCKCalendarViewDelegate
- Foundation.NSCoding
- Foundation.NSExtensionRequestHandling
- ObjectiveC.NSObjectProtocol
- Swift.CVarArg
- Swift.CustomDebugStringConvertible
- Swift.CustomStringConvertible
- Swift.Equatable
- Swift.Hashable
- Swift.Sendable
- Swift.SendableMetatype
- UIKit.UIActivityItemsConfigurationProviding
- UIKit.UIAppearanceContainer
- UIKit.UIContentContainer
- UIKit.UIFocusEnvironment
- UIKit.UIPageViewControllerDataSource
- UIKit.UIPageViewControllerDelegate
- UIKit.UIPasteConfigurationSupporting
- UIKit.UIResponderStandardEditActions
- UIKit.UIStateRestoring
- UIKit.UITraitChangeObservable
- UIKit.UITraitEnvironment
- UIKit.UIUserActivityRestoring

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
- [protocol OCKWeekCalendarPageViewControllerDelegate](./ockweekcalendarpageviewcontrollerdelegate.md)
  A protocol that handles events related to a weekly calendar page view controller.
- [class OCKListViewController](./ocklistviewcontroller.md)
  A view controller displaying views in a list view.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ockweekcalendarpageviewcontroller)*