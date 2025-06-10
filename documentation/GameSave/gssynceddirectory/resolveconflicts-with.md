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
func resolveConflicts(with version: GSSyncedDirectoryVersion)
```

#### Discussion

If you’re implementing your own conflict resolution, read all of the conflicting versions, and modify one of them to incorporate the state and changes from the others. Then call this method, passing that version.

Call this method only when the directory is in the [`GSSyncState.conflicted`](gssyncstate/conflicted.md) state.

## Parameters

- `version`: The version to use.

## See Also

- [class GSSyncedDirectoryVersion](gssynceddirectoryversion.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamesave/gssynceddirectory/resolveconflicts(with:))*