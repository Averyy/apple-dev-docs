# loopEnabled

**Framework**: Core Haptics  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A Boolean that determines whether the haptic repeats itself on completion.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var loopEnabled: Bool { get set }
```

```objc
@property (readwrite) BOOL loopEnabled;
```

## See Also

### Setting Playback Properties
- [var loopEnd: TimeInterval](./loopend.md)
  The time at which to end looping haptic playback.
- [var playbackRate: Float](./playbackrate.md)
  The playback rate of the haptic player.
- [var completionHandler: CHHapticAdvancedPatternPlayerCompletionHandler](./completionhandler.md)
  A completion block that runs after the haptic finishes playing.
- [typealias CHHapticAdvancedPatternPlayerCompletionHandler](../chhapticadvancedpatternplayercompletionhandler.md)
  A typealias for the completion handler to run after a haptic finishes playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticadvancedpatternplayer/loopenabled)*