# fileOutput(_:didFinishRecordingTo:from:error:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Informs the delegate when all pending data has been written to an output file.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+

## Declaration

```swift
func fileOutput(_ output: AVCaptureFileOutput, didFinishRecordingTo outputFileURL: URL, from connections: [AVCaptureConnection], error: (any Error)?)
```

```objc
- (void) captureOutput:(AVCaptureFileOutput *) output didFinishRecordingToOutputFileAtURL:(NSURL *) outputFileURL fromConnections:(NSArray<AVCaptureConnection *> *) connections error:(NSError *) error;
```

## Discussion

This method is called whenever a file is finished. If the file was forced to be finished due to an error, the error is described in the error parameter—otherwise, the error parameter is `nil`.

This method is called when the file output has finished writing all data to a file whose recording was stopped, either because [`startRecording(to:recordingDelegate:)`](../avcapturefileoutput/startrecording%28to,recordingdelegate%29.md) or [`stopRecording()`](../avcapturefileoutput/stoprecording%28%29.md) were called, or because an error (described by the error parameter) occurred (if no error occurred, the error parameter is `nil`).

This method is always called for each recording request, even if no data is successfully written to the file.

You should not assume that this method will be called on a specific thread.

## Parameters

- `output`: The capture file output that has finished writing the file.
- `outputFileURL`: The file URL of the file that is being written.
- `connections`: An array of [`AVCaptureConnection`](../avcaptureconnection.md) objects attached to the file output that provided the data that is being written to the file.
- `error`: If the file was not written successfully, an error object that describes the problem; otherwise `nil`.

## See Also

### Delegate methods
- [func fileOutput(AVCaptureFileOutput, didStartRecordingTo: URL, from: [AVCaptureConnection])](./fileoutput%28_,didstartrecordingto,from%29.md)
  Informs the delegate when the output has started writing to a file.
- [func fileOutput(AVCaptureFileOutput, didStartRecordingTo: URL, startPTS: CMTime, from: [AVCaptureConnection])](./fileoutput%28_,didstartrecordingto,startpts,from%29.md)
- [func fileOutput(AVCaptureFileOutput, willFinishRecordingTo: URL, from: [AVCaptureConnection], error: (any Error)?)](./fileoutput%28_,willfinishrecordingto,from,error%29.md)
  Informs the delegate when the output will stop writing new samples to a file.
- [func fileOutput(AVCaptureFileOutput, didPauseRecordingTo: URL, from: [AVCaptureConnection])](./fileoutput%28_,didpauserecordingto,from%29.md)
  Called whenever the output is recording to a file and successfully pauses the recording at the request of a client.
- [func fileOutput(AVCaptureFileOutput, didResumeRecordingTo: URL, from: [AVCaptureConnection])](./fileoutput%28_,didresumerecordingto,from%29.md)
  Called whenever the output, at the request of the client, successfully resumes a file recording that was paused.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturefileoutputrecordingdelegate/fileoutput(_:didfinishrecordingto:from:error:))*