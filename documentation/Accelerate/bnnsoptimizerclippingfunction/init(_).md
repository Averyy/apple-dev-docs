# init(_:)

**Framework**: Accelerate  
**Kind**: init  
**Role**: Initializer

Creates a new instance with the specified raw value.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
init(_ rawValue: UInt32)
```

## See Also

### Clipping Functions
- [init(rawValue: UInt32)](./init%28rawvalue%29.md)
  Creates a new instance with the specified raw value.
- [var rawValue: UInt32](./rawvalue.md)
  The corresponding value of the raw type.
- [var BNNSOptimizerClippingNone: BNNSOptimizerClippingFunction](../bnnsoptimizerclippingnone.md)
  A constant that specifes no clipping.
- [var BNNSOptimizerClippingByValue: BNNSOptimizerClippingFunction](../bnnsoptimizerclippingbyvalue.md)
  A constant that specifes clipping to minimum and maximum values.
- [var BNNSOptimizerClippingByNorm: BNNSOptimizerClippingFunction](../bnnsoptimizerclippingbynorm.md)
  A constant that specifes clipping to a maximum Euclidean norm.
- [var BNNSOptimizerClippingByGlobalNorm: BNNSOptimizerClippingFunction](../bnnsoptimizerclippingbyglobalnorm.md)
  A constant that specifes clipping to a maximum global Euclidean norm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsoptimizerclippingfunction/init(_:))*