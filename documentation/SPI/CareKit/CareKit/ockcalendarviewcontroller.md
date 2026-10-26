---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ockcalendarviewcontroller"
framework: "CareKit/CareKit"
---

# OCKCalendarViewController

**Framework**: CareKit/CareKit  
**Kind**: class  
**Role**: Class

A view controller that displays a calendar view and synchronizes it with a store.

## Declaration

```swift
@MainActor
class OCKCalendarViewController<ViewSynchronizer> where ViewSynchronizer : ViewSynchronizing, ViewSynchronizer.View : OCKCalendarDisplayable, ViewSynchronizer.ViewModel == [OCKCompletionState]
```

## Topics

### Initializers
- [init(dateInterval: DateInterval, store: OCKAnyStoreProtocol, viewSynchronizer: ViewSynchronizer, computeProgress: (OCKAnyEvent) -> CareTaskProgress)](./ockcalendarviewcontroller/init%28dateinterval,store,viewsynchronizer,computeprogress%29.md)
  Initialize a view controller that displays adherence per date. Fetches and stays synchronized with the adherence data.
### Instance Properties
- [var calendarView: ViewSynchronizer.View](./ockcalendarviewcontroller/calendarview.md)
  The view that is being synchronized against the store.
### Instance Methods
- [func calendarView(UIView & OCKCalendarDisplayable, didSelectDate: Date, at: Int, sender: Any?)](./ockcalendarviewcontroller/calendarview%28_,didselectdate,at,sender%29.md)

## Relationships

### Inherits From
- [SynchronizedViewController](./synchronizedviewcontroller.md)
### Inherited By
- [OCKWeekCalendarViewController](./ockweekcalendarviewcontroller.md)
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
- UIKit.UIPasteConfigurationSupporting
- UIKit.UIResponderStandardEditActions
- UIKit.UIStateRestoring
- UIKit.UITraitChangeObservable
- UIKit.UITraitEnvironment
- UIKit.UIUserActivityRestoring

## See Also

### Displaying a calendar in UIKit
- [class OCKWeekCalendarViewController](./ockweekcalendarviewcontroller.md)
  A view controller that displays a weekly calendar view and synchronizes it with a store.
- [class OCKWeekCalendarViewSynchronizer](./ockweekcalendarviewsynchronizer.md)
  A synchronizer that creates and updates a weekly calendar view.
- [protocol OCKCalendarViewSynchronizerProtocol](./ockcalendarviewsynchronizerprotocol.md)
  A protocol that describes a view synchronizer for calendars.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ockcalendarviewcontroller)*