# contextMenuInteraction(_:willPerformPreviewActionForMenuWith:animator:)

**Framework**: UIKit  
**Kind**: method

Informs the delegate when a preview action begins.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func contextMenuInteraction(_ interaction: UIContextMenuInteraction, willPerformPreviewActionForMenuWith configuration: UIContextMenuConfiguration, animator: any UIContextMenuInteractionCommitAnimating)
```

## Parameters

- `interaction`: The interaction object that triggered the interaction.
- `configuration`: The context menu configuration.
- `animator`: The animator to configure custom animations.

## See Also

- [protocol UIContextMenuInteractionCommitAnimating](uicontextmenuinteractioncommitanimating.md)
  Methods adopted by system-supplied animator objects when committing preview-related animations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontextmenuinteractiondelegate/contextmenuinteraction(_:willperformpreviewactionformenuwith:animator:))*