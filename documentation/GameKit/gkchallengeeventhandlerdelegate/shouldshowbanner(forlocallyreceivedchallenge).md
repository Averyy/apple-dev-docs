# shouldShowBanner(forLocallyReceivedChallenge:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Called to determine whether a banner should be shown when the local player receives a challenge.

**Availability**:
- iOS 6.0+ - Deprecated in 7.0
- iPadOS 6.0+ - Deprecated in 7.0
- Mac Catalyst 6.0+ - Deprecated in 7.0
- macOS 10.8+ - Deprecated in 10.10
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: You should instead implement the GKChallengeListener protocol and register a listener with GKLocalPlayer.

## Declaration

```swift
optional func shouldShowBanner(forLocallyReceivedChallenge challenge: GKChallenge!) -> Bool
```

```objc
- (BOOL) shouldShowBannerForLocallyReceivedChallenge:(GKChallenge *) challenge;
```

#### Return Value

Your delegate should return [`true`](../../Swift/true.md) if it wants a banner to be displayed. Otherwise it should return [`false`](../../Swift/false.md).

#### Discussion

If you do not implement this method, a banner is always shown.

## Parameters

- `challenge`: The received challenge.

## See Also

### Responding When a New Challenge is Received
- [func localPlayerDidReceive(GKChallenge!)](./localplayerdidreceive%28_%29.md)
  Called when the local player receives a new challenge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkchallengeeventhandlerdelegate/shouldshowbanner(forlocallyreceivedchallenge:))*