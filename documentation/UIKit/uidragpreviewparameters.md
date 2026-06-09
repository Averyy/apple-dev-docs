# UIDragPreviewParameters

**Framework**: UIKit  
**Kind**: class

A set of parameters for adjusting the appearance of a drag item preview or a targeted drag item preview.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIDragPreviewParameters
```

#### Overview

You can refine the appearance of a preview by providing additional parameters when creating a [`UIDragPreview`](uidragpreview.md) or [`UITargetedDragPreview`](uitargeteddragpreview.md) object. The parameters specify different visual aspects of the preview, including the background color and the visible area of the view associated with the preview.

## Relationships

### Inherits From
- [UIPreviewParameters](uipreviewparameters.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class UIDragPreview](uidragpreview.md)
  A graphical preview for a single drag item, used by the system after a drag has started and when no related animation is running.
- [class UIDragPreviewTarget](uidragpreviewtarget.md)
  A geometric specification for the source or destination of a drag item preview, used by the system when a user drops items or cancels a drag activity.
- [class UITargetedDragPreview](uitargeteddragpreview.md)
  A drag item preview used by the system during lift, drop, or cancellation animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidragpreviewparameters)*