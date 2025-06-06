# removeTap(onBus:)

**Framework**: AVFAudio  
**Kind**: method

Removes an audio tap on a bus you specify.

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
func removeTap(onBus bus: AVAudioNodeBus)
```

## Parameters

- `bus`: The node output bus with the tap to remove.

## See Also

- [func installTap(onBus: AVAudioNodeBus, bufferSize: AVAudioFrameCount, format: AVAudioFormat?, block: AVAudioNodeTapBlock)](avaudionode/installtap(onbus:buffersize:format:block:).md)
  Installs an audio tap on a bus you specify to record, monitor, and observe the output of the node.
- [typealias AVAudioNodeTapBlock](avaudionodetapblock.md)
  The block that receives copies of the output of an audio node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudionode/removetap(onbus:))*