# canBeginTrimming

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the player view can begin trimming.

**Availability**:
- macOS 10.9+

## Declaration

```swift
var canBeginTrimming: Bool { get }
```

```objc
@property (readonly) BOOL canBeginTrimming;
```

## Mentions

- [Implementing trimming in a macOS player](../implementing-trimming-in-a-macos-player.md)

## Discussion

Before calling [`beginTrimming(completionHandler:)`](./begintrimming%28completionhandler%29.md), check the value of this property to determine whether the player view and current media support trimming. This property value is `false` if the current controls style doesn’t support trimming, the media is content protected, or when playing HTTP Live Streaming media.

If you’re presenting a menu item to initiate trimming, a good place to perform this check is in the [`validateUserInterfaceItem(_:)`](../../AppKit/nsdocument/validateuserinterfaceitem%28_%29.md) method of [`NSDocument`](../../AppKit/nsdocument.md):

```swift
override func validateUserInterfaceItem(_ item: NSValidatedUserInterfaceItem) -> Bool {
    if item.action == #selector(beginTrimming) {
        return playerView.canBeginTrimming
    }
    return super.validateUserInterfaceItem(item)
}
```

## See Also

### Trimming media
- [func beginTrimming(completionHandler: ((AVPlayerViewTrimResult) -> Void)?)](./begintrimming%28completionhandler%29.md)
  Puts the player view into trimming mode.
- [enum AVPlayerViewTrimResult](../avplayerviewtrimresult.md)
  Constants that specify an action a user takes when trimming media in a player view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerview/canbegintrimming)*