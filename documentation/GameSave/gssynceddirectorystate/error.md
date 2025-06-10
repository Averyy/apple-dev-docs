# error

**Framework**: GameSave  
**Kind**: property

The error preventing you from using the directory.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

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