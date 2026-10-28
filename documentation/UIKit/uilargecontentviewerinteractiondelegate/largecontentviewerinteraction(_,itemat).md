# largeContentViewerInteraction(_:itemAt:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Identifies the large content viewer item for the specified interaction and location.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func largeContentViewerInteraction(_ interaction: UILargeContentViewerInteraction, itemAt point: CGPoint) -> (any UILargeContentViewerItem)?
```

```objc
- (id<UILargeContentViewerItem>) largeContentViewerInteraction:(UILargeContentViewerInteraction *) interaction itemAtPoint:(CGPoint) point;
```

## Discussion

By default, UIKit finds the item for the interaction by calling [`point(inside:with:)`](../uiview/point%28inside,with%29.md) recursively on your view hierarchy. If you’re not using views, implement this method to identify the item for an interaction at a given point.

## Parameters

- `interaction`: The large content viewer interaction that needs an item.
- `point`: The point where the user’s interaction is taking place, in the coordinate space of the view that contains the interaction.

## See Also

### Customizing large content viewer interactions
- [func largeContentViewerInteraction(UILargeContentViewerInteraction, didEndOn: (any UILargeContentViewerItem)?, at: CGPoint)](./largecontentviewerinteraction%28_,didendon,at%29.md)
  Performs an action when the large content viewer gesture ends at the location of the specified item.
- [func viewController(for: UILargeContentViewerInteraction) -> UIViewController](./viewcontroller%28for%29.md)
  Specifies which view controller should display the large content viewer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilargecontentviewerinteractiondelegate/largecontentviewerinteraction(_:itemat:))*