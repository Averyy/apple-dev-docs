# GSSyncedDirectoryState

**Framework**: GameSave  
**Kind**: class

Represents the state and its associated properties of the directory

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
class GSSyncedDirectoryState
```

#### Overview

Use the [`state`](gssynceddirectorystate/state.md) property to determine the validity of the other properties

## Topics

### Directory state information
- [enum GSSyncState](gssyncstate.md)
- [var state: GSSyncState](gssynceddirectorystate/state.md)
  Specifies the current state of the directory
- [var conflictedVersions: [GSSyncedDirectoryVersion]?](gssynceddirectorystate/conflictedversions.md)
  The conflicting versions.
- [var error: (any Error)?](gssynceddirectorystate/error.md)
  The error preventing you from using the directory.
- [var url: URL?](gssynceddirectorystate/url.md)
  The URL of a directory to read and write game-save data in.

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

- [class func open(forContainerIdentifier: String?) -> GSSyncedDirectory](gssynceddirectory/open(forcontaineridentifier:).md)
  Requests an instance of the game-save directory.
- [var directoryState: GSSyncedDirectoryState](gssynceddirectory/directorystate.md)
  The state of the directory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamesave/gssynceddirectorystate)*