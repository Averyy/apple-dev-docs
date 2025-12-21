# CNAssetSpatialAudioInfo

**Framework**: Cinematic  
**Kind**: class

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
class CNAssetSpatialAudioInfo
```

## Topics

### Initializers
- [init(asset: AVAsset) async throws](cnassetspatialaudioinfo-7hdev/init(asset:).md)
  Initializes an instance of `CNAssetAudioInfo` for an AVAsset object asynchronously if it meets all requirements. .
### Instance Properties
- [var defaultEffectIntensity: Float32](cnassetspatialaudioinfo-7hdev/defaulteffectintensity.md)
  default effect intensity value as provided by the system. Supported range is [0.0-1.0]
- [var defaultRenderingStyle: CNSpatialAudioRenderingStyle](cnassetspatialaudioinfo-7hdev/defaultrenderingstyle.md)
  default rendering style as provided by the system
- [var defaultSpatialAudioTrack: AVAssetTrack](cnassetspatialaudioinfo-7hdev/defaultspatialaudiotrack.md)
  default `AVAssetTrack` containing Spatial Audio
- [var spatialAudioMixMetadata: Data](cnassetspatialaudioinfo-7hdev/spatialaudiomixmetadata.md)
  The result of audio analysis during recording which contains metadata necessary to properly configure the Audio Mix feature during playback or editing. Can be used with `AUAudioUnit` instances that support AudioUnitPropertyID `kProperty_SpatialAudioMixMetadata`
### Instance Methods
- [func assetReaderOutputSettings(for: CNSpatialAudioContentType) -> Dictionary<String, Any>](cnassetspatialaudioinfo-7hdev/assetreaderoutputsettings(for:).md)
  Returns a dictionary of settings and the source track that should be used to fetch LPCM samples from this track with the effect applied
- [func assetWriterInputSettings(for: CNSpatialAudioContentType) -> Dictionary<String, Any>](cnassetspatialaudioinfo-7hdev/assetwriterinputsettings(for:).md)
  Returns a dictionary of settings that should be used to encode LPCM samples using `AVAssetWriterInput`
- [func audioMix(effectIntensity: Float32, renderingStyle: CNSpatialAudioRenderingStyle) -> AVAudioMix](cnassetspatialaudioinfo-7hdev/audiomix(effectintensity:renderingstyle:).md)
  Returns an instance of `AVAudioMix` encapsulating all spatial audio related data with specified effect intesnsity and rendering style.
### Type Properties
- [static var isSupported: Bool](cnassetspatialaudioinfo-7hdev/issupported.md)
  Indicates whether the current device supports Audio Mix
### Type Methods
- [class func assetContainsSpatialAudio(asset: AVAsset) async -> Bool](cnassetspatialaudioinfo-7hdev/assetcontainsspatialaudio(asset:).md)
  Check if asset meets all the requirements to operate with Spatial Audio and its accompanying effects
- [class func checkIfContainsSpatialAudio(asset: AVAsset, completionHandler: (Bool) -> Void)](cnassetspatialaudioinfo-7hdev/checkifcontainsspatialaudio(asset:completionhandler:).md)
  Check if asset meets all the requirements to operate with Spatial Audio and its accompanying effects


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cnassetspatialaudioinfo-7hdev)*