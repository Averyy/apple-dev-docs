# SSRandomIntBetween(_:_:)

**Framework**: Screen Saver  
**Kind**: func

Returns a random integer value.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func SSRandomIntBetween(_ a: Int32, _ b: Int32) -> Int32
```

#### Discussion

The Screen Saver framework automatically seeds the `random()` C function to generate the number.

## Parameters

- `a`: The first integer value.
- `b`: The second integer value.

## See Also

- [func SSRandomFloatBetween(CGFloat, CGFloat) -> CGFloat](ssrandomfloatbetween(_:_:).md)
  Returns a random float value.
- [func SSRandomPointForSizeWithinRect(NSSize, NSRect) -> NSPoint](ssrandompointforsizewithinrect(_:_:).md)
  Returns a random point.
- [func SSCenteredRectInRect(NSRect, NSRect) -> NSRect](sscenteredrectinrect(_:_:).md)
  Returns a rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screensaver/ssrandomintbetween(_:_:))*