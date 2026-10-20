# startTrackingCaptureRequest(using:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Tracks a capture request that uses the specified photo settings.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```swift
func startTrackingCaptureRequest(using settings: AVCapturePhotoSettings)
```

```objc
- (void) startTrackingCaptureRequestUsingPhotoSettings:(AVCapturePhotoSettings *) settings;
```

## Parameters

- `settings`: A settings object that the system passes [`capturePhoto(with:delegate:)`](../avcapturephotooutput/capturephoto%28with,delegate%29.md) for this capture request.

## See Also

### Performing tracking requests
- [func stopTrackingCaptureRequest(using: Int64)](./stoptrackingcapturerequest%28using%29.md)
  Stop tracking the capture request represented by the specified photo setting’s unique identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotooutputreadinesscoordinator/starttrackingcapturerequest(using:))*