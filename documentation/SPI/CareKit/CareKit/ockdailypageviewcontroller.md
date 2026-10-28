---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ockdailypageviewcontroller"
framework: "CareKit/CareKit"
---

# OCKDailyPageViewController

**Framework**: CareKit/CareKit  
**Kind**: class  
**Role**: Class

A view controller that displays a calendar page view controller in the header and a view controller in the body.

## Declaration

```swift
@MainActor
class OCKDailyPageViewController
```

## Overview

Manually query these view controllers and set them from outside of the class.

## Topics

### Initializers
- [init(store: OCKAnyStoreProtocol, computeProgress: (OCKAnyEvent) -> CareTaskProgress)](./ockdailypageviewcontroller/init%28store,computeprogress%29.md)
  Create an instance of the view controller. Will hook up the calendar to the tasks collection, and query and display the tasks.
### Instance Properties
- [var currentPage: OCKListViewController?](./ockdailypageviewcontroller/currentpage.md)
  The page that is currently being displayed.
- [var dataSource: OCKDailyPageViewControllerDataSource?](./ockdailypageviewcontroller/datasource.md)
- [var delegate: OCKDailyPageViewControllerDelegate?](./ockdailypageviewcontroller/delegate.md)
- [var selectedDate: Date](./ockdailypageviewcontroller/selecteddate.md)
- [let store: OCKAnyStoreProtocol](./ockdailypageviewcontroller/store.md)
  The store the view controller uses for synchronization.
### Instance Methods
- [func dailyPageViewController(OCKDailyPageViewController, didFailWithError: Error)](./ockdailypageviewcontroller/dailypageviewcontroller%28_,didfailwitherror%29.md)
- [func dailyPageViewController(OCKDailyPageViewController, prepare: OCKListViewController, for: Date)](./ockdailypageviewcontroller/dailypageviewcontroller%28_,prepare,for%29.md)
- [func loadView()](./ockdailypageviewcontroller/loadview%28%29.md)
- [func pageViewController(UIPageViewController, didFinishAnimating: Bool, previousViewControllers: [UIViewController], transitionCompleted: Bool)](./ockdailypageviewcontroller/pageviewcontroller%28_,didfinishanimating,previousviewcontrollers,transitioncompleted%29.md)
- [func pageViewController(UIPageViewController, viewControllerAfter: UIViewController) -> UIViewController?](./ockdailypageviewcontroller/pageviewcontroller%28_,viewcontrollerafter%29.md)
- [func pageViewController(UIPageViewController, viewControllerBefore: UIViewController) -> UIViewController?](./ockdailypageviewcontroller/pageviewcontroller%28_,viewcontrollerbefore%29.md)
- [func reload()](./ockdailypageviewcontroller/reload%28%29.md)
  Reload the contents at the currently selected date.
- [func selectDate(Date, animated: Bool)](./ockdailypageviewcontroller/selectdate%28_,animated%29.md)
  Selects the given date, updating both the calendar view and the daily content.
- [func viewDidLoad()](./ockdailypageviewcontroller/viewdidload%28%29.md)
- [func viewSafeAreaInsetsDidChange()](./ockdailypageviewcontroller/viewsafeareainsetsdidchange%28%29.md)
- [func weekCalendarPageViewController(OCKWeekCalendarPageViewController, didChangeDateInterval: DateInterval)](./ockdailypageviewcontroller/weekcalendarpageviewcontroller%28_,didchangedateinterval%29.md)
- [func weekCalendarPageViewController(OCKWeekCalendarPageViewController, didEncounterError: Error)](./ockdailypageviewcontroller/weekcalendarpageviewcontroller%28_,didencountererror%29.md)
- [func weekCalendarPageViewController(OCKWeekCalendarPageViewController, didSelectDate: Date, previousDate: Date)](./ockdailypageviewcontroller/weekcalendarpageviewcontroller%28_,didselectdate,previousdate%29.md)

## Relationships

### Inherits From
- UIKit.UIViewController
### Inherited By
- [OCKDailyTasksPageViewController](./ockdailytaskspageviewcontroller.md)
### Conforms To
- Foundation.NSCoding
- Foundation.NSExtensionRequestHandling
- [OCKDailyPageViewControllerDataSource](./ockdailypageviewcontrollerdatasource.md)
- [OCKDailyPageViewControllerDelegate](./ockdailypageviewcontrollerdelegate.md)
- [OCKWeekCalendarPageViewControllerDelegate](./ockweekcalendarpageviewcontrollerdelegate.md)
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
- [protocol OCKDailyPageViewControllerDataSource](./ockdailypageviewcontrollerdatasource.md)
  A protocol for classes that provides content to a page view controller.
- [protocol OCKDailyPageViewControllerDelegate](./ockdailypageviewcontrollerdelegate.md)
  A protocol that provides callbacks when important events occur in a page view controller.
- [class OCKWeekCalendarPageViewController](./ockweekcalendarpageviewcontroller.md)
  A view controller that allows paging through adjacent weeks of task adherence content.
- [protocol OCKWeekCalendarPageViewControllerDelegate](./ockweekcalendarpageviewcontrollerdelegate.md)
  A protocol that handles events related to a weekly calendar page view controller.
- [class OCKListViewController](./ocklistviewcontroller.md)
  A view controller displaying views in a list view.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ockdailypageviewcontroller)*