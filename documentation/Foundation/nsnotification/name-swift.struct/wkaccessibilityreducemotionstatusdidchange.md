# WKAccessibilityReduceMotionStatusDidChange

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

Tells the interface controller that the reduce motion status has changed.

**Availability**:
- watchOS 4.0+

## Declaration

```swift
static let WKAccessibilityReduceMotionStatusDidChange: NSNotification.Name
```

#### Discussion

Use this notification to customize your application’s user interface for when reduced motion is enabled. You can also use the [`WKAccessibilityIsReduceMotionEnabled()`](../../../WatchKit/wkaccessibilityisreducemotionenabled%28%29.md) function to determine whether reduced motion is enabled.

Observe this notification using the default notification center. This notification doesn’t include a parameter.

## See Also

### WatchKit
- [static let WKAudioFilePlayerItemDidPlayToEndTime: NSNotification.Name](./wkaudiofileplayeritemdidplaytoendtime.md)
  A notification that the item has played successfully to its end.
- [static let WKAudioFilePlayerItemFailedToPlayToEndTime: NSNotification.Name](./wkaudiofileplayeritemfailedtoplaytoendtime.md)
  A notification that the item failed to play to its end.
- [static let WKAudioFilePlayerItemTimeJumped: NSNotification.Name](./wkaudiofileplayeritemtimejumped.md)
  A notification that the item’s current time has changed discontinuously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/wkaccessibilityreducemotionstatusdidchange)*