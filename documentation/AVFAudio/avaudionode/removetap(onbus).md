# removeTap(onBus:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) removeTapOnBus:(AVAudioNodeBus) bus;
```

## Parameters

- `bus`: The node output bus with the tap to remove.

## See Also

### Managing audio taps
- [func installAudioTap(onBus: AVAudioNodeBus, bufferSize: AVAudioFrameCount, format: AVAudioFormat?, tapProvider: (AVReadOnlyAudioPCMBuffer, AVAudioTime) -> Void) throws](./installaudiotap%28onbus,buffersize,format,tapprovider%29.md)
  Install a tap on a bus using a sendable block
- [func installTap(onBus: AVAudioNodeBus, bufferSize: AVAudioFrameCount, format: AVAudioFormat?, block: AVAudioNodeTapBlock)](./installtap%28onbus,buffersize,format,block%29.md)
  Installs an audio tap on a bus you specify to record, monitor, and observe the output of the node.
- [typealias AVAudioNodeTapBlock](../avaudionodetapblock.md)
  The block that receives copies of the output of an audio node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudionode/removetap(onbus:))*