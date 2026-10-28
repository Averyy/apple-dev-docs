# GameSaveSyncedDirectory.Version

**Framework**: GameSave  
**Kind**: class  
**Role**: Class

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

## Overview

Used to describe the conflicted or local versions of a directory in case there are conflicts.

## Topics

### Accessing saved game state
- [var url: URL](./version/url.md)
  The URL of a directory where you read and write game-save data.
- [var isLocal: Bool](./version/islocal.md)
  `true` if the directory version is local; otherwise `false`.
### Comparing versions
- [var localizedNameOfSavingComputer: String](./version/localizednameofsavingcomputer.md)
  The localized name of the device that saved this version.
- [var modifiedDate: Date](./version/modifieddate.md)
  The date that this version was last modified.

## Relationships

### Conforms To
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Identifiable](../../Swift/identifiable.md)

## See Also

### Resolving conflicts
- [func resolveConflicts(with: GameSaveSyncedDirectory.Version)](./resolveconflicts%28with%29.md)
  Indicates that you resolved a conflict.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamesave/gamesavesynceddirectory/version)*