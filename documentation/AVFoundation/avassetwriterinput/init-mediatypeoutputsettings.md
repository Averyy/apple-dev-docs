# init(mediaType:outputSettings:)

**Framework**: AVFoundation  
**Kind**: init

Creates an input to append sample buffers of the specified type to the output file.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(mediaType: AVMediaType, outputSettings: [String : Any]?)
```

#### Discussion

If you’re appending samples that are already in an acceptable compressed format, pass a value of `nil` for the output settings to pass the buffers to the output unaltered. However, if you’re not writing to a QuickTime movie file, an asset writer only supports passing through a restricted set of media types and subtypes. To pass through media data to files with a type other than [`mov`](avfiletype/mov.md), pass a nonnull format hint using the [`init(mediaType:outputSettings:sourceFormatHint:)`](avassetwriterinput/init(mediatype:outputsettings:sourceformathint:).md) instead.

##### Configuring Audio Settings

You must fully specify the audio settings dictionary when using this initializer, which means you must provide values for the following keys:

- [`AVFormatIDKey`](https://developer.apple.com/documentation/AVFAudio/AVFormatIDKey). The identifier of the audio format. For [`kAudioFormatLinearPCM`](https://developer.apple.com/documentation/CoreAudioTypes/kAudioFormatLinearPCM) format, you must include values for all relevant keys with a `AVLinearPCM` prefix, and for [`kAudioFormatAppleLossless`](https://developer.apple.com/documentation/CoreAudioTypes/kAudioFormatAppleLossless), you must specify a value for [`AVEncoderBitDepthHintKey`](https://developer.apple.com/documentation/AVFAudio/AVEncoderBitDepthHintKey).
- [`AVSampleRateKey`](https://developer.apple.com/documentation/AVFAudio/AVSampleRateKey). The sample rate of the audio. Common values are `44100` and `48000`.
- [`AVNumberOfChannelsKey`](https://developer.apple.com/documentation/AVFAudio/AVNumberOfChannelsKey). If no other channel layout information is available, specifying a value of `1` results in mono output and a value of `2` results in stereo output. If [`AVNumberOfChannelsKey`](https://developer.apple.com/documentation/AVFAudio/AVNumberOfChannelsKey) specifies a channel count greater than `2`, the dictionary must also specify a value for [`AVChannelLayoutKey`](https://developer.apple.com/documentation/AVFAudio/AVChannelLayoutKey).

> **Note**:  The system doesn’t support specifying a value for [`AVSampleRateConverterAudioQualityKey`](https://developer.apple.com/documentation/AVFAudio/AVSampleRateConverterAudioQualityKey) in audio output settings.

##### Configuring Video Settings

A video output settings dictionary must request a compressed video format, which means that the value you specify must follow the rules for compressed video output.

You must fully specify the video settings dictionary when using this initializer, which means you must provide values for the following keys [`AVVideoCodecKey`](avvideocodeckey.md), [`AVVideoWidthKey`](avvideowidthkey.md), [`AVVideoHeightKey`](avvideoheightkey.md).

> **Note**:  Specifying a [`AVVideoScalingModeKey`](avvideoscalingmodekey.md) value of [`AVVideoScalingModeFit`](avvideoscalingmodefit.md) results in an error.

## Parameters

- `mediaType`: The media type of the samples the input accepts.
- `outputSettings`: The settings to use for encoding the media you append to the output. Create an output settings dictionary manually, or use   to create preset-based settings.

## See Also

- [init(mediaType: AVMediaType, outputSettings: [String : Any]?, sourceFormatHint: CMFormatDescription?)](avassetwriterinput/init(mediatype:outputsettings:sourceformathint:).md)
  Creates an input that appends sample buffers of the specified type and format hint to the output file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/init(mediatype:outputsettings:))*