# videoGravity

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

A string value that defines how the capture view displays video within its bounds.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var videoGravity: AVLayerVideoGravity { get set }
```

```objc
@property (copy) AVLayerVideoGravity videoGravity;
```

#### Discussion

See [`AVLayerVideoGravity`](../../AVFoundation/avlayervideogravity.md) for supported values. The default value is [`resizeAspect`](../../AVFoundation/avlayervideogravity/resizeaspect.md).

## See Also

### Customizing the view
- [var controlsStyle: AVCaptureViewControlsStyle](./controlsstyle.md)
  The style of the capture controls presented by the view.
- [enum AVCaptureViewControlsStyle](../avcaptureviewcontrolsstyle.md)
  Constants that describe the capture view’s supported controls styles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avcaptureview/videogravity)*