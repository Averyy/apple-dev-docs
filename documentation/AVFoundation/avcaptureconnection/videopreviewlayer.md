# videoPreviewLayer

**Framework**: AVFoundation  
**Kind**: property

The video preview layer associated with the connection.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+

## Declaration

```swift
var videoPreviewLayer: AVCaptureVideoPreviewLayer? { get }
```

#### Discussion

The connection sets the property in its [`init(inputPort:videoPreviewLayer:)`](avcaptureconnection/init(inputport:videopreviewlayer:).md) initializer.

## See Also

- [var inputPorts: [AVCaptureInput.Port]](avcaptureconnection/inputports.md)
  An array of the connection’s input ports.
- [var output: AVCaptureOutput?](avcaptureconnection/output.md)
  The connection’s output port, if applicable.
- [var audioChannels: [AVCaptureAudioChannel]](avcaptureconnection/audiochannels.md)
  An array of audio channels that the connection provides.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureconnection/videopreviewlayer)*