# viewController(for:)

**Framework**: UIKit  
**Kind**: method

Specifies which view controller should display the large content viewer.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func viewController(for interaction: UILargeContentViewerInteraction) -> UIViewController
```

#### Return Value

A view controller that the system uses to present the large content viewer in.

#### Discussion

By default, UIKit uses a view controller that contains the view you added the interaction to. If this default choice doesn’t work for your app, implement this method to specify a different view controller.

## Parameters

- `interaction`: The large content viewer that the system is displaying.

## See Also

- [func largeContentViewerInteraction(UILargeContentViewerInteraction, didEndOn: (any UILargeContentViewerItem)?, at: CGPoint)](uilargecontentviewerinteractiondelegate/largecontentviewerinteraction(_:didendon:at:).md)
  Performs an action when the large content viewer gesture ends at the location of the specified item.
- [func largeContentViewerInteraction(UILargeContentViewerInteraction, itemAt: CGPoint) -> (any UILargeContentViewerItem)?](uilargecontentviewerinteractiondelegate/largecontentviewerinteraction(_:itemat:).md)
  Identifies the large content viewer item for the specified interaction and location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilargecontentviewerinteractiondelegate/viewcontroller(for:))*