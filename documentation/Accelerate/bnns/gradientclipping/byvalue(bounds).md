# BNNS.GradientClipping.byValue(bounds:)

**Framework**: Accelerate  
**Kind**: case  
**Role**: Case

A constant that indicates that the operation clips gradients to a specified range.

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
case byValue(bounds: ClosedRange<Float>)
```

## Parameters

- `bounds`: The minimum and maximum clipping values.

## See Also

### Gradient Clipping Functions
- [BNNS.GradientClipping.none](./none.md)
  A constant that indicates that the operation doesn’t clip gradients.
- [BNNS.GradientClipping.byNorm(threshold:)](./bynorm%28threshold%29.md)
  A constant that indicates that the operation clips gradients to a specified Euclidean norm.
- [BNNS.GradientClipping.byGlobalNorm(threshold:globalNorm:)](./byglobalnorm%28threshold,globalnorm%29.md)
  A constant that indicates that the operation clips gradients to a specified global Euclidean norm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/gradientclipping/byvalue(bounds:))*