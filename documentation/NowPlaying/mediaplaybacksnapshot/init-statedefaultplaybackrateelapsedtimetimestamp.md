# init(state:defaultPlaybackRate:elapsedTime:timestamp:)

**Framework**: Now Playing  
**Kind**: init

Creates a playback snapshot with the specified state and timing.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
init(state: MediaPlaybackSnapshot.PlaybackState, defaultPlaybackRate: Float = 1.0, elapsedTime: TimeInterval? = nil, timestamp: Date? = nil)
```

#### Discussion

> **Note**: When `state` is `.playing(let rate)`, `rate` must be finite and non-zero.

> **Note**: `defaultPlaybackRate` must be finite and greater than `0`.

## Parameters

- `state`: The current playback state.
- `defaultPlaybackRate`: The baseline rate the player returns to after temporary rate changes. Defaults to `1.0`.
- `elapsedTime`: The current elapsed time, in seconds.
- `timestamp`: The wall-clock time associated with `elapsedTime`, used to extrapolate the current position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/mediaplaybacksnapshot/init(state:defaultplaybackrate:elapsedtime:timestamp:))*