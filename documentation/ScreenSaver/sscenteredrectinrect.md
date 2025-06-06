# SSCenteredRectInRect(_:_:)

**Framework**: Screen Saver  
**Kind**: func

Returns a rectangle.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func SSCenteredRectInRect(_ innerRect: NSRect, _ outerRect: NSRect) -> NSRect
```

#### Return Value

A rectangle that’s the same size as `innerRect`, but is centered inside `outerRect`.

## Parameters

- `innerRect`: The rectangle to center.
- `outerRect`: The rectangle to contain  .

## See Also

- [func SSRandomIntBetween(Int32, Int32) -> Int32](ssrandomintbetween(_:_:).md)
  Returns a random integer value.
- [func SSRandomFloatBetween(CGFloat, CGFloat) -> CGFloat](ssrandomfloatbetween(_:_:).md)
  Returns a random float value.
- [func SSRandomPointForSizeWithinRect(NSSize, NSRect) -> NSPoint](ssrandompointforsizewithinrect(_:_:).md)
  Returns a random point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screensaver/sscenteredrectinrect(_:_:))*