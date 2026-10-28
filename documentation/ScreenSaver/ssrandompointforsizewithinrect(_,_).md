# SSRandomPointForSizeWithinRect(_:_:)

**Framework**: Screen Saver  
**Kind**: func  
**Role**: Function

Returns a random point.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func SSRandomPointForSizeWithinRect(_ size: NSSize, _ rect: NSRect) -> NSPoint
```

```c
static NSPoint SSRandomPointForSizeWithinRect(NSSize size, NSRect rect);
```

## Return Value

A random point within `rect`, constrained within `(rect.size - size)` from `rect`’s origin.

## Discussion

The Screen Saver framework automatically seeds the `random()` C function to generate the point.

## Parameters

- `size`: The horizontal and vertical amounts to subtract from the rectangle’s size.
- `rect`: The rectangle to contain the point.

## See Also

### Utilities
- [func SSRandomIntBetween(Int32, Int32) -> Int32](./ssrandomintbetween%28_,_%29.md)
  Returns a random integer value.
- [func SSRandomFloatBetween(CGFloat, CGFloat) -> CGFloat](./ssrandomfloatbetween%28_,_%29.md)
  Returns a random float value.
- [func SSCenteredRectInRect(NSRect, NSRect) -> NSRect](./sscenteredrectinrect%28_,_%29.md)
  Returns a rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screensaver/ssrandompointforsizewithinrect(_:_:))*