# SSRandomFloatBetween(_:_:)

**Framework**: Screen Saver  
**Kind**: func

Returns a random float value.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func SSRandomFloatBetween(_ a: CGFloat, _ b: CGFloat) -> CGFloat
```

#### Return Value

A random floating-point value between the values `a` and `b`, inclusive.

#### Discussion

The Screen Saver framework automatically seeds the `random()` C function to generate the number.

## Parameters

- `a`: The first floating-point value.
- `b`: The second floating-point value.

## See Also

- [func SSRandomIntBetween(Int32, Int32) -> Int32](ssrandomintbetween(_:_:).md)
  Returns a random integer value.
- [func SSRandomPointForSizeWithinRect(NSSize, NSRect) -> NSPoint](ssrandompointforsizewithinrect(_:_:).md)
  Returns a random point.
- [func SSCenteredRectInRect(NSRect, NSRect) -> NSRect](sscenteredrectinrect(_:_:).md)
  Returns a rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screensaver/ssrandomfloatbetween(_:_:))*