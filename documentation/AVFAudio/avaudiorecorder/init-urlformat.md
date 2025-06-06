# init(url:format:)

**Framework**: AVFAudio  
**Kind**: init

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

#### Return Value

A new audio recorder, or [`nil`](https://developer.apple.com/documentation/ObjectiveC/nil-227m0) if an error occurred.

## Parameters

- `url`: The file system location to record to.
- `format`: The audio format to use for the recording.

## See Also

- [init(url: URL, settings: [String : Any]) throws](avaudiorecorder/init(url:settings:).md)
  Creates an audio recorder with settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiorecorder/init(url:format:))*