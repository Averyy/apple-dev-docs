# session(_:didOutputAudioSampleBuffer:)

**Framework**: ARKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that a new sample buffer of recorded audio is available.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+

## Declaration

```swift
optional func session(_ session: ARSession, didOutputAudioSampleBuffer audioSampleBuffer: CMSampleBuffer)
```

```objc
- (void) session:(ARSession *) session didOutputAudioSampleBuffer:(CMSampleBufferRef) audioSampleBuffer;
```

#### Discussion

ARKit calls this method on your delegate object only if you’re running an AR session with a configuration whose  [`providesAudioData`](../arconfiguration/providesaudiodata.md) setting is [`true`](../../Swift/true.md).

## Parameters

- `session`: The session providing information.
- `audioSampleBuffer`: The sample buffer that was output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arsessionobserver/session(_:didoutputaudiosamplebuffer:))*