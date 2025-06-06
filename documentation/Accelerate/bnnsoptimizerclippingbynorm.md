# BNNSOptimizerClippingByNorm

**Framework**: Accelerate  
**Kind**: var

A constant that specifes clipping to a maximum Euclidean norm.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
var BNNSOptimizerClippingByNorm: BNNSOptimizerClippingFunction { get }
```

## See Also

- [func BNNSClipByNorm(UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, Float, UInt32) -> Int32](bnnsclipbynorm(_:_:_:_:).md)
  Clips a tensor’s values to a maximum Euclidean norm.
- [init(UInt32)](bnnsoptimizerclippingfunction/init(_:).md)
  Creates a new instance with the specified raw value.
- [init(rawValue: UInt32)](bnnsoptimizerclippingfunction/init(rawvalue:).md)
  Creates a new instance with the specified raw value.
- [var rawValue: UInt32](bnnsoptimizerclippingfunction/rawvalue.md)
  The corresponding value of the raw type.
- [var BNNSOptimizerClippingNone: BNNSOptimizerClippingFunction](bnnsoptimizerclippingnone.md)
  A constant that specifes no clipping.
- [var BNNSOptimizerClippingByValue: BNNSOptimizerClippingFunction](bnnsoptimizerclippingbyvalue.md)
  A constant that specifes clipping to minimum and maximum values.
- [var BNNSOptimizerClippingByGlobalNorm: BNNSOptimizerClippingFunction](bnnsoptimizerclippingbyglobalnorm.md)
  A constant that specifes clipping to a maximum global Euclidean norm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsoptimizerclippingbynorm)*