---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ockgridtaskviewsynchronizer"
framework: "CareKit/CareKit"
---

# OCKGridTaskViewSynchronizer

**Framework**: CareKit/CareKit  
**Kind**: class  
**Role**: Class

A synchronizer that creates and updates a grid task view.

## Declaration

```swift
class OCKGridTaskViewSynchronizer
```

## Topics

### Initializers
- [init()](./ockgridtaskviewsynchronizer/init%28%29.md)
### Instance Methods
- [func makeView() -> OCKGridTaskView](./ockgridtaskviewsynchronizer/makeview%28%29.md)
- [func updateView(OCKGridTaskView, context: OCKSynchronizationContext<OCKTaskEvents>)](./ockgridtaskviewsynchronizer/updateview%28_,context%29.md)

## Relationships

### Conforms To
- [ViewSynchronizing](./viewsynchronizing.md)

## See Also

### Displaying care tasks in UIKit
- [class OCKTaskViewController](./ocktaskviewcontroller.md)
  A view controller that displays a task view and keeps it synchronized with a store.
- [class OCKSimpleTaskViewController](./ocksimpletaskviewcontroller.md)
  A view controller that display and updates a single event that can be completed or uncompleted by tapping a large button.
- [class OCKInstructionsTaskViewController](./ockinstructionstaskviewcontroller.md)
  A view controller that shows a detailed description for a single complete or incomplete event.
- [class OCKChecklistTaskViewController](./ockchecklisttaskviewcontroller.md)
  A view controller that shows detailed descriptions for complete or incomplete events, organized in a checklist.
- [class OCKGridTaskViewController](./ockgridtaskviewcontroller.md)
  A task view controller that displays multiple events in a grid collection view.
- [class OCKButtonLogTaskViewController](./ockbuttonlogtaskviewcontroller.md)
  A view controller that shows detailed descriptions for complete or incomplete events, organized in a grid.
- [struct OCKTaskEvents](./ocktaskevents.md)
  A data structure that holds events for multiple tasks.
- [class OCKSimpleTaskViewSynchronizer](./ocksimpletaskviewsynchronizer.md)
  A synchronizer for the simple task view.
- [class OCKInstructionsTaskViewSynchronizer](./ockinstructionstaskviewsynchronizer.md)
  A synchronizer for the instructions task view.
- [class OCKChecklistTaskViewSynchronizer](./ockchecklisttaskviewsynchronizer.md)
  A synchronizer for the checklist task view.
- [class OCKButtonLogTaskViewSynchronizer](./ockbuttonlogtaskviewsynchronizer.md)
  A synchronizer that creates and updates a button log task view.
- [protocol OCKTaskViewSynchronizerProtocol](./ocktaskviewsynchronizerprotocol.md)
  A protocol that describes a view synchronizer for tasks.
- [protocol OCKAnyTaskViewSynchronizerProtocol](./ockanytaskviewsynchronizerprotocol.md)
  A protocol that describes a type-erased view synchronizer for tasks.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ockgridtaskviewsynchronizer)*