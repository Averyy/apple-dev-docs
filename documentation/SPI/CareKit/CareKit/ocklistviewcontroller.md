---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ocklistviewcontroller"
framework: "CareKit/CareKit"
---

# OCKListViewController

**Framework**: CareKit/CareKit  
**Kind**: class  
**Role**: Class

A view controller displaying views in a list view.

## Declaration

```swift
@MainActor
class OCKListViewController
```

## Overview

`OCKDailyPageViewController` uses `OCKListViewController` to display scrollable stacks of embedded view controllers.

## Topics

### Instance Methods
- [func appendView(UIView, animated: Bool)](./ocklistviewcontroller/appendview%28_,animated%29.md)
  Appends `view` to the vertical stack of listed views.
- [func appendViewController(UIViewController, animated: Bool)](./ocklistviewcontroller/appendviewcontroller%28_,animated%29.md)
  Sets up the containment of `viewController` in OCKListViewController and appends its view to the vertical stack of listed views.
- [func clear()](./ocklistviewcontroller/clear%28%29.md)
  Removes all displayed views without animation.
- [func insertView(UIView, at: Int, animated: Bool)](./ocklistviewcontroller/insertview%28_,at,animated%29.md)
  Inserts a view in the vertical stack of listed views at the specified index.
- [func insertViewController(UIViewController, at: Int, animated: Bool)](./ocklistviewcontroller/insertviewcontroller%28_,at,animated%29.md)
  Sets up the containment of `viewController` in OCKListViewController and inserts its view in the vertical stack of listed views at the specified index.
- [func loadView()](./ocklistviewcontroller/loadview%28%29.md)
- [func remove(at: Int)](./ocklistviewcontroller/remove%28at%29.md)
  Removes the view located at `index`.

## Relationships

### Inherits From
- UIKit.UIViewController
### Conforms To
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
- [class OCKWeekCalendarPageViewController](./ockweekcalendarpageviewcontroller.md)
  A view controller that allows paging through adjacent weeks of task adherence content.
- [protocol OCKWeekCalendarPageViewControllerDelegate](./ockweekcalendarpageviewcontrollerdelegate.md)
  A protocol that handles events related to a weekly calendar page view controller.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ocklistviewcontroller)*