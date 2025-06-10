# photoOutput(_:didFinishCaptureFor:error:)

**Framework**: AVFoundation  
**Kind**: method

Notifies the delegate that the capture process is complete.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 17.0+

## Declaration

```swift
optional func photoOutput(_ output: AVCapturePhotoOutput, didFinishCaptureFor resolvedSettings: AVCaptureResolvedPhotoSettings, error: (any Error)?)
```

## Mentions

- [Tracking Photo Capture Progress](tracking-photo-capture-progress.md)
- [Capturing Photos in RAW and Apple ProRAW Formats](capturing-photos-in-raw-and-apple-proraw-formats.md)

#### Discussion

The photo output calls this method when the entire capture process has finished, and no more delegate messages will be sent for this capture request. Use this time to clean up any resources you’ve allocated that relate to this capture request.

## Parameters

- `output`: The photo output performing the capture.
- `resolvedSettings`: An object describing the settings used for this capture. Match this object’s   value to the   property of the photo settings object you initiated capture with to determine which capture request this delegate call corresponds to. You can also use this object to find out which values the photo output has chosen for automatic settings.
- `error`: If the capture process did not complete successfully, an error object describing the failure; otherwise,  .

## See Also

- [func photoOutput(AVCapturePhotoOutput, willBeginCaptureFor: AVCaptureResolvedPhotoSettings)](avcapturephotocapturedelegate/photooutput(_:willbegincapturefor:).md)
  Notifies the delegate that the capture output has resolved settings and will soon begin its capture process.
- [func photoOutput(AVCapturePhotoOutput, willCapturePhotoFor: AVCaptureResolvedPhotoSettings)](avcapturephotocapturedelegate/photooutput(_:willcapturephotofor:).md)
  Notifies the delegate that photo capture is about to occur.
- [func photoOutput(AVCapturePhotoOutput, didCapturePhotoFor: AVCaptureResolvedPhotoSettings)](avcapturephotocapturedelegate/photooutput(_:didcapturephotofor:).md)
  Notifies the delegate that the photo has been taken.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotocapturedelegate/photooutput(_:didfinishcapturefor:error:))*