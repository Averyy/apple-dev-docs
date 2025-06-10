# resolveConflicts(with:)

**Framework**: GameSave  
**Kind**: method

Indicates that you resolved a conflict.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func resolveConflicts(with version: GameSyncedDirectory.Version)
```

#### Discussion

If you’re implementing your own conflict resolution, read all of the conflicting versions, and modify one of them to incorporate the state and changes from the others. Then call this method, passing that version.

Call this method only when the directory is in the [`GameSyncedDirectory.State.conflicted(versions:)`](gamesynceddirectory/state-swift.enum/conflicted(versions:).md) state.

## Parameters

- `version`: The version to use.

## See Also

- [GameSyncedDirectory.Version](gamesynceddirectory/version.md)
  A representation of a version of the directory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamesave/gamesynceddirectory/resolveconflicts(with:))*