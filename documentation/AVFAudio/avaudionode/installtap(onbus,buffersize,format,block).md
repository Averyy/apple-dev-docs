# installTap(onBus:bufferSize:format:block:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

Installs an audio tap on a bus you specify to record, monitor, and observe the output of the node.

**Availability**:
- iOS 8.0+ - Deprecated in 27.0
- iPadOS 8.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.10+ - Deprecated in 27.0
- tvOS 9.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 2.0+ - Deprecated in 27.0

## Declaration

```swift
func installTap(onBus bus: AVAudioNodeBus, bufferSize: AVAudioFrameCount, format: AVAudioFormat?, block tapBlock: @escaping AVAudioNodeTapBlock)
```

```objc
- (void) installTapOnBus:(AVAudioNodeBus) bus bufferSize:(AVAudioFrameCount) bufferSize format:(AVAudioFormat *) format block:(AVAudioNodeTapBlock) tapBlock;
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
- `format`: If non-`nil`, the framework applies this format to the output bus you specify. An error occurs when attaching to an output bus that’s already in a connected state. The tap and connection formats (if non-`nil`) on the bus need to be identical. Otherwise, the latter operation overrides the previous format.

  For `AVAudioOutputNode`, you must specify the tap format as `nil`.
- `tapBlock`: A block the framework calls with audio buffers.

## See Also

### Managing audio taps
- [func installAudioTap(onBus: AVAudioNodeBus, bufferSize: AVAudioFrameCount, format: AVAudioFormat?, tapProvider: (AVReadOnlyAudioPCMBuffer, AVAudioTime) -> Void) throws](./installaudiotap%28onbus,buffersize,format,tapprovider%29.md)
  Install a tap on a bus using a sendable block
- [func removeTap(onBus: AVAudioNodeBus)](./removetap%28onbus%29.md)
  Removes an audio tap on a bus you specify.
- [typealias AVAudioNodeTapBlock](../avaudionodetapblock.md)
  The block that receives copies of the output of an audio node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudionode/installtap(onbus:buffersize:format:block:))*