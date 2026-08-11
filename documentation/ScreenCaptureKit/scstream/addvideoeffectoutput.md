# addVideoEffectOutput(_:)

**Framework**: ScreenCaptureKit  
**Kind**: method

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
func addVideoEffectOutput(_ videoEffectOutput: SCVideoEffectOutput) throws
```

#### Discussion

Add a SCVideoEffectOutput to the SCStream to start camera video effect. Only one video effect output can be active per stream.

Returns a BOOL denoting if the add was successful. Video effect output is only supported on streams using in-app capture (presentPickerForCurrentApplication). Attempting to add a video effect output to a non-in-app capture stream will return NO with SCStreamErrorNotSupported. Camera video effect will start after successfully adding or if stream has not yet started, when stream starts capturing. Delegate for outputVideoEffectDidStartForStream: will be notified on the SCStreamDelegate, or outputVideoEffectDidFailForStream:withError: will be notified if camera video effect failed to start.

## Parameters

- `videoEffectOutput`: A SCVideoEffectOutput object to add to the stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scstream/addvideoeffectoutput(_:))*