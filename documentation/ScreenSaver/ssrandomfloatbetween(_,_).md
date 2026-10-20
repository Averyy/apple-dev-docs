# SSRandomFloatBetween(_:_:)

**Framework**: Screen Saver  
**Kind**: func  
**Role**: Function

Returns a random float value.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func SSRandomFloatBetween(_ a: CGFloat, _ b: CGFloat) -> CGFloat
```

```c
static CGFloat SSRandomFloatBetween(CGFloat a, CGFloat b);
```

#### Return Value

A random floating-point value between the values `a` and `b`, inclusive.

#### Discussion

The Screen Saver framework automatically seeds the `random()` C function to generate the number.

## Parameters

- `a`: The first floating-point value.
- `b`: The second floating-point value.

## See Also

### Utilities
- [func SSRandomIntBetween(Int32, Int32) -> Int32](./ssrandomintbetween%28_,_%29.md)
  Returns a random integer value.
- [func SSRandomPointForSizeWithinRect(NSSize, NSRect) -> NSPoint](./ssrandompointforsizewithinrect%28_,_%29.md)
  Returns a random point.
- [func SSCenteredRectInRect(NSRect, NSRect) -> NSRect](./sscenteredrectinrect%28_,_%29.md)
  Returns a rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screensaver/ssrandomfloatbetween(_:_:))*