# NSEvenOddWindingRule

**Framework**: AppKit  
**Kind**: var  
**Role**: Global Variable

Specifies the even-odd winding rule.

**Availability**:
- macOS 10.0+ - Deprecated in 11.0

> **Deprecated**: Use [`NSBezierPath.WindingRule.evenOdd`](./nsbezierpath/windingrule-swift.enum/evenodd.md) instead.

## Declaration

```c
static const NSWindingRule NSEvenOddWindingRule;
```

#### Discussion

Count the total number of path crossings. If the number of crossings is even, the point is outside the path. If the number of crossings is odd, the point is inside the path and the region that contains it is filled.

## See Also

### Constants
- [NSBezierPath.WindingRule.nonZero](./nsbezierpath/windingrule-swift.enum/nonzero.md)
  Specifies the non-zero winding rule.
- [NSBezierPath.WindingRule.evenOdd](./nsbezierpath/windingrule-swift.enum/evenodd.md)
  Specifies the even-odd winding rule.
- [NSNonZeroWindingRule](./nsnonzerowindingrule.md)
  Specifies the non-zero winding rule.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevenoddwindingrule)*