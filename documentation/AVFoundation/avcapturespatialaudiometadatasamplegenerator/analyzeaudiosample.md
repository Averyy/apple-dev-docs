# analyzeAudioSample(_:)

**Framework**: AVFoundation  
**Kind**: method

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
func analyzeAudioSample(_ sbuf: CMSampleBuffer) -> OSStatus
```

#### Return Value

Returns noErr if the sample was able to be analyzed.

#### Discussion

Analyzes the audio sample buffer for its contribution to the spatial audio timed metadata value.

All of the spatial audio sample buffer that given to an AVAssetWriter need to be analyzed for the generation of the proper spatial audio timed metadata value.

## Parameters

- `sbuf`: An CMSampleBuffer containing spatial audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturespatialaudiometadatasamplegenerator/analyzeaudiosample(_:))*