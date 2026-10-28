# exitsFullScreenWhenPlaybackEnds

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the player exits full-screen mode when playback ends.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var exitsFullScreenWhenPlaybackEnds: Bool { get set }
```

```objc
@property (nonatomic) BOOL exitsFullScreenWhenPlaybackEnds;
```

## Discussion

If you enqueue multiple player items, the player exits full-screen mode after it plays all remaining items in the queue.

The default value is `false`.

## See Also

### Managing full-screen behavior
- [var entersFullScreenWhenPlaybackBegins: Bool](./entersfullscreenwhenplaybackbegins.md)
  A Boolean value that determines whether the player automatically displays in full screen when someone taps the Play button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewcontroller/exitsfullscreenwhenplaybackends)*