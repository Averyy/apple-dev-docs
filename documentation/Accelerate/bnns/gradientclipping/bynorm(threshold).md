# BNNS.GradientClipping.byNorm(threshold:)

**Framework**: Accelerate  
**Kind**: case  
**Role**: Case

A constant that indicates that the operation clips gradients to a specified Euclidean norm.

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
case byNorm(threshold: Float)
```

## Parameters

- `threshold`: The maximum Euclidean norm.

## See Also

### Gradient Clipping Functions
- [BNNS.GradientClipping.none](./none.md)
  A constant that indicates that the operation doesn’t clip gradients.
- [case byValue(bounds: ClosedRange<Float>)](./byvalue%28bounds%29.md)
  A constant that indicates that the operation clips gradients to a specified range.
- [BNNS.GradientClipping.byGlobalNorm(threshold:globalNorm:)](./byglobalnorm%28threshold,globalnorm%29.md)
  A constant that indicates that the operation clips gradients to a specified global Euclidean norm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/gradientclipping/bynorm(threshold:))*