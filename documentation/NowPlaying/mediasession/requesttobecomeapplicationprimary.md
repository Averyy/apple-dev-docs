# requestToBecomeApplicationPrimary()

**Framework**: Now Playing  
**Kind**: method

Attempts to make this session your app’s primary media session.

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
@MainActor
func requestToBecomeApplicationPrimary() async throws
```

## Mentions

- [Publishing media sessions](publishing-media-sessions.md)

#### Discussion

Use this method to signal to the system that this session supplies data and handles commands.

> **Note**: [`MediaSessionError.invalidState`](mediasessionerror/invalidstate.md) if the session can’t become active. [`MediaSessionError.internalFailure`](mediasessionerror/internalfailure.md) if the system couldn’t set the active player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/mediasession/requesttobecomeapplicationprimary())*