# unusedTrackID()

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Returns an identifier that no other tracks in the asset use.

**Availability**:
- iOS 4.0+ - Deprecated in 16.0
- iPadOS 4.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.7+ - Deprecated in 13.0
- tvOS 9.0+ - Deprecated in 16.0
- watchOS 1.0+ - Deprecated in 9.0

> **Deprecated**: Use [`findUnusedTrackID(completionHandler:)`](./findunusedtrackid%28completionhandler%29.md) instead.

## Declaration

```swift
func unusedTrackID() -> CMPersistentTrackID
```

```objc
- (CMPersistentTrackID) unusedTrackID;
```

## Return Value

An unused [`CMPersistentTrackID`](../../CoreMedia/cmpersistenttrackid.md) value.

## See Also

### Accessing tracks
- [tracks](./tracks.md)
  The tracks an asset contains.
- [- trackWithTrackID:](./track%28withtrackid%29.md)
  Returns a track that contains the specified identifier.
- [- tracksWithMediaType:](./tracks%28withmediatype%29.md)
  Returns tracks that contain media of a specified type.
- [- tracksWithMediaCharacteristic:](./tracks%28withmediacharacteristic%29.md)
  Returns an array of asset tracks matching the specified media characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasset/unusedtrackid())*