# paperMarkupViewController(_:didUpdateAdornmentWithID:toAnchor:)

**Framework**: PaperKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells the delegate when a drag session ends for an adornment.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func paperMarkupViewController(_ paperMarkupViewController: PaperMarkupViewController, didUpdateAdornmentWithID id: UUID, toAnchor anchor: MarkupAdornment.Anchor)
```

## Parameters

- `paperMarkupViewController`: The `PaperMarkupViewController` containing the adornment.
- `id`: The ID of the adornment that moved.
- `anchor`: The updated anchor for the adornment.

## Default Implementations

### PaperMarkupViewController.Delegate Implementations
- [func paperMarkupViewController(PaperMarkupViewController, didUpdateAdornmentWithID: UUID, toAnchor: MarkupAdornment.Anchor)](./papermarkupviewcontroller%28_,didupdateadornmentwithid,toanchor%29-3wm3l.md)
  Tells the delegate when a drag session ends for an adornment.

## See Also

### Responding to adornment interactions
- [func paperMarkupViewController(PaperMarkupViewController, didTapAdornmentWithID: UUID)](./papermarkupviewcontroller%28_,didtapadornmentwithid%29.md)
  Tells the delegate when a person taps an adornment.
- [func paperMarkupViewController(PaperMarkupViewController, willUpdateAdornmentWithID: UUID, toProposedAnchor: MarkupAdornment.Anchor) -> MarkupAdornment.Anchor?](./papermarkupviewcontroller%28_,willupdateadornmentwithid,toproposedanchor%29.md)
  Asks the delegate to validate and potentially adjust an adornment’s proposed anchor position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/papermarkupviewcontroller/delegate-swift.protocol/papermarkupviewcontroller(_:didupdateadornmentwithid:toanchor:))*