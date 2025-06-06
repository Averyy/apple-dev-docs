# availableTrackAssociationTypes

**Framework**: AVFoundation  
**Kind**: property

An array of association types that the track uses to associate with other tracks.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static var availableTrackAssociationTypes: AVAsyncProperty<Root, [AVAssetTrack.AssociationType]> { get }
```

#### Discussion

Use the [`load(_:)`](avasynchronouskeyvalueloading/load(_:).md) method to retrieve the property value.

## See Also

- [func loadAssociatedTracks(ofType: AVAssetTrack.AssociationType, completionHandler: ([AVAssetTrack]?, (any Error)?) -> Void)](avassettrack/loadassociatedtracks(oftype:completionhandler:).md)
  Loads associated tracks that have the specified association type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/availabletrackassociationtypes)*