# canBeginTrimming

**Framework**: AVKit  
**Kind**: property

A Boolean value that indicates whether the player view can begin trimming.

**Availability**:
- macOS 10.9+

## Declaration

```swift
@MainActor
var canBeginTrimming: Bool { get }
```

## Mentions

- [Implementing Trimming in a macOS Player](implementing-trimming-in-a-macos-player.md)

#### Discussion

Before calling [`beginTrimming(completionHandler:)`](avplayerview/begintrimming(completionhandler:).md), check the value of this property to determine whether the player view and current media support trimming. This property value is `false` if the current controls style doesn’t support trimming, the media is content protected, or when playing HTTP Live Streaming media.

If you’re presenting a menu item to initiate trimming, a good place to perform this check is in the [`validateUserInterfaceItem(_:)`](https://developer.apple.com/documentation/AppKit/NSDocument/validateUserInterfaceItem(_:)) method of [`NSDocument`](https://developer.apple.com/documentation/AppKit/NSDocument):

```swift
override func validateUserInterfaceItem(_ item: NSValidatedUserInterfaceItem) -> Bool {
    if item.action == #selector(beginTrimming) {
        return playerView.canBeginTrimming
    }
    return super.validateUserInterfaceItem(item)
}
```

## See Also

- [func beginTrimming(completionHandler: ((AVPlayerViewTrimResult) -> Void)?)](avplayerview/begintrimming(completionhandler:).md)
  Puts the player view into trimming mode.
- [enum AVPlayerViewTrimResult](avplayerviewtrimresult.md)
  Constants that specify an action a user takes when trimming media in a player view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerview/canbegintrimming)*