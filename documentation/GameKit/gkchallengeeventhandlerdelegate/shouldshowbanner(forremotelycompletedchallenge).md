# shouldShowBanner(forRemotelyCompletedChallenge:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Called to determine whether a banner should be shown when a remote player completes a challenge.

**Availability**:
- iOS 6.0+ - Deprecated in 7.0
- iPadOS 6.0+ - Deprecated in 7.0
- Mac Catalyst 6.0+ - Deprecated in 7.0
- macOS 10.8+ - Deprecated in 10.10
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: You should instead implement the GKChallengeListener protocol and register a listener with GKLocalPlayer.

## Declaration

```swift
optional func shouldShowBanner(forRemotelyCompletedChallenge challenge: GKChallenge!) -> Bool
```

```objc
- (BOOL) shouldShowBannerForRemotelyCompletedChallenge:(GKChallenge *) challenge;
```

#### Return Value

Your delegate should return [`true`](../../Swift/true.md) if it wants a banner to be displayed. Otherwise it should return [`false`](../../Swift/false.md).

#### Discussion

If you do not implement this method, a banner is always shown.

## Parameters

- `challenge`: The completed challenge.

## See Also

### Responding to Challenges Issued by the Local Player
- [func remotePlayerDidComplete(GKChallenge!)](./remoteplayerdidcomplete%28_%29.md)
  Called when a remote player completes a challenge issued by the local player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkchallengeeventhandlerdelegate/shouldshowbanner(forremotelycompletedchallenge:))*