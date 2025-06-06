# loadAssociatedTracks(ofType:completionHandler:)

**Framework**: AVFoundation  
**Kind**: method

Loads associated tracks that have the specified association type.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
func loadAssociatedTracks(ofType trackAssociationType: AVAssetTrack.AssociationType) async throws -> [AVAssetTrack]
```

## Parameters

- `trackAssociationType`: The track association type to load tracks for.
- `completionHandler`: A callback that the system invokes after it finishes the loading request. It passes the completion handler the following parameters:

## See Also

- [static var availableTrackAssociationTypes: AVAsyncProperty<Root, [AVAssetTrack.AssociationType]>](avpartialasyncproperty/availabletrackassociationtypes.md)
  An array of association types that the track uses to associate with other tracks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassettrack/loadassociatedtracks(oftype:completionhandler:))*