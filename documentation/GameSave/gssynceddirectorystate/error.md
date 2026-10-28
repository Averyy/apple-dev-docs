# error

**Framework**: GameSave  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readonly, nullable) NSError * error;
```

## Discussion

This property’s value is `nil` unless the state is `GSSyncStateError`.

## See Also

### Directory state information
- [enum GSSyncState](../gssyncstate.md)
- [var state: GSSyncState](./state.md)
  Specifies the current state of the directory
- [var conflictedVersions: [GSSyncedDirectoryVersion]?](./conflictedversions.md)
  The conflicting versions.
- [var url: URL?](./url.md)
  The URL of a directory to read and write game-save data in.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamesave/gssynceddirectorystate/error)*