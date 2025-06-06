# streamDescription

**Framework**: AVFAudio  
**Kind**: property

The audio format properties of a stream of audio data.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var streamDescription: UnsafePointer<AudioStreamBasicDescription> { get }
```

#### Discussion

Returns an [`AudioStreamBasicDescription`](https://developer.apple.com/documentation/CoreAudioTypes/AudioStreamBasicDescription) that you use with lower-level audio APIs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioformat/streamdescription)*