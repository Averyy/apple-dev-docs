# SSCenteredRectInRect(_:_:)

**Framework**: Screen Saver  
**Kind**: func  
**Role**: Function

Returns a rectangle.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func SSCenteredRectInRect(_ innerRect: NSRect, _ outerRect: NSRect) -> NSRect
```

```c
static NSRect SSCenteredRectInRect(NSRect innerRect, NSRect outerRect);
```

#### Return Value

A rectangle that’s the same size as `innerRect`, but is centered inside `outerRect`.

## Parameters

- `innerRect`: The rectangle to center.
- `outerRect`: The rectangle to contain `innerRect`.

## See Also

### Utilities
- [func SSRandomIntBetween(Int32, Int32) -> Int32](./ssrandomintbetween%28_,_%29.md)
  Returns a random integer value.
- [func SSRandomFloatBetween(CGFloat, CGFloat) -> CGFloat](./ssrandomfloatbetween%28_,_%29.md)
  Returns a random float value.
- [func SSRandomPointForSizeWithinRect(NSSize, NSRect) -> NSPoint](./ssrandompointforsizewithinrect%28_,_%29.md)
  Returns a random point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screensaver/sscenteredrectinrect(_:_:))*