# UIDragPreviewTarget

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

A geometric specification for the source or destination of a drag item preview, used by the system when a user drops items or cancels a drag activity.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIDragPreviewTarget
```

```objc
@interface UIDragPreviewTarget : UIPreviewTarget
```

## Relationships

### Inherits From
- [UIPreviewTarget](./uipreviewtarget.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Custom drag item previews
- [class UIDragPreviewParameters](./uidragpreviewparameters.md)
  A set of parameters for adjusting the appearance of a drag item preview or a targeted drag item preview.
- [class UIDragPreview](./uidragpreview.md)
  A graphical preview for a single drag item, used by the system after a drag has started and when no related animation is running.
- [class UITargetedDragPreview](./uitargeteddragpreview.md)
  A drag item preview used by the system during lift, drop, or cancellation animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidragpreviewtarget)*