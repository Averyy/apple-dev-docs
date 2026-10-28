# init(url:settings:)

**Framework**: AVFAudio  
**Kind**: init  
**Role**: Initializer

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

```objc
- (instancetype) initWithURL:(NSURL *) url settings:(NSDictionary<NSString *,id> *) settings error:(NSError **) outError;
```

## Return Value

A new audio recorder, or [`nil`](../../ObjectiveC/nil-227m0.md) if an error occurred.

## Discussion

The system supports the following keys when defining the format settings:

| Key | Supported Values |
| --- | --- |
| [`AVFormatIDKey`](../avformatidkey.md) | [`kAudioFormatLinearPCM`](../../CoreAudioTypes/kaudioformatlinearpcm.md) ![](https://developer.apple.com/tutorials/images/com.apple.avfaudio/spacer.png) [`kAudioFormatMPEG4AAC`](../../CoreAudioTypes/kaudioformatmpeg4aac.md) ![](https://developer.apple.com/tutorials/images/com.apple.avfaudio/spacer.png) [`kAudioFormatAppleLossless`](../../CoreAudioTypes/kaudioformatapplelossless.md) ![](https://developer.apple.com/tutorials/images/com.apple.avfaudio/spacer.png) [`kAudioFormatAppleIMA4`](../../CoreAudioTypes/kaudioformatappleima4.md) ![](https://developer.apple.com/tutorials/images/com.apple.avfaudio/spacer.png) [`kAudioFormatiLBC`](../../CoreAudioTypes/kaudioformatilbc.md) ![](https://developer.apple.com/tutorials/images/com.apple.avfaudio/spacer.png) [`kAudioFormatULaw`](../../CoreAudioTypes/kaudioformatulaw.md) |
| [`AVSampleRateKey`](../avsampleratekey.md) | 8 kHz to 192 kHz |
| [`AVNumberOfChannelsKey`](../avnumberofchannelskey.md) | 1 to 64 |

The system supports additional configuration options based on your selected audio format. See [Linear PCM format settings](../../AVFoundation/linear-pcm-format-settings.md) for information about customizing Linear PCM formats and [Encoder settings](../../AVFoundation/encoder-settings.md) for compressed formats.

## Parameters

- `url`: The file system location to record to.
- `settings`: The audio settings to use for the recording.

## See Also

### Creating an audio recorder
- [init(url: URL, format: AVAudioFormat) throws](./init%28url,format%29-7herw.md)
  Creates an audio recorder with an audio format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiorecorder/init(url:settings:)-5whyq)*