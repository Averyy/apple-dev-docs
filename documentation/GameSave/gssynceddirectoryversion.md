# GSSyncedDirectoryVersion

**Framework**: GameSave  
**Kind**: class  
**Role**: Class

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

```objc
@interface GSSyncedDirectoryVersion : NSObject
```

##### Accessing saved game state

- [`url`](./gssynceddirectoryversion/url.md)
- [`isLocal`](./gssynceddirectoryversion/islocal.md)

##### Comparing versions

- [`localizedNameOfSavingComputer`](./gssynceddirectoryversion/localizednameofsavingcomputer.md)
- [`modifiedDate`](./gssynceddirectoryversion/modifieddate.md)

## Topics

### Instance Properties
- [var description: String](./gssynceddirectoryversion/description.md)
- [var isLocal: Bool](./gssynceddirectoryversion/islocal.md)
  `YES` if the directory version is local; otherwise `NO`.
- [var localizedNameOfSavingComputer: String](./gssynceddirectoryversion/localizednameofsavingcomputer.md)
  The localized name of the device that saved this version.
- [var modifiedDate: Date](./gssynceddirectoryversion/modifieddate.md)
  The date that this version was last modified.
- [var url: URL](./gssynceddirectoryversion/url.md)
  The URL of a directory where you read and write game-save data.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Resolving conflicts
- [func resolveConflicts(with: GSSyncedDirectoryVersion)](./gssynceddirectory/resolveconflicts%28with%29.md)
  Indicates that you resolved a conflict.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamesave/gssynceddirectoryversion)*