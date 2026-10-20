# PaperMarkupViewController.Delegate

**Framework**: PaperKit  
**Kind**: protocol  
**Role**: Protocol

The interface for responding to interactions in a markup view controller.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
protocol Delegate : AnyObject
```

## Topics

### Responding to markup changes
- [func paperMarkupViewControllerDidChangeMarkup(PaperMarkupViewController)](./delegate-swift.protocol/papermarkupviewcontrollerdidchangemarkup%28_%29.md)
  Tells the delegate when the markup changes.
- [func paperMarkupViewControllerDidChangeSelection(PaperMarkupViewController)](./delegate-swift.protocol/papermarkupviewcontrollerdidchangeselection%28_%29.md)
  Tells the delegate when the selection changes.
- [func paperMarkupViewControllerDidBeginDrawing(PaperMarkupViewController)](./delegate-swift.protocol/papermarkupviewcontrollerdidbegindrawing%28_%29.md)
  Tells the delegate when a person begins drawing.
- [func paperMarkupViewControllerDidChangeContentVisibleFrame(PaperMarkupViewController)](./delegate-swift.protocol/papermarkupviewcontrollerdidchangecontentvisibleframe%28_%29.md)
  Tells the delegate when a person scrolls or zooms the content.
### Responding to adornment interactions
- [func paperMarkupViewController(PaperMarkupViewController, didTapAdornmentWithID: UUID)](./delegate-swift.protocol/papermarkupviewcontroller%28_,didtapadornmentwithid%29.md)
  Tells the delegate when a person taps an adornment.
- [func paperMarkupViewController(PaperMarkupViewController, willUpdateAdornmentWithID: UUID, toProposedAnchor: MarkupAdornment.Anchor) -> MarkupAdornment.Anchor?](./delegate-swift.protocol/papermarkupviewcontroller%28_,willupdateadornmentwithid,toproposedanchor%29.md)
  Asks the delegate to validate and potentially adjust an adornment’s proposed anchor position.
- [func paperMarkupViewController(PaperMarkupViewController, didUpdateAdornmentWithID: UUID, toAnchor: MarkupAdornment.Anchor)](./delegate-swift.protocol/papermarkupviewcontroller%28_,didupdateadornmentwithid,toanchor%29.md)
  Tells the delegate when a drag session ends for an adornment.

## See Also

### Responding to changes
- [var delegate: (any PaperMarkupViewController.Delegate)?](./delegate-swift.property.md)
  The delegate for responding to a person’s actions.
- [var undoManager: UndoManager?](./undomanager.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/papermarkupviewcontroller/delegate-swift.protocol)*