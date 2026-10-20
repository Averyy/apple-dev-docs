# applyWithBlock(_:)

**Framework**: Core Graphics  
**Kind**: method  
**Role**: Instance Method

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

```c
extern void CGPathApplyWithBlock(CGPathRef path, CGPathApplyBlock block);
```

## See Also

### Instance Methods
- [func componentsSeparated(using: CGPathFillRule) -> [CGPath]](./componentsseparated%28using%29.md)
- [func flattened(threshold: CGFloat) -> CGPath](./flattened%28threshold%29.md)
- [func intersection(CGPath, using: CGPathFillRule) -> CGPath](./intersection%28_,using%29.md)
- [func intersects(CGPath, using: CGPathFillRule) -> Bool](./intersects%28_,using%29.md)
- [func lineIntersection(CGPath, using: CGPathFillRule) -> CGPath](./lineintersection%28_,using%29.md)
- [func lineSubtracting(CGPath, using: CGPathFillRule) -> CGPath](./linesubtracting%28_,using%29.md)
- [func normalized(using: CGPathFillRule) -> CGPath](./normalized%28using%29.md)
- [func subtracting(CGPath, using: CGPathFillRule) -> CGPath](./subtracting%28_,using%29.md)
- [func symmetricDifference(CGPath, using: CGPathFillRule) -> CGPath](./symmetricdifference%28_,using%29.md)
- [func union(CGPath, using: CGPathFillRule) -> CGPath](./union%28_,using%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpath/applywithblock(_:))*