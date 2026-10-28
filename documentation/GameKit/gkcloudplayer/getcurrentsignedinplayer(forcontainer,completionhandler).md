# getCurrentSignedInPlayer(forContainer:completionHandler:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Type Method

Returns player information for the currently signed-in player.

**Availability**:
- iOS 10.0+ - Deprecated in 12.0
- iPadOS 10.0+ - Deprecated in 12.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.12+ - Deprecated in 10.14
- tvOS 10.0+ - Deprecated in 12.0
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```swift
class func getCurrentSignedInPlayer(forContainer containerName: String?, completionHandler handler: @escaping @Sendable (GKCloudPlayer?, (any Error)?) -> Void)
```

```swift
class func currentSignedInPlayer(forContainer containerName: String?) async throws -> GKCloudPlayer
```

```objc
+ (void) getCurrentSignedInPlayerForContainer:(NSString *) containerName completionHandler:(void (^)(GKCloudPlayer *player, NSError *error)) handler;
```

## Discussion

The container name must be a unique string associated with the app.

## Parameters

- `containerName`: String containing a unique container name associated with the app.
- `handler`: A block that is called after the player information is retrieved.

  - **player**: The GKCloudPlayer object representing the currently signed-in player.
  - **error**: If an error occurred, this parameter holds an error object that explains the error. Otherwise, the value of this parameter is `nil`. See `GameKit Constants`for a list of error codes specific to GameKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkcloudplayer/getcurrentsignedinplayer(forcontainer:completionhandler:))*