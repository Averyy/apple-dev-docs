# load(withIdentifier:completionHandler:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Type Method

Loads a specific game session.

**Availability**:
- iOS 10.0+ - Deprecated in 12.0
- iPadOS 10.0+ - Deprecated in 12.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.12+ - Deprecated in 10.14
- tvOS 10.0+ - Deprecated in 12.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: For real-time matches, use GKMatchmakerViewController. For turn-based matches, use GKTurnBasedMatchmakerViewController.

## Declaration

```swift
class func load(withIdentifier identifier: String, completionHandler: @escaping @Sendable (GKGameSession?, (any Error)?) -> Void)
```

```swift
class func load(withIdentifier identifier: String) async throws -> GKGameSession
```

```objc
+ (void) loadSessionWithIdentifier:(NSString *) identifier completionHandler:(void (^)(GKGameSession *session, NSError *error)) completionHandler;
```

## Parameters

- `identifier`: A unique string that identifies the game session to be loaded.
- `completionHandler`: A block that is called after the game session has been loaded.

  - **session**: The `GKGameSession` object associated with the specified identifier.
  - **error**: If an error occurred, this parameter holds an error object that explains the error. Otherwise, the value of this parameter is nil. See `GameKit Constants` for a list of error codes specific to GameKit.

## See Also

### Creating and Loading Game Sessions
- [class func createSession(inContainer: String?, withTitle: String, maxConnectedPlayers: Int, completionHandler: (GKGameSession?, (any Error)?) -> Void)](./createsession%28incontainer,withtitle,maxconnectedplayers,completionhandler%29.md)
  Creates a new game session inside of an iCloud container.
- [class func loadSessions(inContainer: String?, completionHandler: ([GKGameSession]?, (any Error)?) -> Void)](./loadsessions%28incontainer,completionhandler%29.md)
  Retrieves all of the game sessions associated with a container.
- [class func remove(withIdentifier: String, completionHandler: ((any Error)?) -> Void)](./remove%28withidentifier,completionhandler%29.md)
  Removes the specified game session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgamesession/load(withidentifier:completionhandler:))*