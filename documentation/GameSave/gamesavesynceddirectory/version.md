# GameSaveSyncedDirectory.Version

**Framework**: GameSave  
**Kind**: class

A representation of a version of the directory.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
class Version
```

#### Overview

Used to describe the conflicted or local versions of a directory in case there are conflicts.

## Topics

### Accessing saved game state
- [var url: URL](gamesavesynceddirectory/version/url.md)
  The URL of a directory where you read and write game-save data.
- [var isLocal: Bool](gamesavesynceddirectory/version/islocal.md)
  `true` if the directory version is local; otherwise `false`.
### Comparing versions
- [var localizedNameOfSavingComputer: String](gamesavesynceddirectory/version/localizednameofsavingcomputer.md)
  The localized name of the device that saved this version.
- [var modifiedDate: Date](gamesavesynceddirectory/version/modifieddate.md)
  The date that this version was last modified.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Identifiable](../Swift/Identifiable.md)

## See Also

- [func resolveConflicts(with: GameSaveSyncedDirectory.Version)](gamesavesynceddirectory/resolveconflicts(with:).md)
  Indicates that you resolved a conflict.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamesave/gamesavesynceddirectory/version)*