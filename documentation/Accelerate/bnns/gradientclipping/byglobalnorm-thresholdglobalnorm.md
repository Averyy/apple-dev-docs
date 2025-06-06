# BNNS.GradientClipping.byGlobalNorm(threshold:globalNorm:)

**Framework**: Accelerate  
**Kind**: case

A constant that indicates that the operation clips gradients to a specified global Euclidean norm.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS ?+
- watchOS 8.0+

## Declaration

```swift
case byGlobalNorm(threshold: Float, globalNorm: Float = 0)
```

## Parameters

- `threshold`: The maximum Euclidean norm.
- `globalNorm`: An optional value for a known global Euclidean norm. Set to   to specify that the function computes the norm.

## See Also

- [BNNS.GradientClipping.none](bnns/gradientclipping/none.md)
  A constant that indicates that the operation doesn’t clip gradients.
- [case byValue(bounds: ClosedRange<Float>)](bnns/gradientclipping/byvalue(bounds:).md)
  A constant that indicates that the operation clips gradients to a specified range.
- [BNNS.GradientClipping.byNorm(threshold:)](bnns/gradientclipping/bynorm(threshold:).md)
  A constant that indicates that the operation clips gradients to a specified Euclidean norm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/gradientclipping/byglobalnorm(threshold:globalnorm:))*