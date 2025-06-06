# loadSessions(inContainer:completionHandler:)

**Framework**: GameKit  
**Kind**: method

Retrieves all of the game sessions associated with a container.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class func loadSessions(inContainer containerName: String?) async throws -> [GKGameSession]
```

## Parameters

- `containerName`: A unique string that identifies the container to be accessed.
- `completionHandler`: A block that is called after all the game sessions have been loaded.

## See Also

- [class func createSession(inContainer: String?, withTitle: String, maxConnectedPlayers: Int, completionHandler: (GKGameSession?, (any Error)?) -> Void)](gkgamesession/createsession(incontainer:withtitle:maxconnectedplayers:completionhandler:).md)
  Creates a new game session inside of an iCloud container.
- [class func load(withIdentifier: String, completionHandler: (GKGameSession?, (any Error)?) -> Void)](gkgamesession/load(withidentifier:completionhandler:).md)
  Loads a specific game session.
- [class func remove(withIdentifier: String, completionHandler: ((any Error)?) -> Void)](gkgamesession/remove(withidentifier:completionhandler:).md)
  Removes the specified game session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgamesession/loadsessions(incontainer:completionhandler:))*