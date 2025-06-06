# shouldBeOpaque

**Framework**: ScreenCaptureKit  
**Kind**: property

A Boolean value that indicates if semitransparent content presents as opaque.

**Availability**:
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
var shouldBeOpaque: Bool { get set }
```

#### Discussion

When this property is `true`, semitransparent content in the stream presents as backed by a solid white background, making the resulting image fully opaque. The default value is `false`.

## See Also

- [var showsCursor: Bool](scstreamconfiguration/showscursor.md)
  A Boolean value that determines whether the cursor is visible in the stream.
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

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scstreamconfiguration/shouldbeopaque)*