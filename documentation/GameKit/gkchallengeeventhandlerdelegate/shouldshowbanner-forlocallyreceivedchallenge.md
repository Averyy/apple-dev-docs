# shouldShowBanner(forLocallyReceivedChallenge:)

**Framework**: GameKit  
**Kind**: method

Called to determine whether a banner should be shown when the local player receives a challenge.

**Availability**:
- macOS 10.8+
- visionOS 1.0+

## Declaration

```swift
optional func shouldShowBanner(forLocallyReceivedChallenge challenge: GKChallenge!) -> Bool
```

#### Return Value

Your delegate should return [`true`](https://developer.apple.com/documentation/Swift/true) if it wants a banner to be displayed. Otherwise it should return [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

If you do not implement this method, a banner is always shown.

## Parameters

- `challenge`: The received challenge.

## See Also

- [func localPlayerDidReceive(GKChallenge!)](gkchallengeeventhandlerdelegate/localplayerdidreceive(_:).md)
  Called when the local player receives a new challenge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkchallengeeventhandlerdelegate/shouldshowbanner(forlocallyreceivedchallenge:))*