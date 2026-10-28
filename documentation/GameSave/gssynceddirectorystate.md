# GSSyncedDirectoryState

**Framework**: GameSave  
**Kind**: class  
**Role**: Class

Represents the state and its associated properties of the directory

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
class GSSyncedDirectoryState
```

```objc
@interface GSSyncedDirectoryState : NSObject
```

## Overview

Use the [`state`](./gssynceddirectorystate/state.md) property to determine the validity of the other properties

## Topics

### Directory state information
- [enum GSSyncState](./gssyncstate.md)
- [var state: GSSyncState](./gssynceddirectorystate/state.md)
  Specifies the current state of the directory
- [var conflictedVersions: [GSSyncedDirectoryVersion]?](./gssynceddirectorystate/conflictedversions.md)
  The conflicting versions.
- [var error: (any Error)?](./gssynceddirectorystate/error.md)
  The error preventing you from using the directory.
- [var url: URL?](./gssynceddirectorystate/url.md)
  The URL of a directory to read and write game-save data in.

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

### Accessing a directory
- [class func open(forContainerIdentifier: String?) -> GSSyncedDirectory](./gssynceddirectory/open%28forcontaineridentifier%29.md)
  Requests an instance of the game-save directory.
- [var directoryState: GSSyncedDirectoryState](./gssynceddirectory/directorystate.md)
  The state of the directory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamesave/gssynceddirectorystate)*