# paperMarkupViewController(_:willUpdateAdornmentWithID:toProposedAnchor:)

**Framework**: PaperKit  
**Kind**: method  
**Role**: Instance Method

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/papermarkupviewcontroller/delegate-swift.protocol/papermarkupviewcontroller(_:willupdateadornmentwithid:toproposedanchor:)-5m1yu)*