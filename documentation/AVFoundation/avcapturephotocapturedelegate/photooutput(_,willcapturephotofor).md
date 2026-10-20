# photoOutput(_:willCapturePhotoFor:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) captureOutput:(AVCapturePhotoOutput *) output willCapturePhotoForResolvedSettings:(AVCaptureResolvedPhotoSettings *) resolvedSettings;
```

## Mentions

- [Tracking photo capture progress](../tracking-photo-capture-progress.md)

#### Discussion

The photo output calls this method as close as possible to the initial moment of capture. If the shutter sound is enabled, this call occurs immediately after the photo output begins playing the shutter sound.

> **Note**:  Live Photo capture disables the shutter sound. In some regions, the device’s mute switch can disable the shutter sound.

## Parameters

- `output`: The photo output performing the capture.
- `resolvedSettings`: An object describing the settings used for this capture. Match this object’s [`uniqueID`](../avcapturephotosettings/uniqueid.md) value to the [`uniqueID`](../avcapturephotosettings/uniqueid.md) property of the photo settings object you initiated capture with to determine which capture request this delegate call corresponds to. You can also use this object to find out which values the photo output has chosen for automatic settings.

## See Also

### Monitoring capture progress
- [func photoOutput(AVCapturePhotoOutput, willBeginCaptureFor: AVCaptureResolvedPhotoSettings)](./photooutput%28_,willbegincapturefor%29.md)
  Notifies the delegate that the capture output has resolved settings and will soon begin its capture process.
- [func photoOutput(AVCapturePhotoOutput, didCapturePhotoFor: AVCaptureResolvedPhotoSettings)](./photooutput%28_,didcapturephotofor%29.md)
  Notifies the delegate that the photo has been taken.
- [func photoOutput(AVCapturePhotoOutput, didFinishCaptureFor: AVCaptureResolvedPhotoSettings, error: (any Error)?)](./photooutput%28_,didfinishcapturefor,error%29.md)
  Notifies the delegate that the capture process is complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotocapturedelegate/photooutput(_:willcapturephotofor:))*