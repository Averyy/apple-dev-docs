# captureView(_:startRecordingTo:)

**Framework**: AVKit  
**Kind**: method  
**Required**: Yes

Tells the delegate that the user has made a request to start a new recording.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func captureView(_ captureView: AVCaptureView, startRecordingTo fileOutput: AVCaptureFileOutput)
```

#### Discussion

If the capture file output is an instance of [`AVCaptureMovieFileOutput`](https://developer.apple.com/documentation/avfoundation/avcapturemoviefileoutput), you start recording by calling [`startRecording(to:recordingDelegate:)`](https://developer.apple.com/documentation/avfoundation/avcapturefileoutput/startrecording(to:recordingdelegate:)) on the capture file output.

## Parameters

- `captureView`: The capture view.
- `fileOutput`: The capture file output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avcaptureviewdelegate/captureview(_:startrecordingto:))*