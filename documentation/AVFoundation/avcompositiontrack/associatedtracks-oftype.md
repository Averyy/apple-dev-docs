# associatedTracks(ofType:)

**Framework**: AVFoundation  
**Kind**: method

Returns an array of associated tracks that have the specified association type.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func associatedTracks(ofType trackAssociationType: AVAssetTrack.AssociationType) -> [AVAssetTrack]
```

#### Return Value

An array of tracks matching the specified track association type, or an empty array if none are found.

#### Discussion

Apple discourages using this method in iOS 15, tvOS 15, macOS 12, and watchOS 8 or later. Load associated tracks asynchronously using [`loadAssociatedTracks(ofType:completionHandler:)`](avassettrack/loadassociatedtracks(oftype:completionhandler:).md) instead.

You can call this method without blocking the current thread after you’ve loaded the [`availableTrackAssociationTypes`](avassettrack/availabletrackassociationtypes.md) property.

## Parameters

- `trackAssociationType`: The requested track association type.

## See Also

- [var availableTrackAssociationTypes: [AVAssetTrack.AssociationType]](avcompositiontrack/availabletrackassociationtypes.md)
  An array of association types that the track uses to associate with other tracks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcompositiontrack/associatedtracks(oftype:))*