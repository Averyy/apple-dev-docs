# init(audioTracks:audioSettings:)

**Framework**: AVFoundation  
**Kind**: init

Creates an object that reads mixed audio from the specified audio tracks.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init(audioTracks: [AVAssetTrack], audioSettings: [String : Any]?)
```

## Parameters

- `audioTracks`: An array of track objects of type [`audio`](avmediatype/audio.md) from which to source the sample buffers to mix.
- `audioSettings`: Optional audio settings to use for audio output. Pass `nil` to receive the decoded samples in an uncompressed format. To determine the specific format, examine the value of the sample buffer’s [`formatDescription`](https://developer.apple.com/documentation/coremedia/cmsamplebuffer/formatdescription) property. For non-`nil` audio settings, the dictionary must contain values for the [`Linear PCM format settings`](linear-pcm-format-settings.md) keys. The output doesn’t support the [`AVSampleRateConverterAudioQualityKey`](https://developer.apple.com/documentation/avfaudio/avsamplerateconverteraudioqualitykey) constant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreaderaudiomixoutput/init(audiotracks:audiosettings:))*