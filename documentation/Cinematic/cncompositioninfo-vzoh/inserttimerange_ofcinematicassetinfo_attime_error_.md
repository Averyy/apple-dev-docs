# insertTimeRange:ofCinematicAssetInfo:atTime:error:

**Framework**: Cinematic  
**Kind**: method  
**Role**: Instance Method

Inserts a time range of Cinematic source asset into the corresponding tracks of a composition.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```objc
- (BOOL) insertTimeRange:(CMTimeRange) timeRange ofCinematicAssetInfo:(CNAssetInfo *) assetInfo atTime:(CMTime) startTime error:(NSError **) outError;
```

## Parameters

- `timeRange`: The time range where to insert the Cinematic source asset.
- `assetInfo`: The asset to insert.
- `startTime`: The starting time where to insert the corresponding tracks of the composition.
- `outError`: The error result, if any.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cncompositioninfo-vzoh/inserttimerange:ofcinematicassetinfo:attime:error:)*