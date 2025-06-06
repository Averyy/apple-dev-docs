# UILargeContentViewerInteractionDelegate

**Framework**: UIKit  
**Kind**: protocol

An object that customizes the behavior of the large content viewer interactions.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
protocol UILargeContentViewerInteractionDelegate : NSObjectProtocol
```

## Topics

### Customizing large content viewer interactions
- [func largeContentViewerInteraction(UILargeContentViewerInteraction, didEndOn: (any UILargeContentViewerItem)?, at: CGPoint)](uilargecontentviewerinteractiondelegate/largecontentviewerinteraction(_:didendon:at:).md)
  Performs an action when the large content viewer gesture ends at the location of the specified item.
- [func largeContentViewerInteraction(UILargeContentViewerInteraction, itemAt: CGPoint) -> (any UILargeContentViewerItem)?](uilargecontentviewerinteractiondelegate/largecontentviewerinteraction(_:itemat:).md)
  Identifies the large content viewer item for the specified interaction and location.
- [func viewController(for: UILargeContentViewerInteraction) -> UIViewController](uilargecontentviewerinteractiondelegate/viewcontroller(for:).md)
  Specifies which view controller should display the large content viewer.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class UILargeContentViewerInteraction](uilargecontentviewerinteraction.md)
  An interaction that enables a gesture to present the large content viewer for cases when supporting the largest dynamic type sizes isn’t appropriate.
- [protocol UILargeContentViewerItem](uilargecontentvieweritem.md)
  Methods that provide details about how to display your custom content in the large content viewer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilargecontentviewerinteractiondelegate)*