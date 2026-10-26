# assetReaderAudioMixOutputWithAudioTracks:audioSettings:

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Type Method

Creates an object that reads mixed audio from the specified audio tracks.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```objc
+ (instancetype) assetReaderAudioMixOutputWithAudioTracks:(NSArray<AVAssetTrack *> *) audioTracks audioSettings:(NSDictionary<NSString *,id> *) audioSettings;
```

#### Return Value

A new audio mix output, or `nil` if initialization fails.

## Parameters

- `audioTracks`: An array of track objects of type [`audio`](../avmediatype/audio.md) from which to source the sample buffers to mix.
- `audioSettings`: Optional audio settings to use for audio output. Pass `nil` to receive the decoded samples in an uncompressed format. To determine the specific format, examine the value of the sample buffer’s [`formatDescription`](../../CoreMedia/cmsamplebuffer/formatdescription.md) property.

  For non-`nil` audio settings, the dictionary must contain values for the [Linear PCM format settings](../linear-pcm-format-settings.md) keys. The output doesn’t support the [`AVSampleRateConverterAudioQualityKey`](../../AVFAudio/avsamplerateconverteraudioqualitykey.md) constant.

## See Also

### Creating an audio mix output
- [init(audioTracks: [AVAssetTrack], audioSettings: [String : Any]?)](./init%28audiotracks,audiosettings%29.md)
  Creates an object that reads mixed audio from the specified audio tracks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreaderaudiomixoutput/assetreaderaudiomixoutputwithaudiotracks:audiosettings:)*