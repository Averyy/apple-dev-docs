# scalesToFit

**Framework**: ScreenCaptureKit  
**Kind**: property

A Boolean value that indicates whether to scale the output to fit the configured width and height.

**Availability**:
- Mac Catalyst 18.2+
- macOS 12.3+

## Declaration

```swift
var scalesToFit: Bool { get set }
```

#### Discussion

The system uses this value during independent window capture.

## See Also

- [var width: Int](scstreamconfiguration/width.md)
  The width of the output.
- [var height: Int](scstreamconfiguration/height.md)
  The height of the output.
- [var sourceRect: CGRect](scstreamconfiguration/sourcerect.md)
  A rectangle that specifies the source area to capture.
- [var destinationRect: CGRect](scstreamconfiguration/destinationrect.md)
  A rectangle that specifies a destination into which to write the output.
- [var preservesAspectRatio: Bool](scstreamconfiguration/preservesaspectratio.md)
  A Boolean value that determines if the stream preserves aspect ratio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scstreamconfiguration/scalestofit)*