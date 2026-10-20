# conflictedVersions

**Framework**: GameSave  
**Kind**: property  
**Role**: Instance Property

The conflicting versions.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var conflictedVersions: [GSSyncedDirectoryVersion]? { get }
```

```objc
@property (readonly, nullable) NSArray<GSSyncedDirectoryVersion *> * conflictedVersions;
```

#### Discussion

If you’re implementing your own conflict resolution, read all of the conflicting versions, and modify one of them to incorporate the state and changes from the others. Then call [`resolveConflicts(with:)`](../gssynceddirectory/resolveconflicts%28with%29.md), passing that version.

This property’s value is `nil` unless the state is `GSSyncStateConflicted`.

## See Also

### Directory state information
- [enum GSSyncState](../gssyncstate.md)
- [var state: GSSyncState](./state.md)
  Specifies the current state of the directory
- [var error: (any Error)?](./error.md)
  The error preventing you from using the directory.
- [var url: URL?](./url.md)
  The URL of a directory to read and write game-save data in.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamesave/gssynceddirectorystate/conflictedversions)*