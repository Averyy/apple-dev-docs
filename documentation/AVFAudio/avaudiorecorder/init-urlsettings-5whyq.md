# init(url:settings:)

**Framework**: AVFAudio  
**Kind**: init

Creates an audio recorder with settings.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
init(url: URL, settings: [String : Any]) throws
```

#### Return Value

A new audio recorder, or [`nil`](https://developer.apple.com/documentation/objectivec/nil-227m0) if an error occurred.

#### Discussion

The system supports the following keys when defining the format settings:

| Key | Supported Values |
| --- | --- |
| [`AVFormatIDKey`](avformatidkey.md) | [`kAudioFormatLinearPCM`](https://developer.apple.com/documentation/coreaudiotypes/kaudioformatlinearpcm) ![None](/images/com.apple.avfaudio/spacer.png) [`kAudioFormatMPEG4AAC`](https://developer.apple.com/documentation/coreaudiotypes/kaudioformatmpeg4aac) ![None](/images/com.apple.avfaudio/spacer.png) [`kAudioFormatAppleLossless`](https://developer.apple.com/documentation/coreaudiotypes/kaudioformatapplelossless) ![None](/images/com.apple.avfaudio/spacer.png) [`kAudioFormatAppleIMA4`](https://developer.apple.com/documentation/coreaudiotypes/kaudioformatappleima4) ![None](/images/com.apple.avfaudio/spacer.png) [`kAudioFormatiLBC`](https://developer.apple.com/documentation/coreaudiotypes/kaudioformatilbc) ![None](/images/com.apple.avfaudio/spacer.png) [`kAudioFormatULaw`](https://developer.apple.com/documentation/coreaudiotypes/kaudioformatulaw) |
| [`AVSampleRateKey`](avsampleratekey.md) | 8 kHz to 192 kHz |
| [`AVNumberOfChannelsKey`](avnumberofchannelskey.md) | 1 to 64 |

The system supports additional configuration options based on your selected audio format. See [`Linear PCM format settings`](https://developer.apple.com/documentation/avfoundation/linear-pcm-format-settings) for information about customizing Linear PCM formats and [`Encoder settings`](https://developer.apple.com/documentation/avfoundation/encoder-settings) for compressed formats.

## Parameters

- `url`: The file system location to record to.
- `settings`: The audio settings to use for the recording.

## See Also

- [init(url: URL, format: AVAudioFormat) throws](avaudiorecorder/init(url:format:)-7herw.md)
  Creates an audio recorder with an audio format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiorecorder/init(url:settings:)-5whyq)*