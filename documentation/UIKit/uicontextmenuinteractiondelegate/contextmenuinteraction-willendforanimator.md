# contextMenuInteraction(_:willEndFor:animator:)

**Framework**: UIKit  
**Kind**: method

Informs the delegate when a menu display ends.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func contextMenuInteraction(_ interaction: UIContextMenuInteraction, willEndFor configuration: UIContextMenuConfiguration, animator: (any UIContextMenuInteractionAnimating)?)
```

## Parameters

- `interaction`: The interaction object that triggered the interaction.
- `configuration`: The context menu configuration.
- `animator`: The animator to configure custom animations.

## See Also

- [func contextMenuInteraction(UIContextMenuInteraction, willDisplayMenuFor: UIContextMenuConfiguration, animator: (any UIContextMenuInteractionAnimating)?)](uicontextmenuinteractiondelegate/contextmenuinteraction(_:willdisplaymenufor:animator:).md)
  Informs the delegate when a menu display begins.
- [protocol UIContextMenuInteractionAnimating](uicontextmenuinteractionanimating.md)
  Methods adopted by system-supplied animator objects when interacting with context menus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontextmenuinteractiondelegate/contextmenuinteraction(_:willendfor:animator:))*