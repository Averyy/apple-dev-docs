# shouldShowBanner(forRemotelyCompletedChallenge:)

**Framework**: GameKit  
**Kind**: method

Called to determine whether a banner should be shown when a remote player completes a challenge.

**Availability**:
- macOS 10.8+
- visionOS 1.0+

## Declaration

```swift
optional func shouldShowBanner(forRemotelyCompletedChallenge challenge: GKChallenge!) -> Bool
```

#### Return Value

Your delegate should return [`true`](https://developer.apple.com/documentation/Swift/true) if it wants a banner to be displayed. Otherwise it should return [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

If you do not implement this method, a banner is always shown.

## Parameters

- `challenge`: The completed challenge.

## See Also

- [func remotePlayerDidComplete(GKChallenge!)](gkchallengeeventhandlerdelegate/remoteplayerdidcomplete(_:).md)
  Called when a remote player completes a challenge issued by the local player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkchallengeeventhandlerdelegate/shouldshowbanner(forremotelycompletedchallenge:))*