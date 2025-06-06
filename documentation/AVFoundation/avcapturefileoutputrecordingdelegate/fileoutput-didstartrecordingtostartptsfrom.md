# fileOutput(_:didStartRecordingTo:startPTS:from:)

**Framework**: AVFoundation  
**Kind**: method

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- macOS 15.2+
- tvOS 18.2+

## Declaration

```swift
optional func fileOutput(_ output: AVCaptureFileOutput, didStartRecordingTo fileURL: URL, startPTS: CMTime, from connections: [AVCaptureConnection])
```

#### Discussion

```None
Informs the delegate when the output has started writing to a file.
```

This method is called when the file output has started writing data to a file. If an error condition prevents any data from being written, this method may not be called. captureOutput:willFinishRecordingToOutputFileAtURL:fromConnections:error: and captureOutput:didFinishRecordingToOutputFileAtURL:fromConnections:error: will always be called, even if no data is written.

```None
If this method is implemented, the alternative delegate callback -captureOutput:didStartRecordingToOutputFileAtURL:fromConnections will not be called.

Clients should not assume that this method will be called on a specific thread, and should also try to make this method as efficient as possible.
```

## Parameters

- `output`: The capture file output that started writing the file.
- `fileURL`: The file URL of the file that is being written.
- `startPTS`: The timestamp of the first buffer written to the file, synced with AVCaptureSession.synchronizationClock
- `connections`: An array of AVCaptureConnection objects attached to the file output that provided the data that is being written to the file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturefileoutputrecordingdelegate/fileoutput(_:didstartrecordingto:startpts:from:))*