# canAddOutput(_:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Determines whether you can add an output to a session.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func canAddOutput(_ output: AVCaptureOutput) -> Bool
```

```objc
- (BOOL) canAddOutput:(AVCaptureOutput *) output;
```

#### Return Value

[`true`](../../Swift/true.md) if you can add the output; otherwise [`false`](../../Swift/false.md).

#### Discussion

In iOS and Mac Catalyst, the system imposes the following limitations on the combinations of outputs a capture session may contain:

- An app may add only a single output of a particular type. For apps that link against iOS 16 or later, this restriction no longer applies to [`AVCaptureVideoDataOutput`](../avcapturevideodataoutput.md).
- Prior to iOS 16, you can add an [`AVCaptureVideoDataOutput`](../avcapturevideodataoutput.md) and an [`AVCaptureMovieFileOutput`](../avcapturemoviefileoutput.md) to the same session, but only one may have its connection active. If you attempt to enable both connections, the system chooses the movie file output as the active connection and disables the video data output’s connection. For apps that link against iOS 16 or later, this restriction no longer exists.
- Similarly, prior to iOS 16, you can add an [`AVCaptureAudioDataOutput`](../avcaptureaudiodataoutput.md) and an [`AVCaptureMovieFileOutput`](../avcapturemoviefileoutput.md) to the same session, but only one may have its connection active. If you attempt to enable both connections, the system chooses the movie file output and disables the audio data output’s connection. For apps that link against iOS 16 or later, this restriction no longer exists.
- An app can’t add an [`AVCapturePhotoOutput`](../avcapturephotooutput.md) and [`AVCaptureStillImageOutput`](../avcapturestillimageoutput.md) to the same session.

> ❗ **Important**:  If you configure a capture session to use more than one [`AVCaptureVideoDataOutput`](../avcapturevideodataoutput.md) instance, monitor the value of the capture session’s [`hardwareCost`](./hardwarecost.md) property and reconfigure the session as appropriate.

## Parameters

- `output`: An output to add to the session.

## See Also

### Configuring outputs
- [var outputs: [AVCaptureOutput]](./outputs.md)
  The output destinations to which a captures session sends its data.
- [func addOutput(AVCaptureOutput)](./addoutput%28_%29.md)
  Adds an output to the capture session.
- [func removeOutput(AVCaptureOutput)](./removeoutput%28_%29.md)
  Removes an output from a capture session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesession/canaddoutput(_:))*