# AVPlayerViewTrimResult

**Framework**: AVKit  
**Kind**: enum  
**Role**: Enumeration

Constants that specify an action a user takes when trimming media in a player view.

**Availability**:
- macOS 10.9+

## Declaration

```swift
enum AVPlayerViewTrimResult
```

```c
enum AVPlayerViewTrimResult : NSInteger;
```

## Topics

### Creating a trim result
- [init?(rawValue: Int)](./avplayerviewtrimresult/init%28rawvalue%29.md)
### Trim results
- [AVPlayerViewTrimResult.okButton](./avplayerviewtrimresult/okbutton.md)
  The user clicked the Trim button.
- [AVPlayerViewTrimResult.cancelButton](./avplayerviewtrimresult/cancelbutton.md)
  The user clicked the Cancel button.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Media trimming and export
- [Implementing trimming in a macOS player](./implementing-trimming-in-a-macos-player.md)
  Provide a QuickTime media-trimming experience in your macOS app.
- [Trimming and exporting media in visionOS](./trimming-and-exporting-media-in-visionos.md)
  Display standard controls in your app to edit the timeline of the currently playing media.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewtrimresult)*