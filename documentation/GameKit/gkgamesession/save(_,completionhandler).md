# save(_:completionHandler:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Saves the current game session data.

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
func save(_ data: Data, completionHandler: @escaping (Data?, (any Error)?) -> Void)
```

```objc
- (void) saveData:(NSData *) data completionHandler:(void (^)(NSData *conflictingData, NSError *error)) completionHandler;
```

#### Discussion

The maximum amount of data to be saved is 512K. The `lastModifiedDate` and `lastModifiedPlayer` properties are updated upon completion. When a save conflict appears, the data is not saved to the server. The data property in the completion handler contains the information currently saved to the server. It is up to the developer to decide how to handle save conflicts.

## Parameters

- `data`: A `Data` object containing the information to be saved.
- `completionHandler`: A block that is called after the data has been saved.

  - **data**: A `Data` object containing the information that is currently saved on the server.
  - **error**: If an error occurred, this parameter holds an error object that explains the error. Otherwise, the value of this parameter is nil. See `GameKit Constants` for a list of error codes specific to GameKit.

## See Also

### Saving and Loading Data
- [func loadData(completionHandler: (Data?, (any Error)?) -> Void)](./loaddata%28completionhandler%29.md)
  Retrieves the game data from the current game session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgamesession/save(_:completionhandler:))*