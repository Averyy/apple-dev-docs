# BNNS.GradientClipping.none

**Framework**: Accelerate  
**Kind**: case  
**Role**: Case

A constant that indicates that the operation doesn’t clip gradients.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS
- watchOS 8.0+

## Declaration

```swift
case none
```

## See Also

### Gradient Clipping Functions
- [case byValue(bounds: ClosedRange<Float>)](./byvalue%28bounds%29.md)
  A constant that indicates that the operation clips gradients to a specified range.
- [BNNS.GradientClipping.byNorm(threshold:)](./bynorm%28threshold%29.md)
  A constant that indicates that the operation clips gradients to a specified Euclidean norm.
- [BNNS.GradientClipping.byGlobalNorm(threshold:globalNorm:)](./byglobalnorm%28threshold,globalnorm%29.md)
  A constant that indicates that the operation clips gradients to a specified global Euclidean norm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/gradientclipping/none)*