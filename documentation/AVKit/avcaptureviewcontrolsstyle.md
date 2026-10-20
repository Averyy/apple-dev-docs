# AVCaptureViewControlsStyle

**Framework**: AVKit  
**Kind**: enum  
**Role**: Enumeration

Constants that describe the capture view’s supported controls styles.

**Availability**:
- macOS 10.10+

## Declaration

```swift
enum AVCaptureViewControlsStyle
```

```c
enum AVCaptureViewControlsStyle : NSInteger;
```

## Topics

### Creating a controls style
- [init?(rawValue: Int)](./avcaptureviewcontrolsstyle/init%28rawvalue%29.md)
### Controls styles
- [AVCaptureViewControlsStyle.inline](./avcaptureviewcontrolsstyle/inline.md)
  The view’s inline controls style.
- [AVCaptureViewControlsStyle.floating](./avcaptureviewcontrolsstyle/floating.md)
  The view’s floating controls style, which matches the user interface of QuickTime Player.
- [AVCaptureViewControlsStyle.inlineDeviceSelection](./avcaptureviewcontrolsstyle/inlinedeviceselection.md)
  The view’s inline device selection style.
- [static var `default`: AVCaptureViewControlsStyle](./avcaptureviewcontrolsstyle/default.md)
  The view’s default controls style.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Customizing the view
- [var controlsStyle: AVCaptureViewControlsStyle](./avcaptureview/controlsstyle.md)
  The style of the capture controls presented by the view.
- [var videoGravity: AVLayerVideoGravity](./avcaptureview/videogravity.md)
  A string value that defines how the capture view displays video within its bounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avcaptureviewcontrolsstyle)*