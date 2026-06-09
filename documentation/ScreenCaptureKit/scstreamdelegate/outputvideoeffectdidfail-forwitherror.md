# outputVideoEffectDidFail(for:withError:)

**Framework**: ScreenCaptureKit  
**Kind**: method

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
optional func outputVideoEffectDidFail(for stream: SCStream, withError error: any Error)
```

#### Discussion

outputVideoEffectDidFailForStream:withError:

Notifies the delegate that the video effect failed with an error. This can occur if the camera device is unavailable, permissions are missing, or an internal error occurs.

## Parameters

- `stream`: The SCStream object
- `error`: The error describing why the video effect failed


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scstreamdelegate/outputvideoeffectdidfail(for:witherror:))*