# largeContentViewerInteraction(_:didEndOn:at:)

**Framework**: UIKit  
**Kind**: method

Performs an action when the large content viewer gesture ends at the location of the specified item.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func largeContentViewerInteraction(_ interaction: UILargeContentViewerInteraction, didEndOn item: (any UILargeContentViewerItem)?, at point: CGPoint)
```

#### Discussion

If you don’t implement this method and are using standard UIKit controls, the system performs a default action, such as sending a [`touchUpInside`](uicontrol/event/touchupinside.md) event to the control. If you’re using a custom view with its own tap gesture recognizer, implement this method to handle the interaction. For example, to perform the action that would have occurred if the user tapped on that item.

UIKit only calls this method if the gesture ends successfully, not if it fails or gets canceled.

## Parameters

- `interaction`: The large content viewer interaction associated with the view that the user interacted with.
- `item`: The item that the user interacted with in the large content viewer.
- `point`: The point where the user’s interaction ended, in the coordinate space of the item’s view.

## See Also

- [func largeContentViewerInteraction(UILargeContentViewerInteraction, itemAt: CGPoint) -> (any UILargeContentViewerItem)?](uilargecontentviewerinteractiondelegate/largecontentviewerinteraction(_:itemat:).md)
  Identifies the large content viewer item for the specified interaction and location.
- [func viewController(for: UILargeContentViewerInteraction) -> UIViewController](uilargecontentviewerinteractiondelegate/viewcontroller(for:).md)
  Specifies which view controller should display the large content viewer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilargecontentviewerinteractiondelegate/largecontentviewerinteraction(_:didendon:at:))*