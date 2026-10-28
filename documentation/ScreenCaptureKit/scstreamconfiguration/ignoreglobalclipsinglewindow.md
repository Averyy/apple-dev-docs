# ignoreGlobalClipSingleWindow

**Framework**: ScreenCaptureKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates if the stream ignores content clipped past the edge of a display, when streaming in window style.

**Availability**:
- Mac Catalyst 18.2+
- macOS 14.0+

## Declaration

```swift
var ignoreGlobalClipSingleWindow: Bool { get set }
```

```objc
@property (nonatomic, assign) BOOL ignoreGlobalClipSingleWindow;
```

## Discussion

The display that originates the stream determines clipping bounds. When this value is `true`, the stream contains content moved past the clipping bounds. The default value is `false`.

## See Also

### Configuring captured elements
- [var showsCursor: Bool](./showscursor.md)
  A Boolean value that determines whether the cursor is visible in the stream.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scstreamconfiguration/ignoreglobalclipsinglewindow)*