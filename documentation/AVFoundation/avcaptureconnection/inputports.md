# inputPorts

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

An array of the connection’s input ports.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+
- visionOS 2.1+

## Declaration

```swift
var inputPorts: [AVCaptureInput.Port] { get }
```

```objc
@property (nonatomic, readonly) NSArray<AVCaptureInputPort *> * inputPorts;
```

## Discussion

Input ports are instances of [`AVCaptureInput.Port`](../avcaptureinput/port.md).

## See Also

### Inspecting a connection
- [var output: AVCaptureOutput?](./output.md)
  The connection’s output port, if applicable.
- [var videoPreviewLayer: AVCaptureVideoPreviewLayer?](./videopreviewlayer.md)
  The video preview layer associated with the connection.
- [var audioChannels: [AVCaptureAudioChannel]](./audiochannels.md)
  An array of audio channels that the connection provides.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureconnection/inputports)*