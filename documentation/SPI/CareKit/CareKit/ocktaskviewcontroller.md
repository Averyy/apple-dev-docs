---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ocktaskviewcontroller"
framework: "CareKit/CareKit"
---

# OCKTaskViewController

**Framework**: CareKit/CareKit  
**Kind**: class  
**Role**: Class

A view controller that displays a task view and keeps it synchronized with a store.

## Declaration

```swift
@MainActor
class OCKTaskViewController<ViewSynchronizer> where ViewSynchronizer : ViewSynchronizing, ViewSynchronizer.View : OCKTaskDisplayable, ViewSynchronizer.ViewModel == OCKTaskEvents
```

## Topics

### Initializers
- [init(query: OCKEventQuery, store: OCKAnyStoreProtocol, viewSynchronizer: ViewSynchronizer, modifyTaskEvents: (OCKTaskEvents) -> OCKTaskEvents)](./ocktaskviewcontroller/init%28query,store,viewsynchronizer,modifytaskevents%29.md)
  Creates a view controller that displays a task view and keeps it synchronized with a store.
### Instance Properties
- [var taskView: ViewSynchronizer.View](./ocktaskviewcontroller/taskview.md)
  The view that is being synchronized against the store.
### Instance Methods
- [func didSelectTaskView(UIView & OCKTaskDisplayable, eventIndexPath: IndexPath)](./ocktaskviewcontroller/didselecttaskview%28_,eventindexpath%29.md)
- [func taskView(UIView & OCKTaskDisplayable, didCompleteEvent: Bool, at: IndexPath, sender: Any?)](./ocktaskviewcontroller/taskview%28_,didcompleteevent,at,sender%29.md)
- [func taskView(UIView & OCKTaskDisplayable, didCreateOutcomeValueAt: Int, eventIndexPath: IndexPath, sender: Any?)](./ocktaskviewcontroller/taskview%28_,didcreateoutcomevalueat,eventindexpath,sender%29.md)
- [func taskView(UIView & OCKTaskDisplayable, didSelectOutcomeValueAt: Int, eventIndexPath: IndexPath, sender: Any?)](./ocktaskviewcontroller/taskview%28_,didselectoutcomevalueat,eventindexpath,sender%29.md)
- [func viewDidLoad()](./ocktaskviewcontroller/viewdidload%28%29.md)

## Relationships

### Inherits From
- [SynchronizedViewController](./synchronizedviewcontroller.md)
### Inherited By
- [OCKButtonLogTaskViewController](./ockbuttonlogtaskviewcontroller.md)
- [OCKChecklistTaskViewController](./ockchecklisttaskviewcontroller.md)
- [OCKGridTaskViewController](./ockgridtaskviewcontroller.md)
- [OCKInstructionsTaskViewController](./ockinstructionstaskviewcontroller.md)
- [OCKSimpleTaskViewController](./ocksimpletaskviewcontroller.md)
### Conforms To
- CareKitUI.OCKTaskViewDelegate
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

### Displaying care tasks in UIKit
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
- [class OCKGridTaskViewSynchronizer](./ockgridtaskviewsynchronizer.md)
  A synchronizer that creates and updates a grid task view.
- [class OCKButtonLogTaskViewSynchronizer](./ockbuttonlogtaskviewsynchronizer.md)
  A synchronizer that creates and updates a button log task view.
- [protocol OCKTaskViewSynchronizerProtocol](./ocktaskviewsynchronizerprotocol.md)
  A protocol that describes a view synchronizer for tasks.
- [protocol OCKAnyTaskViewSynchronizerProtocol](./ockanytaskviewsynchronizerprotocol.md)
  A protocol that describes a type-erased view synchronizer for tasks.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ocktaskviewcontroller)*