# destinationRect

**Framework**: ScreenCaptureKit  
**Kind**: property  
**Role**: Instance Property

A rectangle that specifies a destination into which to write the output.

**Availability**:
- Mac Catalyst 18.2+
- macOS 12.3+

## Declaration

```swift
var destinationRect: CGRect { get set }
```

```objc
@property (nonatomic, assign) CGRect destinationRect;
```

## Discussion

If you don’t specify a destination rectangle, the system uses the full dimensions of the output surface.

> **Note**:  The system doesn’t reference this value when capturing a single window because it draws the window into the output’s full bounds.

## See Also

### Specifying dimensions
- [var width: Int](./width.md)
  The width of the output.
- [var height: Int](./height.md)
  The height of the output.
- [var scalesToFit: Bool](./scalestofit.md)
  A Boolean value that indicates whether to scale the output to fit the configured width and height.
- [var sourceRect: CGRect](./sourcerect.md)
  A rectangle that specifies the source area to capture.
- [var preservesAspectRatio: Bool](./preservesaspectratio.md)
  A Boolean value that determines if the stream preserves aspect ratio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scstreamconfiguration/destinationrect)*