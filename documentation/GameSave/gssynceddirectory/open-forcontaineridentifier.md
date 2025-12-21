# open(forContainerIdentifier:)

**Framework**: GameSave  
**Kind**: method

Requests an instance of the game-save directory.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
class func open(forContainerIdentifier containerIdentifier: String?) -> GSSyncedDirectory
```

#### Discussion

This method returns immediately, and starts syncing the directory in the background. To wait for syncing to complete, call the [`finishSyncing(completionHandler:)`](gssynceddirectory/finishsyncing(completionhandler:).md) method.

## Parameters

- `containerIdentifier`: The identifier of the directory to request.   If you pass  , this method uses the first container identifier   listed in the   entitlements array.

## See Also

- [var directoryState: GSSyncedDirectoryState](gssynceddirectory/directorystate.md)
  The state of the directory.
- [class GSSyncedDirectoryState](gssynceddirectorystate.md)
  Represents the state and its associated properties of the directory


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamesave/gssynceddirectory/open(forcontaineridentifier:))*