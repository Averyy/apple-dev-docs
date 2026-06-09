# paperMarkupViewController(_:willUpdateAdornmentWithID:toProposedAnchor:)

**Framework**: PaperKit  
**Kind**: method  
**Required**: Yes

Asks the delegate to validate and potentially adjust an adornment’s proposed anchor position.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func paperMarkupViewController(_ paperMarkupViewController: PaperMarkupViewController, willUpdateAdornmentWithID adornmentID: UUID, toProposedAnchor proposedAnchor: MarkupAdornment.Anchor) -> MarkupAdornment.Anchor?
```

#### Return Value

The final anchor position to use for the adornment, or `nil` to deny the move.

## Parameters

- `paperMarkupViewController`: The `PaperMarkupViewController` containing the adornment.
- `adornmentID`: The unique identifier of the adornment the person is moving.
- `proposedAnchor`: The proposed new anchor position for the adornment.

## See Also

- [func paperMarkupViewController(PaperMarkupViewController, didTapAdornmentWithID: UUID)](papermarkupviewcontroller/delegate-swift.protocol/papermarkupviewcontroller(_:didtapadornmentwithid:).md)
  Tells the delegate when a person taps an adornment.
- [func paperMarkupViewController(PaperMarkupViewController, didUpdateAdornmentWithID: UUID, toAnchor: MarkupAdornment.Anchor)](papermarkupviewcontroller/delegate-swift.protocol/papermarkupviewcontroller(_:didupdateadornmentwithid:toanchor:).md)
  Tells the delegate when a drag session ends for an adornment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/papermarkupviewcontroller/delegate-swift.protocol/papermarkupviewcontroller(_:willupdateadornmentwithid:toproposedanchor:))*