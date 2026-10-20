# audioChannels

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly) NSArray<AVCaptureAudioChannel *> * audioChannels;
```

#### Discussion

The property only applies to a video connection.

## See Also

### Inspecting a connection
- [var inputPorts: [AVCaptureInput.Port]](./inputports.md)
  An array of the connection’s input ports.
- [var output: AVCaptureOutput?](./output.md)
  The connection’s output port, if applicable.
- [var videoPreviewLayer: AVCaptureVideoPreviewLayer?](./videopreviewlayer.md)
  The video preview layer associated with the connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureconnection/audiochannels)*