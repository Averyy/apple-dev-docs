# GameSaveSyncedDirectory.Version

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

### Instance Properties
- [var description: String](gamesavesynceddirectory/version/description.md)
  A textual representation of this instance.
- [var id: URL](gamesavesynceddirectory/version/id-swift.property.md)
  The stable identity of the entity associated with this instance.
- [var isLocal: Bool](gamesavesynceddirectory/version/islocal.md)
  `true` if the directory version is local; otherwise `false`.
- [var localizedNameOfSavingComputer: String](gamesavesynceddirectory/version/localizednameofsavingcomputer.md)
  The localized name of the device that saved this version.
- [var modifiedDate: Date](gamesavesynceddirectory/version/modifieddate.md)
  The date that this version was last modified.
- [var url: URL](gamesavesynceddirectory/version/url.md)
  The URL of a directory where you read and write game-save data.
### Type Aliases
- [GameSaveSyncedDirectory.Version.ID](gamesavesynceddirectory/version/id-swift.typealias.md)
  A type representing the stable identity of the entity associated with an instance.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Identifiable](../Swift/Identifiable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamesave/gamesavesynceddirectory/version)*