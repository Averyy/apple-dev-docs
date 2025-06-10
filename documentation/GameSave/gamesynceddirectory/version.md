# GameSyncedDirectory.Version

**Framework**: GameSave  
**Kind**: class

A representation of a version of the directory.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
class Version
```

#### Overview

Used to describe the conflicted or local versions of a directory in case there are conflicts.

## Topics

### Accessing saved game state
- [var url: URL](gamesynceddirectory/version/url.md)
  The URL of a directory where you read and write game-save data.
### Comparing versions
- [var localizedNameOfSavingComputer: String](gamesynceddirectory/version/localizednameofsavingcomputer.md)
  The localized name of the device that saved this version.
- [var modifiedDate: Date](gamesynceddirectory/version/modifieddate.md)
  The date that this version was last modified.
### Describing versions
- [GameSyncedDirectory.Version.ID](gamesynceddirectory/version/id-swift.typealias.md)
  A type representing the stable identity of the entity associated with an instance.
- [var id: URL](gamesynceddirectory/version/id-swift.property.md)
  The stable identity of the entity associated with this instance.
- [var description: String](gamesynceddirectory/version/description.md)
  A textual representation of this instance.
### Instance Properties
- [var isLocal: Bool](gamesynceddirectory/version/islocal.md)
  `true` if the directory version is local; otherwise `false`.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Identifiable](../Swift/Identifiable.md)

## See Also

- [func resolveConflicts(with: GameSyncedDirectory.Version)](gamesynceddirectory/resolveconflicts(with:).md)
  Indicates that you resolved a conflict.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamesave/gamesynceddirectory/version)*