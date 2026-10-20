# open(forContainerIdentifier:)

**Framework**: GameSave  
**Kind**: method  
**Role**: Type Method

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

```objc
+ (GSSyncedDirectory *) openDirectoryForContainerIdentifier:(NSString *) containerIdentifier;
```

#### Discussion

This method returns immediately, and starts syncing the directory in the background. To wait for syncing to complete, call the [`finishSyncing(completionHandler:)`](./finishsyncing%28completionhandler%29.md) method.

## Parameters

- `containerIdentifier`: The identifier of the directory to request. If you pass `nil`, this method uses the first container identifier listed in the `com.apple.developer.icloud-container-identifiers` entitlements array.

## See Also

### Accessing a directory
- [var directoryState: GSSyncedDirectoryState](./directorystate.md)
  The state of the directory.
- [class GSSyncedDirectoryState](../gssynceddirectorystate.md)
  Represents the state and its associated properties of the directory


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamesave/gssynceddirectory/open(forcontaineridentifier:))*