# AppAssetLibraryRefDatum.Attributes.VideoSpecs

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

**Availability**:
- App Store Connect API 3.6+

## Declaration

```
object AppAssetLibraryRefDatum.Attributes.VideoSpecs
```

## Topics

### Dictionaries
- [object AppAssetLibraryRefDatum.Attributes.VideoSpecs.Dimensions](./videospecs-data.dictionary/dimensions-data.dictionary.md)
- [object AppAssetLibraryRefDatum.Attributes.VideoSpecs.Duration](./videospecs-data.dictionary/duration-data.dictionary.md)
- [object AppAssetLibraryRefDatum.Attributes.VideoSpecs.FrameRates](./videospecs-data.dictionary/framerates-data.dictionary.md)

## Properties

- `aspectRatio` (string)
- `audioRequired` (boolean)
- `compatiblePlacementTypes` ([AppAssetLibraryPlacementType])
- `dimensions` (AppAssetLibraryRefDatum.Attributes.VideoSpecs.Dimensions)
- `duration` (AppAssetLibraryRefDatum.Attributes.VideoSpecs.Duration)
- `fileExtensions` ([string])
- `frameRates` ([AppAssetLibraryRefDatum.Attributes.VideoSpecs.FrameRates])
- `maxFileSize` (int64): **Minimum**: `1`; **Maximum**: `9007199254740991`
- `mimeTypes` ([string])
- `shortName` (string)
- `specId` (string)
- `universalAsset` (boolean)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appassetlibraryrefdatum/attributes-data.dictionary/videospecs-data.dictionary)*