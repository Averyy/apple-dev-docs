# state

**Framework**: GameSave  
**Kind**: property  
**Role**: Instance Property

Specifies the current state of the directory

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var state: GSSyncState { get }
```

```objc
@property (readonly) GSSyncState state;
```

## See Also

### Directory state information
- [enum GSSyncState](../gssyncstate.md)
- [var conflictedVersions: [GSSyncedDirectoryVersion]?](./conflictedversions.md)
  The conflicting versions.
- [var error: (any Error)?](./error.md)
  The error preventing you from using the directory.
- [var url: URL?](./url.md)
  The URL of a directory to read and write game-save data in.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamesave/gssynceddirectorystate/state)*