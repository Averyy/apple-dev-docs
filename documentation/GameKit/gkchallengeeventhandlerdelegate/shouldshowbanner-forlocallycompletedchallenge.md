# shouldShowBanner(forLocallyCompletedChallenge:)

**Framework**: GameKit  
**Kind**: method

Called to determine whether a banner should be shown when the local player completes a challenge.

**Availability**:
- macOS 10.8+
- visionOS 1.0+

## Declaration

```swift
optional func shouldShowBanner(forLocallyCompletedChallenge challenge: GKChallenge!) -> Bool
```

#### Return Value

Your delegate should return [`true`](https://developer.apple.com/documentation/Swift/true) if it wants a banner to be displayed. Otherwise it should return [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

If you do not implement this method, a banner is always shown.

## Parameters

- `challenge`: The completed challenge.

## See Also

- [func localPlayerDidComplete(GKChallenge!)](gkchallengeeventhandlerdelegate/localplayerdidcomplete(_:).md)
  Called when the local player completes a challenge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkchallengeeventhandlerdelegate/shouldshowbanner(forlocallycompletedchallenge:))*