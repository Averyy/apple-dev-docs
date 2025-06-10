# NSBezierPath.WindingRule.nonZero

**Framework**: AppKit  
**Kind**: case

Specifies the non-zero winding rule.

**Availability**:
- macOS ?+

## Declaration

```swift
case nonZero
```

#### Discussion

Count each left-to-right path as +1, and each right-to-left path as -1. If the sum of all crossings is 0, the point is outside the path. If the sum is nonzero, the point is inside the path and the region containing it is filled. This is the default winding rule.

## See Also

- [NSBezierPath.WindingRule.evenOdd](nsbezierpath/windingrule-swift.enum/evenodd.md)
  Specifies the even-odd winding rule.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/windingrule-swift.enum/nonzero)*