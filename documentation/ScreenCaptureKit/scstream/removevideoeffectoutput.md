# removeVideoEffectOutput(_:)

**Framework**: ScreenCaptureKit  
**Kind**: method

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)

## Declaration

```swift
func removeVideoEffectOutput(_ videoEffectOutput: SCVideoEffectOutput) throws
```

#### Discussion

Remove SCVideoEffectOutput from the SCStream. Stops camera video effect if currently active.

Returns a BOOL denoting if the remove was successful. Delegate for outputVideoEffectDidStopForStream: will be notified on the SCStreamDelegate. If stopCapture is called without removing videoEffectOutput, camera video effect will be stopped automatically.

## Parameters

- `videoEffectOutput`: A SCVideoEffectOutput object to remove from the stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scstream/removevideoeffectoutput(_:))*