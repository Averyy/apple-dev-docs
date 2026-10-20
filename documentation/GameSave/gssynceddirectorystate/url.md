# url

**Framework**: GameSave  
**Kind**: property  
**Role**: Instance Property

The URL of a directory to read and write game-save data in.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var url: URL? { get }
```

```objc
@property (readonly, nullable) NSURL * url;
```

#### Discussion

This property’s value is `nil` unless the state is `GSSyncStateReady`, `GSSyncStateOffline`, or `GSSyncStateLocal`.

## See Also

### Directory state information
- [enum GSSyncState](../gssyncstate.md)
- [var state: GSSyncState](./state.md)
  Specifies the current state of the directory
- [var conflictedVersions: [GSSyncedDirectoryVersion]?](./conflictedversions.md)
  The conflicting versions.
- [var error: (any Error)?](./error.md)
  The error preventing you from using the directory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamesave/gssynceddirectorystate/url)*