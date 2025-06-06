# imageInterpolation

**Framework**: AppKit  
**Kind**: property

A constant that specifies the graphics context’s interpolation, or image smoothing, behavior.

**Availability**:
- macOS ?+

## Declaration

```swift
var imageInterpolation: NSImageInterpolation { get set }
```

#### Discussion

Note that this value is not part of the graphics state, so it cannot be reset using [`restoreGraphicsState()`](nsgraphicscontext/restoregraphicsstate()-swift.method.md).

## See Also

- [var compositingOperation: NSCompositingOperation](nsgraphicscontext/compositingoperation.md)
  The graphics context’s global compositing operation setting.
- [enum NSCompositingOperation](nscompositingoperation.md)
  Constants that describe compositing operators in terms of source and destination images, each having an opaque and transparent region.
- [enum NSImageInterpolation](nsimageinterpolation.md)
  Constants that specify the interpolation, or image smoothing, behavior used by the image interpolation property.
- [var shouldAntialias: Bool](nsgraphicscontext/shouldantialias.md)
  A Boolean value that indicates whether the graphics context uses antialiasing.
- [var patternPhase: NSPoint](nsgraphicscontext/patternphase.md)
  The amount to offset the pattern color when filling the graphics context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgraphicscontext/imageinterpolation)*