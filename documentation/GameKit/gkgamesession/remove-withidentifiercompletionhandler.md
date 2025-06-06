# remove(withIdentifier:completionHandler:)

**Framework**: GameKit  
**Kind**: method

Removes the specified game session.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class func remove(withIdentifier identifier: String) async throws
```

#### Discussion

After the user has finished a game or decides to abandon a game, you must use this function to remove the game session from iCloud. Game sessions are not removed from iCloud automatically.

## Parameters

- `identifier`: The unique string that identifies the game session to be removed.
- `completionHandler`: A block that is called after a game session has been removed from a container.

## See Also

- [class func createSession(inContainer: String?, withTitle: String, maxConnectedPlayers: Int, completionHandler: (GKGameSession?, (any Error)?) -> Void)](gkgamesession/createsession(incontainer:withtitle:maxconnectedplayers:completionhandler:).md)
  Creates a new game session inside of an iCloud container.
- [class func load(withIdentifier: String, completionHandler: (GKGameSession?, (any Error)?) -> Void)](gkgamesession/load(withidentifier:completionhandler:).md)
  Loads a specific game session.
- [class func loadSessions(inContainer: String?, completionHandler: ([GKGameSession]?, (any Error)?) -> Void)](gkgamesession/loadsessions(incontainer:completionhandler:).md)
  Retrieves all of the game sessions associated with a container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgamesession/remove(withidentifier:completionhandler:))*