# stopRecording()

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Tells the receiver to stop recording to the current file.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+

## Declaration

```swift
func stopRecording()
```

```objc
- (void) stopRecording;
```

#### Discussion

You can call this method when they want to stop recording new samples to the current file, and do not want to continue recording to another file. If you want to switch from one file to another, you should not call this method. Instead you should simply call [`startRecording(to:recordingDelegate:)`](./startrecording%28to,recordingdelegate%29.md) with the new file URL.

When recording is stopped either by calling this method, by changing files using [`startRecording(to:recordingDelegate:)`](./startrecording%28to,recordingdelegate%29.md), or because of an error, the remaining data that needs to be included to the file will be written in the background. Therefore, before using the file, you must wait until the delegate that was specified in [`startRecording(to:recordingDelegate:)`](./startrecording%28to,recordingdelegate%29.md) is notified when all data has been written to the file using the [`fileOutput(_:didFinishRecordingTo:from:error:)`](../avcapturefileoutputrecordingdelegate/fileoutput%28_,didfinishrecordingto,from,error%29.md) method.

In macOS, if this method is called within the captureOutput:didOutputSampleBuffer:fromConnection: delegate method, the last samples written to the current file are guaranteed to be those that were output immediately before those in the sample buffer passed to that method.

## See Also

### Related Documentation
- [var isRecording: Bool](./isrecording.md)
  Indicates whether recording is in progress.
### Managing recording
- [func startRecording(to: URL, recordingDelegate: any AVCaptureFileOutputRecordingDelegate)](./startrecording%28to,recordingdelegate%29.md)
  Starts recording media to the specified output URL.
- [func pauseRecording()](./pauserecording%28%29.md)
  Pauses recording to the current output file.
- [func resumeRecording()](./resumerecording%28%29.md)
  Resumes recording to the current output file after it was previously paused using [`pauseRecording()`](./pauserecording%28%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturefileoutput/stoprecording())*