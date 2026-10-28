# shouldAntialias

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the graphics context uses antialiasing.

**Availability**:
- macOS

## Declaration

```swift
var shouldAntialias: Bool { get set }
```

```objc
@property BOOL shouldAntialias;
```

## Discussion

[`true`](../../Swift/true.md) if the receiver uses antialiasing. This value is part of the graphics state and is restored by [`restoreGraphicsState()`](./restoregraphicsstate%28%29-swift.method.md).

## See Also

### Configuring Rendering Options
- [var compositingOperation: NSCompositingOperation](./compositingoperation.md)
  The graphics context’s global compositing operation setting.
- [enum NSCompositingOperation](../nscompositingoperation.md)
  Constants that describe compositing operators in terms of source and destination images, each having an opaque and transparent region.
- [var imageInterpolation: NSImageInterpolation](./imageinterpolation.md)
  A constant that specifies the graphics context’s interpolation, or image smoothing, behavior.
- [enum NSImageInterpolation](../nsimageinterpolation.md)
  Constants that specify the interpolation, or image smoothing, behavior used by the image interpolation property.
- [var patternPhase: NSPoint](./patternphase.md)
  The amount to offset the pattern color when filling the graphics context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgraphicscontext/shouldantialias)*