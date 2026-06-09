# requestToBecomeApplicationPrimary()

**Framework**: Now Playing  
**Kind**: method

Attempts to make this session your app’s primary media session.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

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