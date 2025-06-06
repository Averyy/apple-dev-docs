# session(_:didOutputAudioSampleBuffer:)

**Framework**: ARKit  
**Kind**: method

Tells the delegate that a new sample buffer of recorded audio is available.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
optional func session(_ session: ARSession, didOutputAudioSampleBuffer audioSampleBuffer: CMSampleBuffer)
```

#### Discussion

ARKit calls this method on your delegate object only if you’re running an AR session with a configuration whose  [`providesAudioData`](arconfiguration/providesaudiodata.md) setting is [`true`](https://developer.apple.com/documentation/swift/true).

## Parameters

- `session`: The session providing information.
- `audioSampleBuffer`: The sample buffer that was output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arsessionobserver/session(_:didoutputaudiosamplebuffer:))*