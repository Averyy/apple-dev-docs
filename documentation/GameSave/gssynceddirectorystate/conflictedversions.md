# conflictedVersions

**Framework**: GameSave  
**Kind**: property

The conflicting versions.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var conflictedVersions: [GSSyncedDirectoryVersion]? { get }
```

#### Discussion

If you’re implementing your own conflict resolution, read all of the conflicting versions, and modify one of them to incorporate the state and changes from the others. Then call `GSGameSaveSyncedDirectory/resolveConflictsWithVersion:`, passing that version.

This property’s value is `nil` unless the state is `GSSyncStateConflicted`.

## See Also

- [enum GSSyncState](gssyncstate.md)
- [var state: GSSyncState](gssynceddirectorystate/state.md)
  Specifies the current state of the directory
- [var error: (any Error)?](gssynceddirectorystate/error.md)
  The error preventing you from using the directory.
- [var url: URL?](gssynceddirectorystate/url.md)
  The URL of a directory to read and write game-save data in.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamesave/gssynceddirectorystate/conflictedversions)*