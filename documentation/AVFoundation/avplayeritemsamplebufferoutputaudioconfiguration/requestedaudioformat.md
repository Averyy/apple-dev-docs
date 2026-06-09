# requestedAudioFormat

**Framework**: AVFoundation  
**Kind**: property

Indicates the audio format in which the client prefers to receive the output sample buffers.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
var requestedAudioFormat: CMFormatDescription? { get set }
```

#### Discussion

Must be a PCM format.

The output `CMSampleBuffers'` `CMFormatDescription` may not exactly match this format description, but it will match the parts described in the `AudioStreamBasicDescription`.

Specifying a PCM format is currently required.  In the future it may be optional.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemsamplebufferoutputaudioconfiguration/requestedaudioformat)*