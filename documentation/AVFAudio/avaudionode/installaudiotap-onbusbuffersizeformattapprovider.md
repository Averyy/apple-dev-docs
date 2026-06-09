# installAudioTap(onBus:bufferSize:format:tapProvider:)

**Framework**: AVFAudio  
**Kind**: method

Install a tap on a bus using a sendable block

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
func installAudioTap(onBus bus: AVAudioNodeBus, bufferSize: AVAudioFrameCount, format: AVAudioFormat?, tapProvider: @escaping @Sendable (AVReadOnlyAudioPCMBuffer, AVAudioTime) -> Void) throws
```

#### Discussion

This method installs a tap that receives read-only buffers safe for concurrent use. The tap block is sendable and can be safely called from any isolation domain.

Only one tap may be installed on any bus. Taps may be safely installed and removed while the engine is running.

## Parameters

- `bus`: The node output bus to which to attach the tap
- `bufferSize`: The requested size of incoming buffers in sample frames. Supported range is [100, 400] ms.
- `format`: If non-nil, attempts to apply this as the format of the specified output bus
- `tapProvider`: A sendable closure to be called with read-only audio buffers

## See Also

- [func installTap(onBus: AVAudioNodeBus, bufferSize: AVAudioFrameCount, format: AVAudioFormat?, block: AVAudioNodeTapBlock)](avaudionode/installtap(onbus:buffersize:format:block:).md)
  Installs an audio tap on a bus you specify to record, monitor, and observe the output of the node.
- [func removeTap(onBus: AVAudioNodeBus)](avaudionode/removetap(onbus:).md)
  Removes an audio tap on a bus you specify.
- [typealias AVAudioNodeTapBlock](avaudionodetapblock.md)
  The block that receives copies of the output of an audio node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudionode/installaudiotap(onbus:buffersize:format:tapprovider:))*