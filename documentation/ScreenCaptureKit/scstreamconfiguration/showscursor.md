# showsCursor

**Framework**: ScreenCaptureKit  
**Kind**: property

A Boolean value that determines whether the cursor is visible in the stream.

**Availability**:
- Mac Catalyst 18.2+
- macOS 12.3+

## Declaration

```swift
var showsCursor: Bool { get set }
```

#### Discussion

The cursor is visible by default.

## See Also

- [var shouldBeOpaque: Bool](scstreamconfiguration/shouldbeopaque.md)
  A Boolean value that indicates if semitransparent content presents as opaque.
- [var capturesShadowsOnly: Bool](scstreamconfiguration/capturesshadowsonly.md)
  A Boolean value that indicates if the stream only captures shadows.
- [var ignoreShadowsDisplay: Bool](scstreamconfiguration/ignoreshadowsdisplay.md)
  A Boolean value that indicates if the stream ignores the capturing of window shadows when streaming in display style.
- [var ignoreShadowsSingleWindow: Bool](scstreamconfiguration/ignoreshadowssinglewindow.md)
  A Boolean value that indicates if the stream ignores the capturing of window shadows when streaming in window style.
- [var ignoreGlobalClipDisplay: Bool](scstreamconfiguration/ignoreglobalclipdisplay.md)
  A Boolean value that indicates if the stream ignores content clipped past the edge of a display, when streaming in display style.
- [var ignoreGlobalClipSingleWindow: Bool](scstreamconfiguration/ignoreglobalclipsinglewindow.md)
  A Boolean value that indicates if the stream ignores content clipped past the edge of a display, when streaming in window style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scstreamconfiguration/showscursor)*