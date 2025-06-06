# createSession(inContainer:withTitle:maxConnectedPlayers:completionHandler:)

**Framework**: GameKit  
**Kind**: method

Creates a new game session inside of an iCloud container.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class func createSession(inContainer containerName: String?, withTitle title: String, maxConnectedPlayers maxPlayers: Int) async throws -> GKGameSession
```

#### Discussion

The container name must be a valid iCloud container associated with your app. After a user has finished a game and is done with a game session, remove the created game session from iCloud using [`remove(withIdentifier:completionHandler:)`](gkgamesession/remove(withidentifier:completionhandler:).md). See [`iCloud Design Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/iCloudDesignGuide/Chapters/Introduction.html#//apple_ref/doc/uid/TP40012094) for more information on incorporating iCloud in your app.

## Parameters

- `containerName`: A   value representing the iCloud container for the game session.
- `title`: A   value representing the title of the game session.
- `maxPlayers`: An   value indicating the maximum number of players allowed in the game session.
- `completionHandler`: A block that is called after a new game session has been created.

## See Also

- [class func load(withIdentifier: String, completionHandler: (GKGameSession?, (any Error)?) -> Void)](gkgamesession/load(withidentifier:completionhandler:).md)
  Loads a specific game session.
- [class func loadSessions(inContainer: String?, completionHandler: ([GKGameSession]?, (any Error)?) -> Void)](gkgamesession/loadsessions(incontainer:completionhandler:).md)
  Retrieves all of the game sessions associated with a container.
- [class func remove(withIdentifier: String, completionHandler: ((any Error)?) -> Void)](gkgamesession/remove(withidentifier:completionhandler:).md)
  Removes the specified game session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgamesession/createsession(incontainer:withtitle:maxconnectedplayers:completionhandler:))*