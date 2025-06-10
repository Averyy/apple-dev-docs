# WKAccessibilityReduceMotionStatusDidChange

**Framework**: Foundation  
**Kind**: property

Tells the interface controller that the reduce motion status has changed.

**Availability**:
- watchOS 4.0+

## Declaration

```swift
static let WKAccessibilityReduceMotionStatusDidChange: NSNotification.Name
```

#### Discussion

Use this notification to customize your application’s user interface for when reduced motion is enabled. You can also use the [`WKAccessibilityIsReduceMotionEnabled()`](https://developer.apple.com/documentation/WatchKit/WKAccessibilityIsReduceMotionEnabled()) function to determine whether reduced motion is enabled.

Observe this notification using the default notification center. This notification doesn’t include a parameter.

## See Also

- [static let WKAudioFilePlayerItemDidPlayToEndTime: NSNotification.Name](nsnotification/name-swift.struct/wkaudiofileplayeritemdidplaytoendtime.md)
  A notification that the item has played successfully to its end.
- [static let WKAudioFilePlayerItemFailedToPlayToEndTime: NSNotification.Name](nsnotification/name-swift.struct/wkaudiofileplayeritemfailedtoplaytoendtime.md)
  A notification that the item failed to play to its end.
- [static let WKAudioFilePlayerItemTimeJumped: NSNotification.Name](nsnotification/name-swift.struct/wkaudiofileplayeritemtimejumped.md)
  A notification that the item’s current time has changed discontinuously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/wkaccessibilityreducemotionstatusdidchange)*