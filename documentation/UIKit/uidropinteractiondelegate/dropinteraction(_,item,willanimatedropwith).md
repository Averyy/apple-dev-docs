# dropInteraction(_:item:willAnimateDropWith:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate the system’s drop animation is about to start.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func dropInteraction(_ interaction: UIDropInteraction, item: UIDragItem, willAnimateDropWith animator: any UIDragAnimating)
```

```objc
- (void) dropInteraction:(UIDropInteraction *) interaction item:(UIDragItem *) item willAnimateDropWithAnimator:(id<UIDragAnimating>) animator;
```

## Discussion

This method is called for each drag item in the session, whether the item’s visible or not.

## Parameters

- `interaction`: The interaction that called this method.
- `item`: The current drag item.
- `animator`: The animator that provides custom animations to run alongside the system’s drop animation. You can also use it to add a completion block that runs after the animations have finished.

## See Also

### Animating the drop
- [func dropInteraction(UIDropInteraction, previewForDropping: UIDragItem, withDefault: UITargetedDragPreview) -> UITargetedDragPreview?](./dropinteraction%28_,previewfordropping,withdefault%29.md)
  Asks the delegate for the targeted drag item preview to show during the drop animation.
- [func dropInteraction(UIDropInteraction, concludeDrop: any UIDropSession)](./dropinteraction%28_,concludedrop%29.md)
  Tells the delegate the drop activity and its related animations have finished.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidropinteractiondelegate/dropinteraction(_:item:willanimatedropwith:))*