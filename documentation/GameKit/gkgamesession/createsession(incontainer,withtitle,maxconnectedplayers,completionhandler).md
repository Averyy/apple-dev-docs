# createSession(inContainer:withTitle:maxConnectedPlayers:completionHandler:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Type Method

Creates a new game session inside of an iCloud container.

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
class func createSession(inContainer containerName: String?, withTitle title: String, maxConnectedPlayers maxPlayers: Int, completionHandler: @escaping @Sendable (GKGameSession?, (any Error)?) -> Void)
```

```swift
class func createSession(inContainer containerName: String?, withTitle title: String, maxConnectedPlayers maxPlayers: Int) async throws -> GKGameSession
```

```objc
+ (void) createSessionInContainer:(NSString *) containerName withTitle:(NSString *) title maxConnectedPlayers:(NSInteger) maxPlayers completionHandler:(void (^)(GKGameSession *session, NSError *error)) completionHandler;
```

## Discussion

The container name must be a valid iCloud container associated with your app. After a user has finished a game and is done with a game session, remove the created game session from iCloud using [`remove(withIdentifier:completionHandler:)`](./remove%28withidentifier,completionhandler%29.md). See [iCloud Design Guide](https://developer.apple.com/library/archive/documentation/General/Conceptual/iCloudDesignGuide/Chapters/Introduction.html#//apple_ref/doc/uid/TP40012094) for more information on incorporating iCloud in your app.

## Parameters

- `containerName`: A `String` value representing the iCloud container for the game session.
- `title`: A `String` value representing the title of the game session.
- `maxPlayers`: An `Integer` value indicating the maximum number of players allowed in the game session.
- `completionHandler`: A block that is called after a new game session has been created.

  - **gameSession**: A `GKGameSession` object containing information about the newly created game session.
  - **error**: If an error occurred, this parameter holds an error object that explains the error. Otherwise, the value of this parameter is nil. See `GameKit Constants` for a list of error codes specific to GameKit.

## See Also

### Creating and Loading Game Sessions
- [class func load(withIdentifier: String, completionHandler: (GKGameSession?, (any Error)?) -> Void)](./load%28withidentifier,completionhandler%29.md)
  Loads a specific game session.
- [class func loadSessions(inContainer: String?, completionHandler: ([GKGameSession]?, (any Error)?) -> Void)](./loadsessions%28incontainer,completionhandler%29.md)
  Retrieves all of the game sessions associated with a container.
- [class func remove(withIdentifier: String, completionHandler: ((any Error)?) -> Void)](./remove%28withidentifier,completionhandler%29.md)
  Removes the specified game session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgamesession/createsession(incontainer:withtitle:maxconnectedplayers:completionhandler:))*