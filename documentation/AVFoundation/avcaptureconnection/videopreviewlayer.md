# videoPreviewLayer

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly, nullable) AVCaptureVideoPreviewLayer * videoPreviewLayer;
```

## Discussion

The connection sets the property in its [`init(inputPort:videoPreviewLayer:)`](./init%28inputport,videopreviewlayer%29.md) initializer.

## See Also

### Inspecting a connection
- [var inputPorts: [AVCaptureInput.Port]](./inputports.md)
  An array of the connection’s input ports.
- [var output: AVCaptureOutput?](./output.md)
  The connection’s output port, if applicable.
- [var audioChannels: [AVCaptureAudioChannel]](./audiochannels.md)
  An array of audio channels that the connection provides.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureconnection/videopreviewlayer)*