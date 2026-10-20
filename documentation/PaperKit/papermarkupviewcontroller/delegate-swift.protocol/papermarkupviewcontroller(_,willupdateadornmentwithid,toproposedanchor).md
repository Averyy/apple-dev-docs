# paperMarkupViewController(_:willUpdateAdornmentWithID:toProposedAnchor:)

**Framework**: PaperKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Asks the delegate to validate and potentially adjust an adornment’s proposed anchor position.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func paperMarkupViewController(_ paperMarkupViewController: PaperMarkupViewController, willUpdateAdornmentWithID id: UUID, toProposedAnchor proposedAnchor: MarkupAdornment.Anchor) -> MarkupAdornment.Anchor?
```

#### Return Value

The final anchor position to use for the adornment, or `nil` to deny the move.

## Parameters

- `paperMarkupViewController`: The `PaperMarkupViewController` containing the adornment.
- `id`: The unique identifier of the adornment the person is moving.
- `proposedAnchor`: The proposed new anchor position for the adornment.

## Default Implementations

### PaperMarkupViewController.Delegate Implementations
- [func paperMarkupViewController(PaperMarkupViewController, willUpdateAdornmentWithID: UUID, toProposedAnchor: MarkupAdornment.Anchor) -> MarkupAdornment.Anchor?](./papermarkupviewcontroller%28_,willupdateadornmentwithid,toproposedanchor%29-5m1yu.md)
  Asks the delegate to validate and potentially adjust an adornment’s proposed anchor position.

## See Also

### Responding to adornment interactions
- [func paperMarkupViewController(PaperMarkupViewController, didTapAdornmentWithID: UUID)](./papermarkupviewcontroller%28_,didtapadornmentwithid%29.md)
  Tells the delegate when a person taps an adornment.
- [func paperMarkupViewController(PaperMarkupViewController, didUpdateAdornmentWithID: UUID, toAnchor: MarkupAdornment.Anchor)](./papermarkupviewcontroller%28_,didupdateadornmentwithid,toanchor%29.md)
  Tells the delegate when a drag session ends for an adornment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/papermarkupviewcontroller/delegate-swift.protocol/papermarkupviewcontroller(_:willupdateadornmentwithid:toproposedanchor:))*