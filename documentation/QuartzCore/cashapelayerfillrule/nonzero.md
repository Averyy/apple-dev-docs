# nonZero

**Framework**: Core Animation  
**Kind**: property

Specifies the non-zero winding rule. Count each left-to-right path as +1 and each right-to-left path as -1. If the sum of all crossings is 0, the point is outside the path. If the sum is nonzero, the point is inside the path and the region containing it is filled.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
static let nonZero: CAShapeLayerFillRule
```

## See Also

- [static let evenOdd: CAShapeLayerFillRule](cashapelayerfillrule/evenodd.md)
  Specifies the even-odd winding rule. Count the total number of path crossings. If the number of crossings is even, the point is outside the path. If the number of crossings is odd, the point is inside the path and the region containing it should be filled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/cashapelayerfillrule/nonzero)*