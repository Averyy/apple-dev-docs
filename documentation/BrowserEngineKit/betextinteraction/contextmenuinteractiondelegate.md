# contextMenuInteractionDelegate

**Framework**: BrowserEngineKit  
**Kind**: property

The delegate for the context menu interaction associated with this text interaction.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- visionOS 1.1+

## Declaration

```swift
@MainActor
weak var contextMenuInteractionDelegate: (any UIContextMenuInteractionDelegate)? { get set }
```

#### Overview

Set this object to receive delegate callbacks from the [`contextMenuInteraction`](betextinteraction/contextmenuinteraction.md).

## See Also

- [func presentEditMenuForSelection()](betextinteraction/presenteditmenuforselection.md)
  Presents an edit menu for the current text selection.
- [func dismissEditMenuForSelection()](betextinteraction/dismisseditmenuforselection.md)
  Dismisses the edit menu for the current text selection.
- [var contextMenuInteraction: UIContextMenuInteraction](betextinteraction/contextmenuinteraction.md)
  An interaction you use to work with the text view’s context menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinteraction/contextmenuinteractiondelegate)*