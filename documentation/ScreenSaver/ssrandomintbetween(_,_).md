# SSRandomIntBetween(_:_:)

**Framework**: Screen Saver  
**Kind**: func  
**Role**: Function

Returns a random integer value.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func SSRandomIntBetween(_ a: Int32, _ b: Int32) -> Int32
```

```c
static int SSRandomIntBetween(int a, int b);
```

## Discussion

The Screen Saver framework automatically seeds the `random()` C function to generate the number.

## Parameters

- `a`: The first integer value.
- `b`: The second integer value.

## See Also

### Utilities
- [func SSRandomFloatBetween(CGFloat, CGFloat) -> CGFloat](./ssrandomfloatbetween%28_,_%29.md)
  Returns a random float value.
- [func SSRandomPointForSizeWithinRect(NSSize, NSRect) -> NSPoint](./ssrandompointforsizewithinrect%28_,_%29.md)
  Returns a random point.
- [func SSCenteredRectInRect(NSRect, NSRect) -> NSRect](./sscenteredrectinrect%28_,_%29.md)
  Returns a rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screensaver/ssrandomintbetween(_:_:))*