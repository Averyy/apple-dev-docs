# NSBezierPath.WindingRule.evenOdd

**Framework**: AppKit  
**Kind**: case  
**Role**: Case

Specifies the even-odd winding rule.

**Availability**:
- macOS

## Declaration

```swift
case evenOdd
```

```c
NSWindingRuleEvenOdd
```

## Discussion

Count the total number of path crossings. If the number of crossings is even, the point is outside the path. If the number of crossings is odd, the point is inside the path and the region that contains it is filled.

## See Also

### Constants
- [NSBezierPath.WindingRule.nonZero](./nonzero.md)
  Specifies the non-zero winding rule.
- [NSNonZeroWindingRule](../../nsnonzerowindingrule.md)
  Specifies the non-zero winding rule.
- [NSEvenOddWindingRule](../../nsevenoddwindingrule.md)
  Specifies the even-odd winding rule.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/windingrule-swift.enum/evenodd)*