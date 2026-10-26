# spatialAudioMixMetadata

**Framework**: Cinematic  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS

## Declaration

```objc
@property (nonatomic, readonly) NSData * spatialAudioMixMetadata;
```

#### Discussion

The result of audio analysis during recording which contains metadata necessary to properly configure the Audio Mix feature during playback or editing.. Can be used with `AUAudioUnit` instances that support AudioUnitPropertyID `kProperty_SpatialAudioMixMetadata`


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cnassetspatialaudioinfo-57yc5/spatialaudiomixmetadata)*