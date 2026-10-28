# UIPreviewTarget

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

An object that specifies the container view to use for animations.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIPreviewTarget
```

```objc
@interface UIPreviewTarget : NSObject
```

## Overview

Create a [`UIPreviewTarget`](./uipreviewtarget.md) object when animating views to or from a separate container view. For example, use this method to animate views to or from a different part of your app’s interface.

## Topics

### Creating a preview target object
- [init(container: UIView, center: CGPoint, transform: CGAffineTransform)](./uipreviewtarget/init%28container,center,transform%29.md)
  Creates a preview target object using the specified container view and configuration details.
- [convenience init(container: UIView, center: CGPoint)](./uipreviewtarget/init%28container,center%29.md)
  Creates a preview target object using the specified container view and center point.
### Getting the target attributes
- [var container: UIView](./uipreviewtarget/container.md)
  The container for the view being animated.
- [var center: CGPoint](./uipreviewtarget/center.md)
  The point in the containing view at which to place the center of the view being animated.
- [var transform: CGAffineTransform](./uipreviewtarget/transform.md)
  An affine transform to apply to the view being animated.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [UIDragPreviewTarget](./uidragpreviewtarget.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Contextual menus
- [class UIContextMenuSystem](./uicontextmenusystem.md)
  The context menu system.
- [class UIContextMenuInteraction](./uicontextmenuinteraction.md)
  An interaction object that you use to display relevant actions for your content.
- [protocol UIContextMenuInteractionDelegate](./uicontextmenuinteractiondelegate.md)
  The methods for providing the set of actions to perform on your content, and for customizing the preview of that content.
- [class UITargetedPreview](./uitargetedpreview.md)
  An object describing the view to use during preview-related animations.
- [class UIPreviewParameters](./uipreviewparameters.md)
  Additional parameters to use when animating a preview interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipreviewtarget)*