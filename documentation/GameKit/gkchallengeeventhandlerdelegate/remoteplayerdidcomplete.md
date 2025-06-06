# remotePlayerDidComplete(_:)

**Framework**: GameKit  
**Kind**: method

Called when a remote player completes a challenge issued by the local player.

**Availability**:
- macOS 10.8+
- visionOS 1.0+

## Declaration

```swift
optional func remotePlayerDidComplete(_ challenge: GKChallenge!)
```

## Parameters

- `challenge`: The completed challenge.

## See Also

- [func shouldShowBanner(forRemotelyCompletedChallenge: GKChallenge!) -> Bool](gkchallengeeventhandlerdelegate/shouldshowbanner(forremotelycompletedchallenge:).md)
  Called to determine whether a banner should be shown when a remote player completes a challenge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkchallengeeventhandlerdelegate/remoteplayerdidcomplete(_:))*