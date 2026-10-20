# directoryState

**Framework**: GameSave  
**Kind**: property  
**Role**: Instance Property

The state of the directory.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var directoryState: GSSyncedDirectoryState { get }
```

```objc
@property (readonly, nonnull) GSSyncedDirectoryState * directoryState;
```

## See Also

### Accessing a directory
- [class func open(forContainerIdentifier: String?) -> GSSyncedDirectory](./open%28forcontaineridentifier%29.md)
  Requests an instance of the game-save directory.
- [class GSSyncedDirectoryState](../gssynceddirectorystate.md)
  Represents the state and its associated properties of the directory


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamesave/gssynceddirectory/directorystate)*