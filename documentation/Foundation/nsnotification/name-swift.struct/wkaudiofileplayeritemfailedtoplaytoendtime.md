# WKAudioFilePlayerItemFailedToPlayToEndTime

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

A notification that the item failed to play to its end.

**Availability**:
- watchOS 2.0+ - Deprecated in 6.0

> **Deprecated**: Use the [AVFoundation](../../../AVFoundation/AVFoundation.md) framework’s [`AVPlayer`](../../../AVFoundation/avplayer.md) and [`AVQueuePlayer`](../../../AVFoundation/avqueueplayer.md) classes instead.

## Declaration

```swift
static let WKAudioFilePlayerItemFailedToPlayToEndTime: NSNotification.Name
```

## Discussion

The notification’s object is the player item. There is no `userInfo` dictionary.

## See Also

### WatchKit
- [static let WKAccessibilityReduceMotionStatusDidChange: NSNotification.Name](./wkaccessibilityreducemotionstatusdidchange.md)
  Tells the interface controller that the reduce motion status has changed.
- [static let WKAudioFilePlayerItemDidPlayToEndTime: NSNotification.Name](./wkaudiofileplayeritemdidplaytoendtime.md)
  A notification that the item has played successfully to its end.
- [static let WKAudioFilePlayerItemTimeJumped: NSNotification.Name](./wkaudiofileplayeritemtimejumped.md)
  A notification that the item’s current time has changed discontinuously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/wkaudiofileplayeritemfailedtoplaytoendtime)*