# localPlayerDidComplete(_:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Called when the local player completes a challenge.

**Availability**:
- iOS 6.0+ - Deprecated in 7.0
- iPadOS 6.0+ - Deprecated in 7.0
- Mac Catalyst 6.0+ - Deprecated in 7.0
- macOS 10.8+ - Deprecated in 10.10
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: You should instead implement the GKChallengeListener protocol and register a listener with GKLocalPlayer.

## Declaration

```swift
optional func localPlayerDidComplete(_ challenge: GKChallenge!)
```

```objc
- (void) localPlayerDidCompleteChallenge:(GKChallenge *) challenge;
```

## Parameters

- `challenge`: The completed challenge.

## See Also

### Responding to Challenges Completed By the Local Player
- [func shouldShowBanner(forLocallyCompletedChallenge: GKChallenge!) -> Bool](./shouldshowbanner%28forlocallycompletedchallenge%29.md)
  Called to determine whether a banner should be shown when the local player completes a challenge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkchallengeeventhandlerdelegate/localplayerdidcomplete(_:))*