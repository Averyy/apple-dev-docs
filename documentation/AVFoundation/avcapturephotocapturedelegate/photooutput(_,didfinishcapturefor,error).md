# photoOutput(_:didFinishCaptureFor:error:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) captureOutput:(AVCapturePhotoOutput *) output didFinishCaptureForResolvedSettings:(AVCaptureResolvedPhotoSettings *) resolvedSettings error:(NSError *) error;
```

## Mentions

- [Capturing photos in RAW and Apple ProRAW formats](../capturing-photos-in-raw-and-apple-proraw-formats.md)
- [Tracking photo capture progress](../tracking-photo-capture-progress.md)

## Discussion

The photo output calls this method when the entire capture process has finished, and no more delegate messages will be sent for this capture request. Use this time to clean up any resources you’ve allocated that relate to this capture request.

## Parameters

- `output`: The photo output performing the capture.
- `resolvedSettings`: An object describing the settings used for this capture. Match this object’s [`uniqueID`](../avcapturephotosettings/uniqueid.md) value to the [`uniqueID`](../avcapturephotosettings/uniqueid.md) property of the photo settings object you initiated capture with to determine which capture request this delegate call corresponds to. You can also use this object to find out which values the photo output has chosen for automatic settings.
- `error`: If the capture process did not complete successfully, an error object describing the failure; otherwise, `nil`.

## See Also

### Monitoring capture progress
- [func photoOutput(AVCapturePhotoOutput, willBeginCaptureFor: AVCaptureResolvedPhotoSettings)](./photooutput%28_,willbegincapturefor%29.md)
  Notifies the delegate that the capture output has resolved settings and will soon begin its capture process.
- [func photoOutput(AVCapturePhotoOutput, willCapturePhotoFor: AVCaptureResolvedPhotoSettings)](./photooutput%28_,willcapturephotofor%29.md)
  Notifies the delegate that photo capture is about to occur.
- [func photoOutput(AVCapturePhotoOutput, didCapturePhotoFor: AVCaptureResolvedPhotoSettings)](./photooutput%28_,didcapturephotofor%29.md)
  Notifies the delegate that the photo has been taken.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotocapturedelegate/photooutput(_:didfinishcapturefor:error:))*