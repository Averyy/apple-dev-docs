# UIContextMenuInteractionCommitAnimating

**Framework**: UIKit  
**Kind**: protocol

Methods adopted by system-supplied animator objects when committing preview-related animations.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
protocol UIContextMenuInteractionCommitAnimating : UIContextMenuInteractionAnimating
```

#### Overview

When the user taps in a preview interface to dismiss it, UIKit creates an object that adopts this protocol and passes it to your [`UIContextMenuInteractionDelegate`](uicontextmenuinteractiondelegate.md) method. Use the object to add any custom animations that you want to run alongside the dismissal animations.

## Topics

### Specifying the Commit Style
- [var preferredCommitStyle: UIContextMenuInteractionCommitStyle](uicontextmenuinteractioncommitanimating/preferredcommitstyle.md)
  The preferred animation style triggered when the user taps the preview.
- [enum UIContextMenuInteractionCommitStyle](uicontextmenuinteractioncommitstyle.md)
  Constants that control the interaction commit style.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [UIContextMenuInteractionAnimating](uicontextmenuinteractionanimating.md)

## See Also

- [func contextMenuInteraction(UIContextMenuInteraction, willPerformPreviewActionForMenuWith: UIContextMenuConfiguration, animator: any UIContextMenuInteractionCommitAnimating)](uicontextmenuinteractiondelegate/contextmenuinteraction(_:willperformpreviewactionformenuwith:animator:).md)
  Informs the delegate when a preview action begins.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontextmenuinteractioncommitanimating)*