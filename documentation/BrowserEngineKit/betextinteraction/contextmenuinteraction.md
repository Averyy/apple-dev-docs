# contextMenuInteraction

**Framework**: BrowserEngineKit  
**Kind**: property

An interaction you use to work with the text view’s context menu.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- visionOS 1.1+

## Declaration

```swift
@MainActor
var contextMenuInteraction: UIContextMenuInteraction { get }
```

#### Overview

Set the context menu interaction’s [`delegate`](https://developer.apple.com/documentation/UIKit/UIContextMenuInteraction/delegate) by supplying a value for [`contextMenuInteractionDelegate`](betextinteraction/contextmenuinteractiondelegate.md).

## See Also

- [func presentEditMenuForSelection()](betextinteraction/presenteditmenuforselection.md)
  Presents an edit menu for the current text selection.
- [func dismissEditMenuForSelection()](betextinteraction/dismisseditmenuforselection.md)
  Dismisses the edit menu for the current text selection.
- [var contextMenuInteractionDelegate: (any UIContextMenuInteractionDelegate)?](betextinteraction/contextmenuinteractiondelegate.md)
  The delegate for the context menu interaction associated with this text interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinteraction/contextmenuinteraction)*