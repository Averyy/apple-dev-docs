# fileOutput(_:didStartRecordingTo:from:)

**Framework**: AVFoundation  
**Kind**: method

Informs the delegate when the output has started writing to a file.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+

## Declaration

```swift
optional func fileOutput(_ output: AVCaptureFileOutput, didStartRecordingTo fileURL: URL, from connections: [AVCaptureConnection])
```

#### Discussion

If an error condition prevents any data from being written, this method may not be called. [`fileOutput(_:willFinishRecordingTo:from:error:)`](avcapturefileoutputrecordingdelegate/fileoutput(_:willfinishrecordingto:from:error:).md) and [`fileOutput(_:didFinishRecordingTo:from:error:)`](avcapturefileoutputrecordingdelegate/fileoutput(_:didfinishrecordingto:from:error:).md) are always called, even if no data is written.

You should not assume that this method will be called on a specific thread, and should make this method as efficient as possible.

## Parameters

- `output`: The capture file output that started writing the file.
- `fileURL`: The file URL of the file that is being written.
- `connections`: An array of   objects attached to the file output that provided the data that is being written to the file.

## See Also

- [func fileOutput(AVCaptureFileOutput, didStartRecordingTo: URL, startPTS: CMTime, from: [AVCaptureConnection])](avcapturefileoutputrecordingdelegate/fileoutput(_:didstartrecordingto:startpts:from:).md)
- [func fileOutput(AVCaptureFileOutput, willFinishRecordingTo: URL, from: [AVCaptureConnection], error: (any Error)?)](avcapturefileoutputrecordingdelegate/fileoutput(_:willfinishrecordingto:from:error:).md)
  Informs the delegate when the output will stop writing new samples to a file.
- [func fileOutput(AVCaptureFileOutput, didFinishRecordingTo: URL, from: [AVCaptureConnection], error: (any Error)?)](avcapturefileoutputrecordingdelegate/fileoutput(_:didfinishrecordingto:from:error:).md)
  Informs the delegate when all pending data has been written to an output file.
- [func fileOutput(AVCaptureFileOutput, didPauseRecordingTo: URL, from: [AVCaptureConnection])](avcapturefileoutputrecordingdelegate/fileoutput(_:didpauserecordingto:from:).md)
  Called whenever the output is recording to a file and successfully pauses the recording at the request of a client.
- [func fileOutput(AVCaptureFileOutput, didResumeRecordingTo: URL, from: [AVCaptureConnection])](avcapturefileoutputrecordingdelegate/fileoutput(_:didresumerecordingto:from:).md)
  Called whenever the output, at the request of the client, successfully resumes a file recording that was paused.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturefileoutputrecordingdelegate/fileoutput(_:didstartrecordingto:from:))*