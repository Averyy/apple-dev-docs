# spatialAudioMixMetadata

**Framework**: Cinematic  
**Kind**: property

The result of audio analysis during recording which contains metadata necessary to properly configure the Audio Mix feature during playback or editing. Can be used with `AUAudioUnit` instances that support AudioUnitPropertyID `kProperty_SpatialAudioMixMetadata`

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)

## Declaration

```swift
var spatialAudioMixMetadata: Data { get }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cnassetspatialaudioinfo-7hdev/spatialaudiomixmetadata)*