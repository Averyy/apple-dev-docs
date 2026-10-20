# BNNSOptimizerClippingByGlobalNorm

**Framework**: Accelerate  
**Kind**: var  
**Role**: Global Variable

A constant that specifes clipping to a maximum global Euclidean norm.

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
var BNNSOptimizerClippingByGlobalNorm: BNNSOptimizerClippingFunction { get }
```

```c
BNNSOptimizerClippingByGlobalNorm
```

## See Also

### Related Documentation
- [func BNNSClipByGlobalNorm(UnsafeMutablePointer<UnsafeMutablePointer<BNNSNDArrayDescriptor>>, UnsafeMutablePointer<UnsafePointer<BNNSNDArrayDescriptor>>, Int, Float, Float) -> Int32](./bnnsclipbyglobalnorm%28_,_,_,_,_%29.md)
  Clips a tensor’s values to a maximum global Euclidean norm.
### Clipping Functions
- [init(UInt32)](./bnnsoptimizerclippingfunction/init%28_%29.md)
  Creates a new instance with the specified raw value.
- [init(rawValue: UInt32)](./bnnsoptimizerclippingfunction/init%28rawvalue%29.md)
  Creates a new instance with the specified raw value.
- [var rawValue: UInt32](./bnnsoptimizerclippingfunction/rawvalue.md)
  The corresponding value of the raw type.
- [var BNNSOptimizerClippingNone: BNNSOptimizerClippingFunction](./bnnsoptimizerclippingnone.md)
  A constant that specifes no clipping.
- [var BNNSOptimizerClippingByValue: BNNSOptimizerClippingFunction](./bnnsoptimizerclippingbyvalue.md)
  A constant that specifes clipping to minimum and maximum values.
- [var BNNSOptimizerClippingByNorm: BNNSOptimizerClippingFunction](./bnnsoptimizerclippingbynorm.md)
  A constant that specifes clipping to a maximum Euclidean norm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsoptimizerclippingbyglobalnorm)*