# compositingOperation

**Framework**: AppKit  
**Kind**: property

The graphics context’s global compositing operation setting.

**Availability**:
- macOS ?+

## Declaration

```swift
var compositingOperation: NSCompositingOperation { get set }
```

#### Discussion

The compositing operation is a global attribute of the graphics context and affects drawing operations that do not take an explicit compositing operation parameter. For methods that do take an explicit compositing operation parameter, the value of that parameter supersedes the global value. The compositing operations are related to (but different from) the blend mode settings used in Quartz. Only the default compositing operation ([`NSCompositeCopy`](nscompositecopy.md)) is supported when rendering PDF or PostScript content. See [`NSCompositingOperation`](nscompositingoperation.md) for valid constants.

## See Also

- [enum NSCompositingOperation](nscompositingoperation.md)
  Constants that describe compositing operators in terms of source and destination images, each having an opaque and transparent region.
- [var imageInterpolation: NSImageInterpolation](nsgraphicscontext/imageinterpolation.md)
  A constant that specifies the graphics context’s interpolation, or image smoothing, behavior.
- [enum NSImageInterpolation](nsimageinterpolation.md)
  Constants that specify the interpolation, or image smoothing, behavior used by the image interpolation property.
- [var shouldAntialias: Bool](nsgraphicscontext/shouldantialias.md)
  A Boolean value that indicates whether the graphics context uses antialiasing.
- [var patternPhase: NSPoint](nsgraphicscontext/patternphase.md)
  The amount to offset the pattern color when filling the graphics context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgraphicscontext/compositingoperation)*