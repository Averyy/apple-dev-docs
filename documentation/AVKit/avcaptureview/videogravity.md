# videoGravity

**Framework**: AVKit  
**Kind**: property

A string value that defines how the capture view displays video within its bounds.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
var videoGravity: AVLayerVideoGravity { get set }
```

#### Discussion

See [`AVLayerVideoGravity`](https://developer.apple.com/documentation/AVFoundation/AVLayerVideoGravity) for supported values. The default value is [`resizeAspect`](https://developer.apple.com/documentation/AVFoundation/AVLayerVideoGravity/resizeAspect).

## See Also

- [var controlsStyle: AVCaptureViewControlsStyle](avcaptureview/controlsstyle.md)
  The style of the capture controls presented by the view.
- [enum AVCaptureViewControlsStyle](avcaptureviewcontrolsstyle.md)
  Constants that describe the capture view’s supported controls styles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avcaptureview/videogravity)*