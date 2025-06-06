# destinationRect

**Framework**: Screencapturekit  
**Kind**: property

A rectangle that specifies a destination into which to write the output.

**Availability**:
- Mac Catalyst 18.2+
- macOS 12.3+

## Declaration

```swift
var destinationRect: CGRect { get set }
```

#### Discussion

If you don’t specify a destination rectangle, the system uses the full dimensions of the output surface.

> **Note**:  The system doesn’t reference this value when capturing a single window because it draws the window into the output’s full bounds.

## See Also

- [var width: Int](scstreamconfiguration/width.md)
  The width of the output.
- [var height: Int](scstreamconfiguration/height.md)
  The height of the output.
- [var scalesToFit: Bool](scstreamconfiguration/scalestofit.md)
  A Boolean value that indicates whether to scale the output to fit the configured width and height.
- [var sourceRect: CGRect](scstreamconfiguration/sourcerect.md)
  A rectangle that specifies the source area to capture.
- [var preservesAspectRatio: Bool](scstreamconfiguration/preservesaspectratio.md)
  A Boolean value that determines if the stream preserves aspect ratio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scstreamconfiguration/destinationrect)*