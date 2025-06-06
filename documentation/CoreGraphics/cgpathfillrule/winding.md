# CGPathFillRule.winding

**Framework**: Core Graphics  
**Kind**: case

A rule that considers a region to be interior to a path if the winding number for that region is nonzero.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst ?+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
case winding
```

#### Discussion

This rule plots a ray from any region to be evaluated toward the bounds of the drawing, then counts the closed path elements that the ray crosses: +1 for counterclockwise paths, -1 for clockwise. The rule defines interior regions as those where the sum of crossings is nonzero, and exterior regions as those where the sum of crossings is zero.

## See Also

- [CGPathFillRule.evenOdd](cgpathfillrule/evenodd.md)
  A rule that considers a region to be interior to a path based on the number of times it is enclosed by path elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpathfillrule/winding)*