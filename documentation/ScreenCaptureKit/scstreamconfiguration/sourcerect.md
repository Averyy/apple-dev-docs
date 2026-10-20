# sourceRect

**Framework**: ScreenCaptureKit  
**Kind**: property  
**Role**: Instance Property

A rectangle that specifies the source area to capture.

**Availability**:
- Mac Catalyst 18.2+
- macOS 12.3+

## Declaration

```swift
var sourceRect: CGRect { get set }
```

```objc
@property (nonatomic, assign) CGRect sourceRect;
```

#### Discussion

If you don’t specify a source rectangle to capture, the system captures the entire display.

> **Note**:  The system doesn’t reference this value when you capture a single window because it captures the full bounds of the window.

## See Also

### Specifying dimensions
- [var width: Int](./width.md)
  The width of the output.
- [var height: Int](./height.md)
  The height of the output.
- [var scalesToFit: Bool](./scalestofit.md)
  A Boolean value that indicates whether to scale the output to fit the configured width and height.
- [var destinationRect: CGRect](./destinationrect.md)
  A rectangle that specifies a destination into which to write the output.
- [var preservesAspectRatio: Bool](./preservesaspectratio.md)
  A Boolean value that determines if the stream preserves aspect ratio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scstreamconfiguration/sourcerect)*