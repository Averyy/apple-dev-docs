---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ockweekcalendarviewcontroller"
framework: "CareKit/CareKit"
---

# OCKWeekCalendarViewController

**Framework**: CareKit/CareKit  
**Kind**: class  
**Role**: Class

A view controller that displays a weekly calendar view and synchronizes it with a store.

## Declaration

```swift
@MainActor
class OCKWeekCalendarViewController
```

## Topics

### Initializers
- [init(store: OCKAnyStoreProtocol, viewSynchronizer: OCKWeekCalendarViewSynchronizer, computeProgress: (OCKAnyEvent) -> CareTaskProgress)](./ockweekcalendarviewcontroller/init%28store,viewsynchronizer,computeprogress%29.md)
  Initialize a view controller that displays adherence. Fetches and stays synchronized with the adherence data.
- [init(weekOfDate: Date, store: OCKAnyStoreProtocol, computeProgress: (OCKAnyEvent) -> CareTaskProgress)](./ockweekcalendarviewcontroller/init%28weekofdate,store,computeprogress%29.md)
  Initialize a view controller that displays adherence. Fetches and stays synchronized with the adherence data.

## Relationships

### Inherits From
- [OCKCalendarViewController](./ockcalendarviewcontroller.md)
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
- [class OCKCalendarViewController](./ockcalendarviewcontroller.md)
  A view controller that displays a calendar view and synchronizes it with a store.
- [class OCKWeekCalendarViewSynchronizer](./ockweekcalendarviewsynchronizer.md)
  A synchronizer that creates and updates a weekly calendar view.
- [protocol OCKCalendarViewSynchronizerProtocol](./ockcalendarviewsynchronizerprotocol.md)
  A protocol that describes a view synchronizer for calendars.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ockweekcalendarviewcontroller)*