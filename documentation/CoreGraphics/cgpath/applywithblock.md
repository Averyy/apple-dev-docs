# applyWithBlock(_:)

**Framework**: Core Graphics  
**Kind**: method

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
func applyWithBlock(_ block: (UnsafePointer<CGPathElement>) -> Void)
```

## See Also

- [func componentsSeparated(using: CGPathFillRule) -> [CGPath]](cgpath/componentsseparated(using:).md)
- [func flattened(threshold: CGFloat) -> CGPath](cgpath/flattened(threshold:).md)
- [func intersection(CGPath, using: CGPathFillRule) -> CGPath](cgpath/intersection(_:using:).md)
- [func intersects(CGPath, using: CGPathFillRule) -> Bool](cgpath/intersects(_:using:).md)
- [func lineIntersection(CGPath, using: CGPathFillRule) -> CGPath](cgpath/lineintersection(_:using:).md)
- [func lineSubtracting(CGPath, using: CGPathFillRule) -> CGPath](cgpath/linesubtracting(_:using:).md)
- [func normalized(using: CGPathFillRule) -> CGPath](cgpath/normalized(using:).md)
- [func subtracting(CGPath, using: CGPathFillRule) -> CGPath](cgpath/subtracting(_:using:).md)
- [func symmetricDifference(CGPath, using: CGPathFillRule) -> CGPath](cgpath/symmetricdifference(_:using:).md)
- [func union(CGPath, using: CGPathFillRule) -> CGPath](cgpath/union(_:using:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpath/applywithblock(_:))*