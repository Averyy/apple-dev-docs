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
- `handler`: A block that is called after the player information is retrieved. - **player**: The GKCloudPlayer object representing the currently signed-in player.
- **error**: If an error occurred, this parameter holds an error object that explains the error. Otherwise, the value of this parameter is `nil`. See `GameKit Constants`for a list of error codes specific to GameKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkcloudplayer/getcurrentsignedinplayer(forcontainer:completionhandler:))*