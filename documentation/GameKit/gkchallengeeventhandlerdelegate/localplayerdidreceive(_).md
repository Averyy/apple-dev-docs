# localPlayerDidReceive(_:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Called when the local player receives a new challenge.

**Availability**:
- iOS 6.0+ - Deprecated in 7.0
- iPadOS 6.0+ - Deprecated in 7.0
- Mac Catalyst 6.0+ - Deprecated in 7.0
- macOS 10.8+ - Deprecated in 10.10
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: You should instead implement the GKChallengeListener protocol and register a listener with GKLocalPlayer.

## Declaration

```swift
optional func localPlayerDidReceive(_ challenge: GKChallenge!)
```

```objc
- (void) localPlayerDidReceiveChallenge:(GKChallenge *) challenge;
```

## Parameters

- `challenge`: The received challenge.

## See Also

### Responding When a New Challenge is Received
- [func shouldShowBanner(forLocallyReceivedChallenge: GKChallenge!) -> Bool](./shouldshowbanner%28forlocallyreceivedchallenge%29.md)
  Called to determine whether a banner should be shown when the local player receives a challenge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkchallengeeventhandlerdelegate/localplayerdidreceive(_:))*