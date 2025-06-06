# getCurrentSignedInPlayer(forContainer:completionHandler:)

**Framework**: GameKit  
**Kind**: method

Returns player information for the currently signed-in player.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class func currentSignedInPlayer(forContainer containerName: String?) async throws -> GKCloudPlayer
```

#### Discussion

The container name must be a unique string associated with the app.

## Parameters

- `containerName`: String containing a unique container name associated with the app.
- `handler`: A block that is called after the player information is retrieved.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkcloudplayer/getcurrentsignedinplayer(forcontainer:completionhandler:))*