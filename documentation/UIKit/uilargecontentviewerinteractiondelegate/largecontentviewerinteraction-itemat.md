# largeContentViewerInteraction(_:itemAt:)

**Framework**: UIKit  
**Kind**: method

Identifies the large content viewer item for the specified interaction and location.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func largeContentViewerInteraction(_ interaction: UILargeContentViewerInteraction, itemAt point: CGPoint) -> (any UILargeContentViewerItem)?
```

#### Discussion

By default, UIKit finds the item for the interaction by calling [`point(inside:with:)`](uiview/point(inside:with:).md) recursively on your view hierarchy. If you’re not using views, implement this method to identify the item for an interaction at a given point.

## Parameters

- `interaction`: The large content viewer interaction that needs an item.
- `point`: The point where the user’s interaction is taking place, in the coordinate space of the view that contains the interaction.

## See Also

- [func largeContentViewerInteraction(UILargeContentViewerInteraction, didEndOn: (any UILargeContentViewerItem)?, at: CGPoint)](uilargecontentviewerinteractiondelegate/largecontentviewerinteraction(_:didendon:at:).md)
  Performs an action when the large content viewer gesture ends at the location of the specified item.
- [func viewController(for: UILargeContentViewerInteraction) -> UIViewController](uilargecontentviewerinteractiondelegate/viewcontroller(for:).md)
  Specifies which view controller should display the large content viewer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilargecontentviewerinteractiondelegate/largecontentviewerinteraction(_:itemat:))*