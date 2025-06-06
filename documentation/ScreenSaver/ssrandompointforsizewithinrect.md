# SSRandomPointForSizeWithinRect(_:_:)

**Framework**: Screen Saver  
**Kind**: func

Returns a random point.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func SSRandomPointForSizeWithinRect(_ size: NSSize, _ rect: NSRect) -> NSPoint
```

#### Return Value

A random point within `rect`, constrained within `(rect.size - size)` from `rect`’s origin.

#### Discussion

The Screen Saver framework automatically seeds the `random()` C function to generate the point.

## Parameters

- `size`: The horizontal and vertical amounts to subtract from the rectangle’s size.
- `rect`: The rectangle to contain the point.

## See Also

- [func SSRandomIntBetween(Int32, Int32) -> Int32](ssrandomintbetween(_:_:).md)
  Returns a random integer value.
- [func SSRandomFloatBetween(CGFloat, CGFloat) -> CGFloat](ssrandomfloatbetween(_:_:).md)
  Returns a random float value.
- [func SSCenteredRectInRect(NSRect, NSRect) -> NSRect](sscenteredrectinrect(_:_:).md)
  Returns a rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screensaver/ssrandompointforsizewithinrect(_:_:))*