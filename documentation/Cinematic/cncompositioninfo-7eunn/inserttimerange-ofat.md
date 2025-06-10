# insertTimeRange(_:of:at:)

**Framework**: Cinematic  
**Kind**: method

Inserts a timeRange of Cinematic source asset into the corresponding tracks of a composition.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```swift
func insertTimeRange(_ timeRange: CMTimeRange, of cinematicAssetInfo: CNAssetInfo, at startTime: CMTime) throws
```

## Parameters

- `timeRange`: The time range where to insert the Cinematic source asset.
- `cinematicAssetInfo`: The asset to insert.
- `startTime`: The starting time where to insert the corresponding tracks of the composition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cncompositioninfo-7eunn/inserttimerange(_:of:at:))*