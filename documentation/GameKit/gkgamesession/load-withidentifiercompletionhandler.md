# load(withIdentifier:completionHandler:)

**Framework**: GameKit  
**Kind**: method

Loads a specific game session.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class func load(withIdentifier identifier: String) async throws -> GKGameSession
```

## Parameters

- `identifier`: A unique string that identifies the game session to be loaded.
- `completionHandler`: A block that is called after the game session has been loaded.

## See Also

- [class func createSession(inContainer: String?, withTitle: String, maxConnectedPlayers: Int, completionHandler: (GKGameSession?, (any Error)?) -> Void)](gkgamesession/createsession(incontainer:withtitle:maxconnectedplayers:completionhandler:).md)
  Creates a new game session inside of an iCloud container.
- [class func loadSessions(inContainer: String?, completionHandler: ([GKGameSession]?, (any Error)?) -> Void)](gkgamesession/loadsessions(incontainer:completionhandler:).md)
  Retrieves all of the game sessions associated with a container.
- [class func remove(withIdentifier: String, completionHandler: ((any Error)?) -> Void)](gkgamesession/remove(withidentifier:completionhandler:).md)
  Removes the specified game session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgamesession/load(withidentifier:completionhandler:))*