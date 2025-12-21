# error

**Framework**: GameSave  
**Kind**: property

The error preventing you from using the directory.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var error: (any Error)? { get }
```

#### Discussion

This property’s value is `nil` unless the state is `GSSyncStateError`.

## See Also

- [enum GSSyncState](gssyncstate.md)
- [var state: GSSyncState](gssynceddirectorystate/state.md)
  Specifies the current state of the directory
- [var conflictedVersions: [GSSyncedDirectoryVersion]?](gssynceddirectorystate/conflictedversions.md)
  The conflicting versions.
- [var url: URL?](gssynceddirectorystate/url.md)
  The URL of a directory to read and write game-save data in.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamesave/gssynceddirectorystate/error)*