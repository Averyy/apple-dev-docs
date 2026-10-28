# assetReaderOutputSettingsForContentType:

**Framework**: Cinematic  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS

## Declaration

```objc
- (NSDictionary<NSString *,id> *) assetReaderOutputSettingsForContentType:(CNSpatialAudioContentType) contentType;
```

## Discussion

Returns a dictionary of settings and the source track that should be used to fetch LPCM samples from this track with the effect applied

Use the returned NSDictionary with the `defaulSpatialAudioTrack` to initialize an instance of `AVAssetReaderAudioMixOutput`


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cnassetspatialaudioinfo-57yc5/assetreaderoutputsettingsforcontenttype:)*