# contextMenuInteraction(_:willDisplayMenuFor:animator:)

**Framework**: UIKit  
**Kind**: method

Informs the delegate when a menu display begins.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func contextMenuInteraction(_ interaction: UIContextMenuInteraction, willDisplayMenuFor configuration: UIContextMenuConfiguration, animator: (any UIContextMenuInteractionAnimating)?)
```

## Parameters

- `interaction`: The interaction object that triggered the interaction.
- `configuration`: The context menu configuration.
- `animator`: The animator to configure custom animations.

## See Also

- [func contextMenuInteraction(UIContextMenuInteraction, willEndFor: UIContextMenuConfiguration, animator: (any UIContextMenuInteractionAnimating)?)](uicontextmenuinteractiondelegate/contextmenuinteraction(_:willendfor:animator:).md)
  Informs the delegate when a menu display ends.
- [protocol UIContextMenuInteractionAnimating](uicontextmenuinteractionanimating.md)
  Methods adopted by system-supplied animator objects when interacting with context menus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontextmenuinteractiondelegate/contextmenuinteraction(_:willdisplaymenufor:animator:))*