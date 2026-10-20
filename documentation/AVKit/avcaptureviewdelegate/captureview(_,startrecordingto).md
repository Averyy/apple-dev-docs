# captureView(_:startRecordingTo:)

**Framework**: AVKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells the delegate that the user has made a request to start a new recording.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func captureView(_ captureView: AVCaptureView, startRecordingTo fileOutput: AVCaptureFileOutput)
```

```objc
- (void) captureView:(AVCaptureView *) captureView startRecordingToFileOutput:(AVCaptureFileOutput *) fileOutput;
```

#### Discussion

If the capture file output is an instance of [`AVCaptureMovieFileOutput`](../../AVFoundation/avcapturemoviefileoutput.md), you start recording by calling [`startRecording(to:recordingDelegate:)`](../../AVFoundation/avcapturefileoutput/startrecording%28to,recordingdelegate%29.md) on the capture file output.

## Parameters

- `captureView`: The capture view.
- `fileOutput`: The capture file output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avcaptureviewdelegate/captureview(_:startrecordingto:))*