# modificationDate

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

The date when you saved the game data or modified it.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
var modificationDate: Date? { get }
```

```objc
@property (atomic, readonly, nullable) NSDate * modificationDate;
```

#### Discussion

Game Center sets this property when you save game data using the [`saveGameData(_:withName:completionHandler:)`](../gklocalplayer/savegamedata%28_,withname,completionhandler%29.md) method. If you save game data using an existing filename, Game Center overwrites the file with the new data and changes the modification date.

## See Also

### Retrieving Information About a Saved Game File
- [var name: String?](./name.md)
  The name of the saved game.
- [var deviceName: String?](./devicename.md)
  The name of the device that the player uses to save the game.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gksavedgame/modificationdate)*