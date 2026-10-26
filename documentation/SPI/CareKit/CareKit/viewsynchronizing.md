---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/viewsynchronizing"
framework: "CareKit/CareKit"
---

# ViewSynchronizing

**Framework**: CareKit/CareKit  
**Kind**: protocol  
**Role**: Protocol

A protocol that creates and updates a view.

## Declaration

```swift
protocol ViewSynchronizing
```

## Topics

### Associated Types
- [associatedtype View : UIView](./viewsynchronizing/view.md)
  The view that the controller creates and updates.
- [associatedtype ViewModel](./viewsynchronizing/viewmodel.md)
  The data displayed in the view.
### Instance Methods
- [func makeView() -> View](./viewsynchronizing/makeview%28%29.md)
  Create the view.
- [func updateView(View, context: OCKSynchronizationContext<ViewModel>)](./viewsynchronizing/updateview%28_,context%29.md)
  Update the view using the current `context`. .

## Relationships

### Conforming Types
- [OCKButtonLogTaskViewSynchronizer](./ockbuttonlogtaskviewsynchronizer.md)
- [OCKCartesianChartViewSynchronizer](./ockcartesianchartviewsynchronizer.md)
- [OCKChecklistTaskViewSynchronizer](./ockchecklisttaskviewsynchronizer.md)
- [OCKDetailedContactViewSynchronizer](./ockdetailedcontactviewsynchronizer.md)
- [OCKGridTaskViewSynchronizer](./ockgridtaskviewsynchronizer.md)
- [OCKInstructionsTaskViewSynchronizer](./ockinstructionstaskviewsynchronizer.md)
- [OCKSimpleContactViewSynchronizer](./ocksimplecontactviewsynchronizer.md)
- [OCKSimpleTaskViewSynchronizer](./ocksimpletaskviewsynchronizer.md)
- [OCKWeekCalendarViewSynchronizer](./ockweekcalendarviewsynchronizer.md)

## See Also

### Displaying synchronized care data in UIKit
- [class SynchronizedViewController](./synchronizedviewcontroller.md)
  A view controller that updates a view using a stream of data.
- [struct OCKSynchronizationContext](./ocksynchronizationcontext.md)
  A data structure that provides context for a view model value.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/viewsynchronizing)*