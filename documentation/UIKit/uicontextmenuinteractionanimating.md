# UIContextMenuInteractionAnimating

**Framework**: UIKit  
**Kind**: protocol  
**Role**: Protocol

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

```objc
@protocol UIContextMenuInteractionAnimating <NSObject>
```

## Topics

### Adding Custom Animations
- [func addAnimations(() -> Void)](./uicontextmenuinteractionanimating/addanimations%28_%29.md)
  Adds the specified animation block to the animator.
- [func addCompletion(() -> Void)](./uicontextmenuinteractionanimating/addcompletion%28_%29.md)
  Adds the specified completion block to the animator.
### Previewing the Content
- [var previewViewController: UIViewController?](./uicontextmenuinteractionanimating/previewviewcontroller.md)
  The current preview view controller.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Inherited By
- [UIContextMenuInteractionCommitAnimating](./uicontextmenuinteractioncommitanimating.md)

## See Also

### Handling animations
- [func contextMenuInteraction(UIContextMenuInteraction, willDisplayMenuFor: UIContextMenuConfiguration, animator: (any UIContextMenuInteractionAnimating)?)](./uicontextmenuinteractiondelegate/contextmenuinteraction%28_,willdisplaymenufor,animator%29.md)
  Informs the delegate when a menu display begins.
- [func contextMenuInteraction(UIContextMenuInteraction, willEndFor: UIContextMenuConfiguration, animator: (any UIContextMenuInteractionAnimating)?)](./uicontextmenuinteractiondelegate/contextmenuinteraction%28_,willendfor,animator%29.md)
  Informs the delegate when a menu display ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontextmenuinteractionanimating)*