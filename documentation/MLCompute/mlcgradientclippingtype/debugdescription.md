# debugDescription

**Framework**: ML Compute  
**Kind**: property  
**Role**: Instance Property

A textual description of the gradient clipping type, suitable for debugging.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+

## Declaration

```swift
var debugDescription: String { get }
```

```c
NSString *MLCGradientClippingTypeDebugDescription(MLCGradientClippingType gradientClippingType);
```

## See Also

### Gradient Clipping Types
- [MLCGradientClippingType.byValue](./byvalue.md)
  An option that clips by value.
- [MLCGradientClippingType.byNorm](./bynorm.md)
  An option that clips by norm.
- [MLCGradientClippingType.byGlobalNorm](./byglobalnorm.md)
  An option that clips by global norm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcgradientclippingtype/debugdescription)*