# paperMarkupViewController(_:didTapAdornmentWithID:)

**Framework**: PaperKit  
**Kind**: method  
**Required**: Yes

Tells the delegate when a person taps an adornment.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func paperMarkupViewController(_ paperMarkupViewController: PaperMarkupViewController, didTapAdornmentWithID id: UUID)
```

## Parameters

- `paperMarkupViewController`: The `PaperMarkupViewController` containing the adornment.
- `id`: The ID of the adornment the person tapped.

## See Also

- [func paperMarkupViewController(PaperMarkupViewController, willUpdateAdornmentWithID: UUID, toProposedAnchor: MarkupAdornment.Anchor) -> MarkupAdornment.Anchor?](papermarkupviewcontroller/delegate-swift.protocol/papermarkupviewcontroller(_:willupdateadornmentwithid:toproposedanchor:).md)
  Asks the delegate to validate and potentially adjust an adornment’s proposed anchor position.
- [func paperMarkupViewController(PaperMarkupViewController, didUpdateAdornmentWithID: UUID, toAnchor: MarkupAdornment.Anchor)](papermarkupviewcontroller/delegate-swift.protocol/papermarkupviewcontroller(_:didupdateadornmentwithid:toanchor:).md)
  Tells the delegate when a drag session ends for an adornment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/papermarkupviewcontroller/delegate-swift.protocol/papermarkupviewcontroller(_:didtapadornmentwithid:))*