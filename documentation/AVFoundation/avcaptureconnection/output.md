# output

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The connection’s output port, if applicable.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+
- visionOS 2.1+

## Declaration

```swift
var output: AVCaptureOutput? { get }
```

```objc
@property (nonatomic, readonly, nullable) AVCaptureOutput * output;
```

## See Also

### Inspecting a connection
- [var inputPorts: [AVCaptureInput.Port]](./inputports.md)
  An array of the connection’s input ports.
- [var videoPreviewLayer: AVCaptureVideoPreviewLayer?](./videopreviewlayer.md)
  The video preview layer associated with the connection.
- [var audioChannels: [AVCaptureAudioChannel]](./audiochannels.md)
  An array of audio channels that the connection provides.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureconnection/output)*