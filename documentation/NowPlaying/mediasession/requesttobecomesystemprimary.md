# requestToBecomeSystemPrimary()

**Framework**: Now Playing  
**Kind**: method

Requests to make this session the primary system media session.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
@MainActor
func requestToBecomeSystemPrimary() async throws
```

## Mentions

- [Publishing media sessions](publishing-media-sessions.md)

#### Discussion

Use this method to request that the system display this session prominently on the Lock Screen and in Control Center.

Your app’s primary session should match what your app is prominently displaying to the user in your interface.

For example, if your app has two playing sessions and the user has indicated they want to focus on one of those sessions, call `requestToBecomeSystemPrimary` on that session.

> **Note**: For local playback, calling this method isn’t required unless your app needs to take over as the system primary from another session.

> **Note**: Calling this method doesn’t guarantee the system displays your session on the Lock Screen or in Control Center.

> **Note**: Your app must be in the foreground when calling this method, otherwise this request doesn’t take effect.

> **Note**: [`MediaSessionError.invalidState`](mediasessionerror/invalidstate.md) if the session can’t become application primary. [`MediaSessionError.internalFailure`](mediasessionerror/internalfailure.md) if the system couldn’t promote the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/mediasession/requesttobecomesystemprimary())*