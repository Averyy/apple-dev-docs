# showsCursor

**Framework**: ScreenCaptureKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the cursor is visible in the stream.

**Availability**:
- Mac Catalyst 18.2+
- macOS 12.3+

## Declaration

```swift
var showsCursor: Bool { get set }
```

```objc
@property (nonatomic, assign) BOOL showsCursor;
```

#### Discussion

The cursor is visible by default.

## See Also

### Configuring captured elements
- [var shouldBeOpaque: Bool](./shouldbeopaque.md)
  A Boolean value that indicates if semitransparent content presents as opaque.
- [var capturesShadowsOnly: Bool](./capturesshadowsonly.md)
  A Boolean value that indicates if the stream only captures shadows.
- [var ignoreShadowsDisplay: Bool](./ignoreshadowsdisplay.md)
  A Boolean value that indicates if the stream ignores the capturing of window shadows when streaming in display style.
- [var ignoreShadowsSingleWindow: Bool](./ignoreshadowssinglewindow.md)
  A Boolean value that indicates if the stream ignores the capturing of window shadows when streaming in window style.
- [var ignoreGlobalClipDisplay: Bool](./ignoreglobalclipdisplay.md)
  A Boolean value that indicates if the stream ignores content clipped past the edge of a display, when streaming in display style.
- [var ignoreGlobalClipSingleWindow: Bool](./ignoreglobalclipsinglewindow.md)
  A Boolean value that indicates if the stream ignores content clipped past the edge of a display, when streaming in window style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scstreamconfiguration/showscursor)*