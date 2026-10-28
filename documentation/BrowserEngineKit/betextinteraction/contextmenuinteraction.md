# contextMenuInteraction

**Framework**: BrowserEngineKit  
**Kind**: property  
**Role**: Instance Property

An interaction you use to work with the text view’s context menu.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- visionOS 1.1+

## Declaration

```swift
var contextMenuInteraction: UIContextMenuInteraction { get }
```

```objc
@property (nonatomic, readonly) UIContextMenuInteraction * contextMenuInteraction;
```

## Discussion

Set the context menu interaction’s [`delegate`](../../UIKit/uicontextmenuinteraction/delegate.md) by supplying a value for [`contextMenuInteractionDelegate`](./contextmenuinteractiondelegate.md).

## See Also

### Menus
- [func presentEditMenuForSelection()](./presenteditmenuforselection%28%29.md)
  Presents an edit menu for the current text selection.
- [func dismissEditMenuForSelection()](./dismisseditmenuforselection%28%29.md)
  Dismisses the edit menu for the current text selection.
- [var contextMenuInteractionDelegate: (any UIContextMenuInteractionDelegate)?](./contextmenuinteractiondelegate.md)
  The delegate for the context menu interaction associated with this text interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinteraction/contextmenuinteraction)*