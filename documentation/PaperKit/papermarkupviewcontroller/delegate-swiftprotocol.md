# PaperMarkupViewController.Delegate

**Framework**: PaperKit  
**Kind**: protocol

The interface for responding to interactions in a markup view controller.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
protocol Delegate : AnyObject
```

## Topics

### Responding to markup changes
- [func paperMarkupViewControllerDidChangeMarkup(PaperMarkupViewController)](papermarkupviewcontroller/delegate-swift.protocol/papermarkupviewcontrollerdidchangemarkup(_:).md)
  Tells the delegate when the markup changes.
- [func paperMarkupViewControllerDidChangeSelection(PaperMarkupViewController)](papermarkupviewcontroller/delegate-swift.protocol/papermarkupviewcontrollerdidchangeselection(_:).md)
  Tells the delegate when the selection changes.
- [func paperMarkupViewControllerDidBeginDrawing(PaperMarkupViewController)](papermarkupviewcontroller/delegate-swift.protocol/papermarkupviewcontrollerdidbegindrawing(_:).md)
  Tells the delegate when a person begins drawing.
- [func paperMarkupViewControllerDidChangeContentVisibleFrame(PaperMarkupViewController)](papermarkupviewcontroller/delegate-swift.protocol/papermarkupviewcontrollerdidchangecontentvisibleframe(_:).md)
  Tells the delegate when a person scrolls or zooms the content.
### Responding to adornment interactions
- [func paperMarkupViewController(PaperMarkupViewController, didTapAdornmentWithID: UUID)](papermarkupviewcontroller/delegate-swift.protocol/papermarkupviewcontroller(_:didtapadornmentwithid:).md)
  Tells the delegate when a person taps an adornment.
- [func paperMarkupViewController(PaperMarkupViewController, willUpdateAdornmentWithID: UUID, toProposedAnchor: MarkupAdornment.Anchor) -> MarkupAdornment.Anchor?](papermarkupviewcontroller/delegate-swift.protocol/papermarkupviewcontroller(_:willupdateadornmentwithid:toproposedanchor:).md)
  Asks the delegate to validate and potentially adjust an adornment’s proposed anchor position.
- [func paperMarkupViewController(PaperMarkupViewController, didUpdateAdornmentWithID: UUID, toAnchor: MarkupAdornment.Anchor)](papermarkupviewcontroller/delegate-swift.protocol/papermarkupviewcontroller(_:didupdateadornmentwithid:toanchor:).md)
  Tells the delegate when a drag session ends for an adornment.

## See Also

- [var delegate: (any PaperMarkupViewController.Delegate)?](papermarkupviewcontroller/delegate-swift.property.md)
  The delegate for responding to a person’s actions.
- [var undoManager: UndoManager?](papermarkupviewcontroller/undomanager.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/papermarkupviewcontroller/delegate-swift.protocol)*