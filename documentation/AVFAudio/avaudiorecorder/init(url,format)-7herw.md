# init(url:format:)

**Framework**: AVFAudio  
**Kind**: init  
**Role**: Initializer

Creates an audio recorder with an audio format.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
init(url: URL, format: AVAudioFormat) throws
```

```objc
- (instancetype) initWithURL:(NSURL *) url format:(AVAudioFormat *) format error:(NSError **) outError;
```

#### Return Value

A new audio recorder, or [`nil`](../../ObjectiveC/nil-227m0.md) if an error occurred.

## Parameters

- `url`: The file system location to record to.
- `format`: The audio format to use for the recording.

## See Also

### Creating an audio recorder
- [init(url: URL, settings: [String : Any]) throws](./init%28url,settings%29-5whyq.md)
  Creates an audio recorder with settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiorecorder/init(url:format:)-7herw)*