# audioChannels

**Framework**: AVFoundation  
**Kind**: property

An array of audio channels that the connection provides.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+

## Declaration

```swift
var audioChannels: [AVCaptureAudioChannel] { get }
```

#### Discussion

The property only applies to a video connection.

## See Also

- [var inputPorts: [AVCaptureInput.Port]](avcaptureconnection/inputports.md)
  An array of the connection’s input ports.
- [var output: AVCaptureOutput?](avcaptureconnection/output.md)
  The connection’s output port, if applicable.
- [var videoPreviewLayer: AVCaptureVideoPreviewLayer?](avcaptureconnection/videopreviewlayer.md)
  The video preview layer associated with the connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureconnection/audiochannels)*