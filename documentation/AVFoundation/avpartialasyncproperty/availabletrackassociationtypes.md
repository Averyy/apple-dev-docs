# availableTrackAssociationTypes

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

An array of association types that the track uses to associate with other tracks.

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
static var availableTrackAssociationTypes: AVAsyncProperty<Root, [AVAssetTrack.AssociationType]> { get }
```

Available when `Root` inherits `AVAssetTrack`.

#### Discussion

Use the [`load(_:isolation:)`](../avasynchronouskeyvalueloading/load%28_,isolation%29.md) method to retrieve the property value.

## See Also

### Loading track associations
- [func loadAssociatedTracks(ofType: AVAssetTrack.AssociationType, completionHandler: ([AVAssetTrack]?, (any Error)?) -> Void)](../avassettrack/loadassociatedtracks%28oftype,completionhandler%29.md)
  Loads associated tracks that have the specified association type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/availabletrackassociationtypes)*