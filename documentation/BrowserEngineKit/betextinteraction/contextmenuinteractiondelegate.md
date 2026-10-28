# contextMenuInteractionDelegate

**Framework**: BrowserEngineKit  
**Kind**: property  
**Role**: Instance Property

The delegate for the context menu interaction associated with this text interaction.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- visionOS 1.1+

## Declaration

```swift
weak var contextMenuInteractionDelegate: (any UIContextMenuInteractionDelegate)? { get set }
```

```objc
@property (nonatomic, weak) id<UIContextMenuInteractionDelegate> contextMenuInteractionDelegate;
```

## Discussion

Set this object to receive delegate callbacks from the [`contextMenuInteraction`](./contextmenuinteraction.md).

## See Also

### Menus
- [func presentEditMenuForSelection()](./presenteditmenuforselection%28%29.md)
  Presents an edit menu for the current text selection.
- [func dismissEditMenuForSelection()](./dismisseditmenuforselection%28%29.md)
  Dismisses the edit menu for the current text selection.
- [var contextMenuInteraction: UIContextMenuInteraction](./contextmenuinteraction.md)
  An interaction you use to work with the text view’s context menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinteraction/contextmenuinteractiondelegate)*