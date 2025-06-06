# CHHapticPatternPlayer

**Framework**: Core Haptics  
**Kind**: protocol

A protocol that defines a standard pattern player capable of playing haptic patterns with fixed parameters.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
protocol CHHapticPatternPlayer : NSObjectProtocol
```

## Mentions

- [Playing a single-tap haptic pattern](playing-a-single-tap-haptic-pattern.md)

#### Overview

Create instances of a pattern player through a [`CHHapticEngine`](chhapticengine.md) object by calling a factory method such as [`makePlayer(with:)`](chhapticengine/makeplayer(with:).md). When you ask a pattern player to play a haptic pattern, the player submits those commands to the haptic engine on your behalf.

Use the advanced pattern player, [`CHHapticAdvancedPatternPlayer`](chhapticadvancedpatternplayer.md), when your haptic pattern needs to change during playback, or when you’d like to sync your haptic with a custom audio track. The advanced player allows your app to dynamically change haptic characteristics such as intensity and sharpness through dynamic parameters and parameter curves, capabilities not found in the standard player.

## Topics

### Starting and Stopping Playback
- [func start(atTime: TimeInterval) throws](chhapticpatternplayer/start(attime:).md)
  Starts playing the pattern at the specified time.
- [func stop(atTime: TimeInterval) throws](chhapticpatternplayer/stop(attime:).md)
  Stops playing the pattern at the specified time.
- [func cancel() throws](chhapticpatternplayer/cancel.md)
  Stops the pattern player immediately and returns the specified error.
### Sending Parameters to a Haptic
- [func sendParameters([CHHapticDynamicParameter], atTime: TimeInterval) throws](chhapticpatternplayer/sendparameters(_:attime:).md)
  Sends an array of haptic parameters, starting at the specified time.
- [func scheduleParameterCurve(CHHapticParameterCurve, atTime: TimeInterval) throws](chhapticpatternplayer/scheduleparametercurve(_:attime:).md)
  Schedules a parameter curve to begin transitioning a parameter at a certain time.
### Silencing Haptic Playback
- [var isMuted: Bool](chhapticpatternplayer/ismuted.md)
  A Boolean value that indicates whether to silences all haptic and audio output from the player.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Inherited By
- [CHHapticAdvancedPatternPlayer](chhapticadvancedpatternplayer.md)

## See Also

- [Preparing your app to play haptics](preparing-your-app-to-play-haptics.md)
  Set up your app to play haptics.
- [Playing a single-tap haptic pattern](playing-a-single-tap-haptic-pattern.md)
  Create and play a transient haptic pattern from a dictionary literal inline.
- [class CHHapticEngine](chhapticengine.md)
  An object that represents the connection to the haptic server.
- [class CHHapticPattern](chhapticpattern.md)
  An object representing a haptic waveform.
- [protocol CHHapticAdvancedPatternPlayer](chhapticadvancedpatternplayer.md)
  A protocol that defines an advanced pattern player capable of looping, seeking, pausing, and resuming haptic playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticpatternplayer)*