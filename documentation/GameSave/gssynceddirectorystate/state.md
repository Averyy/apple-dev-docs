# state

**Framework**: GameSave  
**Kind**: property

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

## See Also

- [enum GSSyncState](gssyncstate.md)
- [var conflictedVersions: [GSSyncedDirectoryVersion]?](gssynceddirectorystate/conflictedversions.md)
  The conflicting versions.
- [var error: (any Error)?](gssynceddirectorystate/error.md)
  The error preventing you from using the directory.
- [var url: URL?](gssynceddirectorystate/url.md)
  The URL of a directory to read and write game-save data in.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamesave/gssynceddirectorystate/state)*