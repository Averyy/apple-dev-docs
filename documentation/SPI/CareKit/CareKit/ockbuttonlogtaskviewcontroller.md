---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ockbuttonlogtaskviewcontroller"
framework: "CareKit/CareKit"
---

# OCKButtonLogTaskViewController

**Framework**: CareKit/CareKit  
**Kind**: class  
**Role**: Class

A view controller that shows detailed descriptions for complete or incomplete events, organized in a grid.

## Declaration

```swift
@MainActor
class OCKButtonLogTaskViewController
```

## Topics

### Initializers
- [init(query: OCKEventQuery, store: OCKAnyStoreProtocol, viewSynchronizer: OCKButtonLogTaskViewSynchronizer)](./ockbuttonlogtaskviewcontroller/init%28query,store,viewsynchronizer%29.md)
  Creates a controller that displays a task view and keeps it synchronized with a store.

## Relationships

### Inherits From
- [OCKTaskViewController](./ocktaskviewcontroller.md)
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

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ockbuttonlogtaskviewcontroller)*