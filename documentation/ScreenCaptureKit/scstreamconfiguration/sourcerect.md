# sourceRect

**Framework**: Screencapturekit  
**Kind**: property

A rectangle that specifies the source area to capture.

**Availability**:
- Mac Catalyst 18.2+
- macOS 12.3+

## Declaration

```swift
var sourceRect: CGRect { get set }
```

#### Discussion

If you don’t specify a source rectangle to capture, the system captures the entire display.

> **Note**:  The system doesn’t reference this value when you capture a single window because it captures the full bounds of the window.

## See Also

- [var width: Int](scstreamconfiguration/width.md)
  The width of the output.
- [var height: Int](scstreamconfiguration/height.md)
  The height of the output.
- [var scalesToFit: Bool](scstreamconfiguration/scalestofit.md)
  A Boolean value that indicates whether to scale the output to fit the configured width and height.
- [var destinationRect: CGRect](scstreamconfiguration/destinationrect.md)
  A rectangle that specifies a destination into which to write the output.
- [var preservesAspectRatio: Bool](scstreamconfiguration/preservesaspectratio.md)
  A Boolean value that determines if the stream preserves aspect ratio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scstreamconfiguration/sourcerect)*