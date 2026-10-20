# loadData(completionHandler:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Retrieves the game data from the current game session.

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
func loadData(completionHandler: @escaping @Sendable (Data?, (any Error)?) -> Void)
```

```swift
func loadData() async throws -> Data
```

```objc
- (void) loadDataWithCompletionHandler:(void (^)(NSData *data, NSError *error)) completionHandler;
```

## Parameters

- `completionHandler`: A block that is called after the game session data has been loaded.

  - **data**: A `Data` object containing the app’s saved data.
  - **error**: If an error occurred, this parameter holds an error object that explains the error. Otherwise, the value of this parameter is nil. See `GameKit Constants` for a list of error codes specific to GameKit.

## See Also

### Saving and Loading Data
- [func save(Data, completionHandler: (Data?, (any Error)?) -> Void)](./save%28_,completionhandler%29.md)
  Saves the current game session data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgamesession/loaddata(completionhandler:))*