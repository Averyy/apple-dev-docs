# installTap(onBus:bufferSize:format:block:)

**Framework**: AVFAudio  
**Kind**: method

Installs an audio tap on a bus you specify to record, monitor, and observe the output of the node.

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
func installTap(onBus bus: AVAudioNodeBus, bufferSize: AVAudioFrameCount, format: AVAudioFormat?, block tapBlock: @escaping AVAudioNodeTapBlock)
```

#### Discussion

You can install and remove taps while the engine is in a running state. You can install only one tap on any bus.

```objc
AVAudioEngine *engine = [[AVAudioEngine alloc] init];
AVAudioInputNode *input = [engine inputNode];
AVAudioFormat *format = [input outputFormatForBus: 0];
[input installTapOnBus: 0 bufferSize: 8192 format: format block: ^(AVAudioPCMBuffer *buf, AVAudioTime *when) {
// __'__buf' contains captured audio from the node at time 'when'
}];
....
// start engine
```

> ❗ **Important**:  The framework may invoke the `tapBlock` on a thread other than the main thread.

## Parameters

- `bus`: The output bus to attach the tap to.
- `bufferSize`: The size of the incoming buffers. The implementation may choose another size.
- `format`: For  , you must specify the tap format as  .
- `tapBlock`: A block the framework calls with audio buffers.

## See Also

- [func removeTap(onBus: AVAudioNodeBus)](avaudionode/removetap(onbus:).md)
  Removes an audio tap on a bus you specify.
- [typealias AVAudioNodeTapBlock](avaudionodetapblock.md)
  The block that receives copies of the output of an audio node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudionode/installtap(onbus:buffersize:format:block:))*