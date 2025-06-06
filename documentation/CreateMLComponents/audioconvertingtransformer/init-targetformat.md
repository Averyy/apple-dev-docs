# init(targetFormat:)

**Framework**: Create ML Components  
**Kind**: init

Creates an audio conversion transformer to convert the format of the buffers.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
init(targetFormat: AVAudioFormat)
```

#### Discussion

- Precondition The `targetFormat` must have an AVAudioPCMFormat as its common format type.

## Parameters

- `targetFormat`: The desired audio format for the output buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/audioconvertingtransformer/init(targetformat:))*