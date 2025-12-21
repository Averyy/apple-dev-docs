# GSSyncedDirectoryVersion

**Framework**: GameSave  
**Kind**: class

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
class GSSyncedDirectoryVersion
```

##### Accessing Saved Game State

- [`url`](gssynceddirectoryversion/url.md)
- [`isLocal`](gssynceddirectoryversion/islocal.md)

##### Comparing Versions

- [`localizedNameOfSavingComputer`](gssynceddirectoryversion/localizednameofsavingcomputer.md)
- [`modifiedDate`](gssynceddirectoryversion/modifieddate.md)

## Topics

### Instance Properties
- [var description: String](gssynceddirectoryversion/description.md)
- [var isLocal: Bool](gssynceddirectoryversion/islocal.md)
  `YES` if the directory version is local; otherwise `NO`.
- [var localizedNameOfSavingComputer: String](gssynceddirectoryversion/localizednameofsavingcomputer.md)
  The localized name of the device that saved this version.
- [var modifiedDate: Date](gssynceddirectoryversion/modifieddate.md)
  The date that this version was last modified.
- [var url: URL](gssynceddirectoryversion/url.md)
  The URL of a directory where you read and write game-save data.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [func resolveConflicts(with: GSSyncedDirectoryVersion)](gssynceddirectory/resolveconflicts(with:).md)
  Indicates that you resolved a conflict.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamesave/gssynceddirectoryversion)*