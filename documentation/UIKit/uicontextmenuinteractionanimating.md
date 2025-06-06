# UIContextMenuInteractionAnimating

**Framework**: UIKit  
**Kind**: protocol

Methods adopted by system-supplied animator objects when interacting with context menus.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
protocol UIContextMenuInteractionAnimating : NSObjectProtocol
```

## Topics

### Adding Custom Animations
- [func addAnimations(() -> Void)](uicontextmenuinteractionanimating/addanimations(_:).md)
  Adds the specified animation block to the animator.
- [func addCompletion(() -> Void)](uicontextmenuinteractionanimating/addcompletion(_:).md)
  Adds the specified completion block to the animator.
### Previewing the Content
- [var previewViewController: UIViewController?](uicontextmenuinteractionanimating/previewviewcontroller.md)
  The current preview view controller.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Inherited By
- [UIContextMenuInteractionCommitAnimating](uicontextmenuinteractioncommitanimating.md)

## See Also

- [func contextMenuInteraction(UIContextMenuInteraction, willDisplayMenuFor: UIContextMenuConfiguration, animator: (any UIContextMenuInteractionAnimating)?)](uicontextmenuinteractiondelegate/contextmenuinteraction(_:willdisplaymenufor:animator:).md)
  Informs the delegate when a menu display begins.
- [func contextMenuInteraction(UIContextMenuInteraction, willEndFor: UIContextMenuConfiguration, animator: (any UIContextMenuInteractionAnimating)?)](uicontextmenuinteractiondelegate/contextmenuinteraction(_:willendfor:animator:).md)
  Informs the delegate when a menu display ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontextmenuinteractionanimating)*