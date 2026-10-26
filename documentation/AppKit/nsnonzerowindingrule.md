# NSNonZeroWindingRule

**Framework**: AppKit  
**Kind**: var  
**Role**: Global Variable

Specifies the non-zero winding rule.

**Availability**:
- macOS 10.0+ - Deprecated in 11.0

> **Deprecated**: Use [`NSBezierPath.WindingRule.nonZero`](./nsbezierpath/windingrule-swift.enum/nonzero.md) instead.

## Declaration

```c
static const NSWindingRule NSNonZeroWindingRule;
```

#### Discussion

Count each left-to-right path as +1, and each right-to-left path as -1. If the sum of all crossings is 0, the point is outside the path. If the sum is nonzero, the point is inside the path and the region containing it is filled. This is the default winding rule.

## See Also

### Constants
- [NSBezierPath.WindingRule.nonZero](./nsbezierpath/windingrule-swift.enum/nonzero.md)
  Specifies the non-zero winding rule.
- [NSBezierPath.WindingRule.evenOdd](./nsbezierpath/windingrule-swift.enum/evenodd.md)
  Specifies the even-odd winding rule.
- [NSEvenOddWindingRule](./nsevenoddwindingrule.md)
  Specifies the even-odd winding rule.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsnonzerowindingrule)*