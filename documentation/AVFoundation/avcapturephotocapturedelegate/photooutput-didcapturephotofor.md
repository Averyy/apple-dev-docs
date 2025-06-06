# photoOutput(_:didCapturePhotoFor:)

**Framework**: AVFoundation  
**Kind**: method

Notifies the delegate that the photo has been taken.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 17.0+

## Declaration

```swift
optional func photoOutput(_ output: AVCapturePhotoOutput, didCapturePhotoFor resolvedSettings: AVCaptureResolvedPhotoSettings)
```

## Mentions

- [Tracking Photo Capture Progress](tracking-photo-capture-progress.md)

#### Discussion

The photo output calls this method as soon as the first step of capture ends—that is, at the end of the photographic exposure time.

## Parameters

- `output`: The photo output performing the capture.
- `resolvedSettings`: An object describing the settings used for this capture. Match this object’s   value to the   property of the photo settings object you initiated capture with to determine which capture request this delegate call corresponds to. You can also use this object to find out which values the photo output has chosen for automatic settings.

## See Also

- [func photoOutput(AVCapturePhotoOutput, willBeginCaptureFor: AVCaptureResolvedPhotoSettings)](avcapturephotocapturedelegate/photooutput(_:willbegincapturefor:).md)
  Notifies the delegate that the capture output has resolved settings and will soon begin its capture process.
- [func photoOutput(AVCapturePhotoOutput, willCapturePhotoFor: AVCaptureResolvedPhotoSettings)](avcapturephotocapturedelegate/photooutput(_:willcapturephotofor:).md)
  Notifies the delegate that photo capture is about to occur.
- [func photoOutput(AVCapturePhotoOutput, didFinishCaptureFor: AVCaptureResolvedPhotoSettings, error: (any Error)?)](avcapturephotocapturedelegate/photooutput(_:didfinishcapturefor:error:).md)
  Notifies the delegate that the capture process is complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotocapturedelegate/photooutput(_:didcapturephotofor:))*