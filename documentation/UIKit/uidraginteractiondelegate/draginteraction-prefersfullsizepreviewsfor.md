# dragInteraction(_:prefersFullSizePreviewsFor:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate whether the preview should appear in its original size or a scaled size.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func dragInteraction(_ interaction: UIDragInteraction, prefersFullSizePreviewsFor session: any UIDragSession) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) to tell the system the preview should appear in its original size; otherwise [`false`](https://developer.apple.com/documentation/Swift/false), which is the default if you don’t provide this method.

#### Discussion

The return value is a recommendation to the system. The system may choose to scale the preview to a smaller size, according to its own rules, even if you return [`true`](https://developer.apple.com/documentation/Swift/true).

## Parameters

- `interaction`: The interaction that called this method.
- `session`: The current drag session.

## See Also

- [func dragInteraction(UIDragInteraction, previewForLifting: UIDragItem, session: any UIDragSession) -> UITargetedDragPreview?](uidraginteractiondelegate/draginteraction(_:previewforlifting:session:).md)
  Asks the delegate for the targeted drag item preview that will appear during the lift animation.
- [func dragInteraction(UIDragInteraction, previewForCancelling: UIDragItem, withDefault: UITargetedDragPreview) -> UITargetedDragPreview?](uidraginteractiondelegate/draginteraction(_:previewforcancelling:withdefault:).md)
  Asks the delegate for the targeted drag item preview to show during the cancellation animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidraginteractiondelegate/draginteraction(_:prefersfullsizepreviewsfor:))*