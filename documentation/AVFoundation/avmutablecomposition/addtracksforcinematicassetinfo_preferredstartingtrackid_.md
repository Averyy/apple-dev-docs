# addTracksForCinematicAssetInfo:preferredStartingTrackID:

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Adds a group of empty tracks associated with a cinematic asset to a mutable composition.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```objc
- (CNCompositionInfo *) addTracksForCinematicAssetInfo:(CNAssetInfo *) assetInfo preferredStartingTrackID:(CMPersistentTrackID) preferredStartingTrackID;
```

## Return Value

Information about the composition tracks added to the mutable composition. Be sure to call insertTimeRange on the result to specify at least one time range of cinematic asset you’d like in the composition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablecomposition/addtracksforcinematicassetinfo:preferredstartingtrackid:)*