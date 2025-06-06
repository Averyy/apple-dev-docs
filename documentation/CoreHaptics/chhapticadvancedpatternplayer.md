# CHHapticAdvancedPatternPlayer

**Framework**: Core Haptics  
**Kind**: protocol

A protocol that defines an advanced pattern player capable of looping, seeking, pausing, and resuming haptic playback.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
protocol CHHapticAdvancedPatternPlayer : CHHapticPatternPlayer
```

## Mentions

- [Playing a single-tap haptic pattern](playing-a-single-tap-haptic-pattern.md)

#### Overview

Create instances of this pattern player through a [`CHHapticEngine`](chhapticengine.md) object by calling a factory method such as [`makeAdvancedPlayer(with:)`](chhapticengine/makeadvancedplayer(with:).md). When you ask an advanced pattern player to play, pause, or resume a haptic pattern, the player submits those commands to the haptic engine on your behalf.

Unlike [`CHHapticPatternPlayer`](chhapticpatternplayer.md), the advanced pattern player supports looping of haptic and audio patterns, by setting [`loopEnabled`](chhapticadvancedpatternplayer/loopenabled.md). The advanced pattern player can also call a block when the player finishes, through its [`completionHandler`](chhapticadvancedpatternplayer/completionhandler.md) property.

## Topics

### Setting Playback Properties
- [var loopEnabled: Bool](chhapticadvancedpatternplayer/loopenabled.md)
  A Boolean that determines whether the haptic repeats itself on completion.
- [var loopEnd: TimeInterval](chhapticadvancedpatternplayer/loopend.md)
  The time at which to end looping haptic playback.
- [var playbackRate: Float](chhapticadvancedpatternplayer/playbackrate.md)
  The playback rate of the haptic player.
- [var completionHandler: CHHapticAdvancedPatternPlayerCompletionHandler](chhapticadvancedpatternplayer/completionhandler.md)
  A completion block that runs after the haptic finishes playing.
- [typealias CHHapticAdvancedPatternPlayerCompletionHandler](chhapticadvancedpatternplayercompletionhandler.md)
  A typealias for the completion handler to run after a haptic finishes playback.
### Controlling Playback
- [func pause(atTime: TimeInterval) throws](chhapticadvancedpatternplayer/pause(attime:).md)
  Pauses the haptic player during playback.
- [func resume(atTime: TimeInterval) throws](chhapticadvancedpatternplayer/resume(attime:).md)
  Resumes playing a paused haptic.
- [func seek(toOffset: TimeInterval) throws](chhapticadvancedpatternplayer/seek(tooffset:).md)
  Jumps to the specified offset time in playing the haptic.
### Silencing Haptic Playback
- [var isMuted: Bool](chhapticadvancedpatternplayer/ismuted.md)
  A Boolean value that indicates whether to silences all haptic and audio output from the player.

## Relationships

### Inherits From
- [CHHapticPatternPlayer](chhapticpatternplayer.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Preparing your app to play haptics](preparing-your-app-to-play-haptics.md)
  Set up your app to play haptics.
- [Playing a single-tap haptic pattern](playing-a-single-tap-haptic-pattern.md)
  Create and play a transient haptic pattern from a dictionary literal inline.
- [class CHHapticEngine](chhapticengine.md)
  An object that represents the connection to the haptic server.
- [class CHHapticPattern](chhapticpattern.md)
  An object representing a haptic waveform.
- [protocol CHHapticPatternPlayer](chhapticpatternplayer.md)
  A protocol that defines a standard pattern player capable of playing haptic patterns with fixed parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticadvancedpatternplayer)*