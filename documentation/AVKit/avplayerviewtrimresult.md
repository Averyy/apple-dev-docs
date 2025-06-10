# AVPlayerViewTrimResult

**Framework**: AVKit  
**Kind**: enum

Constants that specify an action a user takes when trimming media in a player view.

**Availability**:
- macOS 10.9+

## Declaration

```swift
enum AVPlayerViewTrimResult
```

## Topics

### Trim Results
- [AVPlayerViewTrimResult.okButton](avplayerviewtrimresult/okbutton.md)
  The user clicked the Trim button.
- [AVPlayerViewTrimResult.cancelButton](avplayerviewtrimresult/cancelbutton.md)
  The user clicked the Cancel button.
### Initializers
- [init?(rawValue: Int)](avplayerviewtrimresult/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var canBeginTrimming: Bool](avplayerview/canbegintrimming.md)
  A Boolean value that indicates whether the player view can begin trimming.
- [func beginTrimming(completionHandler: ((AVPlayerViewTrimResult) -> Void)?)](avplayerview/begintrimming(completionhandler:).md)
  Puts the player view into trimming mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewtrimresult)*