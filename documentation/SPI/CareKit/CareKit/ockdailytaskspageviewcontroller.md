---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ockdailytaskspageviewcontroller"
framework: "CareKit/CareKit"
---

# OCKDailyTasksPageViewController

**Framework**: CareKit/CareKit  
**Kind**: class  
**Role**: Class

A view controller that displays a calendar page view controller in the header and a collection of tasks in the body.

## Declaration

```swift
@MainActor
class OCKDailyTasksPageViewController
```

## Mentions

- [Creating and displaying tasks for a patient](./creating-and-displaying-tasks-for-a-patient.md)

#### Overview

The selection in the calendar generates an automatic query that populates the tasks.

## Topics

### Instance Properties
- [var tasksDelegate: OCKDailyTasksPageViewControllerDelegate?](./ockdailytaskspageviewcontroller/tasksdelegate.md)
  If set, the delegate will receive callbacks when important events happen at the task view controller level.
### Instance Methods
- [func dailyPageViewController(OCKDailyPageViewController, prepare: OCKListViewController, for: Date)](./ockdailytaskspageviewcontroller/dailypageviewcontroller%28_,prepare,for%29.md)
- [func dailyTasksPageViewController(OCKDailyTasksPageViewController, viewControllerForTask: OCKAnyTask, events: [OCKAnyEvent], eventQuery: OCKEventQuery) -> UIViewController?](./ockdailytaskspageviewcontroller/dailytaskspageviewcontroller%28_,viewcontrollerfortask,events,eventquery%29.md)

## Relationships

### Inherits From
- [OCKDailyPageViewController](./ockdailypageviewcontroller.md)
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
- [protocol OCKWeekCalendarPageViewControllerDelegate](./ockweekcalendarpageviewcontrollerdelegate.md)
  A protocol that handles events related to a weekly calendar page view controller.
- [class OCKListViewController](./ocklistviewcontroller.md)
  A view controller displaying views in a list view.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ockdailytaskspageviewcontroller)*