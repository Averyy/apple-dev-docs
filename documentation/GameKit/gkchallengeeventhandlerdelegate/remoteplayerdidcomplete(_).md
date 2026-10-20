# remotePlayerDidComplete(_:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Called when a remote player completes a challenge issued by the local player.

**Availability**:
- iOS 6.0+ - Deprecated in 7.0
- iPadOS 6.0+ - Deprecated in 7.0
- Mac Catalyst 6.0+ - Deprecated in 7.0
- macOS 10.8+ - Deprecated in 10.10
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: You should instead implement the GKChallengeListener protocol and register a listener with GKLocalPlayer.

## Declaration

```swift
optional func remotePlayerDidComplete(_ challenge: GKChallenge!)
```

```objc
- (void) remotePlayerDidCompleteChallenge:(GKChallenge *) challenge;
```

## Parameters

- `challenge`: The completed challenge.

## See Also

### Responding to Challenges Issued by the Local Player
- [func shouldShowBanner(forRemotelyCompletedChallenge: GKChallenge!) -> Bool](./shouldshowbanner%28forremotelycompletedchallenge%29.md)
  Called to determine whether a banner should be shown when a remote player completes a challenge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkchallengeeventhandlerdelegate/remoteplayerdidcomplete(_:))*