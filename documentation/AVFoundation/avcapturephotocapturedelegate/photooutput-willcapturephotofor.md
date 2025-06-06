# photoOutput(_:willCapturePhotoFor:)

**Framework**: AVFoundation  
**Kind**: method

Notifies the delegate that photo capture is about to occur.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 17.0+

## Declaration

```swift
optional func photoOutput(_ output: AVCapturePhotoOutput, willCapturePhotoFor resolvedSettings: AVCaptureResolvedPhotoSettings)
```

## Mentions

- [Tracking Photo Capture Progress](tracking-photo-capture-progress.md)

#### Discussion

The photo output calls this method as close as possible to the initial moment of capture. If the shutter sound is enabled, this call occurs immediately after the photo output begins playing the shutter sound.

> **Note**:  Live Photo capture disables the shutter sound. In some regions, the device’s mute switch can disable the shutter sound.

 Live Photo capture disables the shutter sound. In some regions, the device’s mute switch can disable the shutter sound.

## Parameters

- `output`: The photo output performing the capture.
- `resolvedSettings`: An object describing the settings used for this capture. Match this object’s   value to the   property of the photo settings object you initiated capture with to determine which capture request this delegate call corresponds to. You can also use this object to find out which values the photo output has chosen for automatic settings.

## See Also

- [func photoOutput(AVCapturePhotoOutput, willBeginCaptureFor: AVCaptureResolvedPhotoSettings)](avcapturephotocapturedelegate/photooutput(_:willbegincapturefor:).md)
  Notifies the delegate that the capture output has resolved settings and will soon begin its capture process.
- [func photoOutput(AVCapturePhotoOutput, didCapturePhotoFor: AVCaptureResolvedPhotoSettings)](avcapturephotocapturedelegate/photooutput(_:didcapturephotofor:).md)
  Notifies the delegate that the photo has been taken.
- [func photoOutput(AVCapturePhotoOutput, didFinishCaptureFor: AVCaptureResolvedPhotoSettings, error: (any Error)?)](avcapturephotocapturedelegate/photooutput(_:didfinishcapturefor:error:).md)
  Notifies the delegate that the capture process is complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotocapturedelegate/photooutput(_:willcapturephotofor:))*