# installTapOnBus:bufferSize:format:error:block:

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```objc
- (BOOL) installTapOnBus:(AVAudioNodeBus) bus bufferSize:(AVAudioFrameCount) bufferSize format:(AVAudioFormat *) format error:(NSError **) outError block:(AVAudioNodeTapBlock) tapBlock;
```

#### Return Value

YES for success.

#### Discussion

Create a “tap” to record/monitor/observe the output of the node.

Only one tap may be installed on any bus. Taps may be safely installed and removed while the engine is running.

Note that if you have a tap installed on AVAudioOutputNode, there could be a mismatch between the tap buffer format and AVAudioOutputNode’s output format, depending on the underlying physical device. Hence, instead of tapping the AVAudioOutputNode, it is advised to tap the node connected to it.

E.g. to capture audio from input node:

## Parameters

- `bus`: The node output bus to which to attach the tap
- `bufferSize`: The requested size of the incoming buffers in sample frames. Supported range is [100, 400] ms.
- `format`: If non-nil, attempts to apply this as the format of the specified output bus. This should only be done when attaching to an output bus which is not connected to another node; an error will result otherwise. The tap and connection formats (if non-nil) on the specified bus should be identical. Otherwise, the latter operation will override any previously set format.
- `outError`: On exit, if an error occurs, a description of the error.
- `tapBlock`: A block to be called with audio buffers.

## See Also

### Managing audio taps
- [func installTap(onBus: AVAudioNodeBus, bufferSize: AVAudioFrameCount, format: AVAudioFormat?, block: AVAudioNodeTapBlock)](./installtap%28onbus,buffersize,format,block%29.md)
  Installs an audio tap on a bus you specify to record, monitor, and observe the output of the node.
- [func removeTap(onBus: AVAudioNodeBus)](./removetap%28onbus%29.md)
  Removes an audio tap on a bus you specify.
- [typealias AVAudioNodeTapBlock](../avaudionodetapblock.md)
  The block that receives copies of the output of an audio node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudionode/installtaponbus:buffersize:format:error:block:)*