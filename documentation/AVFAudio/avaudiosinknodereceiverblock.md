# AVAudioSinkNodeReceiverBlock

**Framework**: AVFAudio  
**Kind**: typealias

A block that receives audio data from an audio sink node.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
typealias AVAudioSinkNodeReceiverBlock = (UnsafePointer<AudioTimeStamp>, AVAudioFrameCount, UnsafePointer<AudioBufferList>) -> OSStatus
```

#### Return Value

An `OSStatus` result code. When an error occurs, consider the audio data invalid.

## Parameters

- `timestamp`: The time the input data renders.
- `frameCount`: The number of sample frames of input the engine provides.
- `inputData`: The input audio data.

## See Also

- [init(receiverBlock: AVAudioSinkNodeReceiverBlock)](avaudiosinknode/init(receiverblock:).md)
  Creates an audio sink node with a block that receives audio data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosinknodereceiverblock)*