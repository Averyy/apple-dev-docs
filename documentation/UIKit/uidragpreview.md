# UIDragPreview

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

A graphical preview for a single drag item, used by the system after a drag has started and when no related animation is running.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIDragPreview
```

```objc
@interface UIDragPreview : NSObject
```

## Overview

A [`UIDragPreview`](./uidragpreview.md) object is a visual representation of the drag item. The preview is displayed while the user moves the item across the screen with their finger (after the lift animation completes). The preview disappears when the user lifts their finger, triggering the start of the drop or cancellation animation.

## Topics

### Initializing a drag item preview
- [convenience init(view: UIView)](./uidragpreview/init%28view%29.md)
  Initializes a new drag item preview with a view, using the default appearance parameters.
- [init(view: UIView, parameters: UIDragPreviewParameters)](./uidragpreview/init%28view,parameters%29.md)
  Initializes a new drag item preview with a view and with a set of appearance parameters.
- [convenience init(forURL: URL)](./uidragpreview/init%28forurl%29.md)
  Initializes a new drag item preview with a URL.
- [convenience init(forURL: URL, title: String?)](./uidragpreview/init%28forurl,title%29.md)
  Initializes a drag item preview with a URL and title.
### Getting the visual appearance parameters
- [var parameters: UIDragPreviewParameters](./uidragpreview/parameters.md)
  The appearance parameters associated with the drag item preview.
### Accessing the view
- [var view: UIView](./uidragpreview/view.md)
  The view associated with the drag item preview.
### Initializers
- [convenience init(for: URL)](./uidragpreview/init%28for%29.md)
- [convenience init(for: URL, title: String?)](./uidragpreview/init%28for,title%29.md)
### Default Implementations
- [UIDragPreview Implementations](./uidragpreview/uidragpreview-implementations.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
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

### Custom drag item previews
- [class UIDragPreviewParameters](./uidragpreviewparameters.md)
  A set of parameters for adjusting the appearance of a drag item preview or a targeted drag item preview.
- [class UIDragPreviewTarget](./uidragpreviewtarget.md)
  A geometric specification for the source or destination of a drag item preview, used by the system when a user drops items or cancels a drag activity.
- [class UITargetedDragPreview](./uitargeteddragpreview.md)
  A drag item preview used by the system during lift, drop, or cancellation animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidragpreview)*