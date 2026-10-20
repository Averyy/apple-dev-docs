# loadData(completionHandler:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Loads the game data from the file.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
func loadData(completionHandler handler: (@Sendable (Data?, (any Error)?) -> Void)? = nil)
```

```swift
func loadData() async throws -> Data
```

```objc
- (void) loadDataWithCompletionHandler:(void (^)(NSData *data, NSError *error)) handler;
```

## Mentions

- [Saving the player’s game data to an iCloud account](../saving-the-player-s-game-data-to-an-icloud-account.md)

## Parameters

- `handler`: The block that this method calls when it completes the request.

  The block receives the following parameters:

  - ***data***: The data object that you saved to the file using the [`saveGameData(_:withName:completionHandler:)`](../gklocalplayer/savegamedata%28_,withname,completionhandler%29.md) method
  - ***error***: Describes an error if it occurs, or `nil` if the operation completes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gksavedgame/loaddata(completionhandler:))*