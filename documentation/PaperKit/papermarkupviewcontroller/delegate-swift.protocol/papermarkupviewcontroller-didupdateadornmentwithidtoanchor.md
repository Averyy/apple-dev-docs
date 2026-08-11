# paperMarkupViewController(_:didUpdateAdornmentWithID:toAnchor:)

**Framework**: PaperKit  
**Kind**: method  
**Required**: Yes

Tells the delegate when a drag session ends for an adornment.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func paperMarkupViewController(_ paperMarkupViewController: PaperMarkupViewController, didUpdateAdornmentWithID id: UUID, toAnchor anchor: MarkupAdornment.Anchor)
```

## Parameters

- `paperMarkupViewController`: The `PaperMarkupViewController` containing the adornment.
- `id`: The ID of the adornment that moved.
- `anchor`: The updated anchor for the adornment.

## See Also

- [func paperMarkupViewController(PaperMarkupViewController, didTapAdornmentWithID: UUID)](papermarkupviewcontroller/delegate-swift.protocol/papermarkupviewcontroller(_:didtapadornmentwithid:).md)
  Tells the delegate when a person taps an adornment.
- [func paperMarkupViewController(PaperMarkupViewController, willUpdateAdornmentWithID: UUID, toProposedAnchor: MarkupAdornment.Anchor) -> MarkupAdornment.Anchor?](papermarkupviewcontroller/delegate-swift.protocol/papermarkupviewcontroller(_:willupdateadornmentwithid:toproposedanchor:).md)
  Asks the delegate to validate and potentially adjust an adornment’s proposed anchor position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/papermarkupviewcontroller/delegate-swift.protocol/papermarkupviewcontroller(_:didupdateadornmentwithid:toanchor:))*