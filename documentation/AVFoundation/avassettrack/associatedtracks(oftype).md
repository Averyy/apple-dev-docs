# associatedTracks(ofType:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Returns an array of associated tracks that have the specified association type.

**Availability**:
- iOS 7.0+ - Deprecated in 16.0
- iPadOS 7.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.9+ - Deprecated in 13.0
- tvOS 9.0+ - Deprecated in 16.0
- watchOS 1.0+ - Deprecated in 9.0

> **Deprecated**: Use [`loadAssociatedTracks(ofType:completionHandler:)`](./loadassociatedtracks%28oftype,completionhandler%29.md) instead.

## Declaration

```swift
func associatedTracks(ofType trackAssociationType: AVAssetTrack.AssociationType) -> [AVAssetTrack]
```

```objc
- (NSArray<AVAssetTrack *> *) associatedTracksOfType:(AVTrackAssociationType) trackAssociationType;
```

## Return Value

An array of tracks matching the specified track association type, or an empty array if none are found.

## Discussion

Apple discourages using this method in iOS 15, tvOS 15, macOS 12, and watchOS 8 or later. Load associated tracks asynchronously using [`loadAssociatedTracks(ofType:completionHandler:)`](./loadassociatedtracks%28oftype,completionhandler%29.md) instead.

You can call this method without blocking the current thread after you’ve loaded the [`availableTrackAssociationTypes`](./availabletrackassociationtypes.md) property.

## Parameters

- `trackAssociationType`: The requested track association type.

## See Also

### Accessing track associations
- [availableTrackAssociationTypes](./availabletrackassociationtypes.md)
  An array of association types that the track uses to associate with other tracks.
- [AVTrackAssociationType](./associationtype.md)
  Constants that define track association types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassettrack/associatedtracks(oftype:))*