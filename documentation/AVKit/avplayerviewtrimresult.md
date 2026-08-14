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

### Creating a trim result
- [init?(rawValue: Int)](avplayerviewtrimresult/init(rawvalue:).md)
### Trim Results
- [AVPlayerViewTrimResult.okButton](avplayerviewtrimresult/okbutton.md)
  The user clicked the Trim button.
- [AVPlayerViewTrimResult.cancelButton](avplayerviewtrimresult/cancelbutton.md)
  The user clicked the Cancel button.

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var canBeginTrimming: Bool](avplayerview/canbegintrimming.md)
  A Boolean value that indicates whether the player view can begin trimming.
- [func beginTrimming(completionHandler: ((AVPlayerViewTrimResult) -> Void)?)](avplayerview/begintrimming(completionhandler:).md)
  Puts the player view into trimming mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewtrimresult)*