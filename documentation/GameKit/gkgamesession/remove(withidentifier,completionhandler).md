# remove(withIdentifier:completionHandler:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Type Method

Removes the specified game session.

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
class func remove(withIdentifier identifier: String, completionHandler: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
class func remove(withIdentifier identifier: String) async throws
```

```objc
+ (void) removeSessionWithIdentifier:(NSString *) identifier completionHandler:(void (^)(NSError *error)) completionHandler;
```

#### Discussion

After the user has finished a game or decides to abandon a game, you must use this function to remove the game session from iCloud. Game sessions are not removed from iCloud automatically.

## Parameters

- `identifier`: The unique string that identifies the game session to be removed.
- `completionHandler`: A block that is called after a game session has been removed from a container.

  - **error**: If an error occurred, this parameter holds an error object that explains the error. Otherwise, the value of this parameter is nil. See `GameKit Constants` for a list of error codes specific to GameKit.

## See Also

### Creating and Loading Game Sessions
- [class func createSession(inContainer: String?, withTitle: String, maxConnectedPlayers: Int, completionHandler: (GKGameSession?, (any Error)?) -> Void)](./createsession%28incontainer,withtitle,maxconnectedplayers,completionhandler%29.md)
  Creates a new game session inside of an iCloud container.
- [class func load(withIdentifier: String, completionHandler: (GKGameSession?, (any Error)?) -> Void)](./load%28withidentifier,completionhandler%29.md)
  Loads a specific game session.
- [class func loadSessions(inContainer: String?, completionHandler: ([GKGameSession]?, (any Error)?) -> Void)](./loadsessions%28incontainer,completionhandler%29.md)
  Retrieves all of the game sessions associated with a container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgamesession/remove(withidentifier:completionhandler:))*