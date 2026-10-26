---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ockcompletionringview"
framework: "CareKit/CareKitUI"
---

# OCKCompletionRingView

**Framework**: CareKit/CareKitUI  
**Kind**: class  
**Role**: Class

A fillable ring with an inner checkmark.

## Declaration

```swift
@MainActor
class OCKCompletionRingView
```

## Topics

### Instance Properties
- [var duration: TimeInterval](./ockcompletionringview/duration.md)
  The duration for the ring and check view animations.
- [var intrinsicContentSize: CGSize](./ockcompletionringview/intrinsiccontentsize.md)
- [var lineWidth: CGFloat](./ockcompletionringview/linewidth.md)
  The line width of the ring and check views.
- [var progress: CGFloat](./ockcompletionringview/progress.md)
  The progress value of the ring view.
- [var strokeColor: UIColor](./ockcompletionringview/strokecolor.md)
  The stroke color of the ring and check views.
### Instance Methods
- [func setProgress(CGFloat, animated: Bool)](./ockcompletionringview/setprogress%28_,animated%29.md)
  Set the progress value for the ring view. The ring will fill accordingly, and if full the checkmark will display.
- [func styleDidChange()](./ockcompletionringview/styledidchange%28%29.md)

## Relationships

### Inherits From
- [OCKView](./ockview.md)
### Conforms To
- Foundation.NSCoding
- [OCKStylable](./ockstylable.md)
- ObjectiveC.NSObjectProtocol
- QuartzCore.CALayerDelegate
- Swift.CVarArg
- Swift.CustomDebugStringConvertible
- Swift.CustomStringConvertible
- Swift.Equatable
- Swift.Hashable
- Swift.Sendable
- Swift.SendableMetatype
- UIKit.UIAccessibilityIdentification
- UIKit.UIActivityItemsConfigurationProviding
- UIKit.UIAppearance
- UIKit.UIAppearanceContainer
- UIKit.UIDynamicItem
- UIKit.UIFocusEnvironment
- UIKit.UIFocusItem
- UIKit.UIFocusItemContainer
- UIKit.UILargeContentViewerItem
- UIKit.UIPasteConfigurationSupporting
- UIKit.UIPopoverPresentationControllerSourceItem
- UIKit.UIResponderStandardEditActions
- UIKit.UITraitChangeObservable
- UIKit.UITraitEnvironment
- UIKit.UIUserActivityRestoring
- UIUtilities.UICoordinateSpace

## See Also

### Calendar
- [class OCKWeekCalendarView](./ockweekcalendarview.md)
  A horizontal row of seven selectable completion rings and corresponding labels.
- [class OCKCompletionRingButton](./ockcompletionringbutton.md)
  A selectable completion ring with an inner check view and a title label.
- [enum OCKCompletionState](./ockcompletionstate.md)
  A completion state that marks progress.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ockcompletionringview)*