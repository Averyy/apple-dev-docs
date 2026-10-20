# resolveConflicts(with:)

**Framework**: GameSave  
**Kind**: method

Indicates that you resolved a conflict.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func resolveConflicts(with version: GameSaveSyncedDirectory.Version)
```

#### Discussion

If you’re implementing your own conflict resolution, read all of the conflicting versions, and modify one of them to incorporate the state and changes from the others. Then call this method, passing that version.

Call this method only when the directory is in the [`GameSaveSyncedDirectory.State.conflicted(versions:)`](gamesavesynceddirectory/state-swift.enum/conflicted(versions:).md) state.

## Parameters

- `version`: The version to use.

## See Also

- [GameSaveSyncedDirectory.Version](gamesavesynceddirectory/version.md)
  A representation of a version of the directory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamesave/gamesavesynceddirectory/resolveconflicts(with:))*