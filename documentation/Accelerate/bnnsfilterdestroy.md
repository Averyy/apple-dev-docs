# BNNSFilterDestroy(_:)

**Framework**: Accelerate  
**Kind**: func

Destroys the specified filter, releasing all resources allocated for it.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func BNNSFilterDestroy(_ filter: BNNSFilter?)
```

## Parameters

- `filter`: A BNNSFilter object.

## See Also

- [typealias BNNSFilter](bnnsfilter.md)
  An opaque type that represents a filter.
- [Applying Filters](applying-filters.md)
- [class Layer](bnns/layer.md)
  The base class for layer objects that wrap filters and manage deinitialization.
- [class UnaryLayer](bnns/unarylayer.md)
  The base class for layers that accept a single input.
- [class BinaryLayer](bnns/binarylayer.md)
  The base class for layers that accept two inputs.
- [struct BNNSFilterParameters](bnnsfilterparameters.md)
  A structure that contains common filter parameters.
- [typealias BNNSAlloc](bnnsalloc.md)
  A type-alias for a user-provided memory allocation function.
- [typealias BNNSFree](bnnsfree.md)
  A type-alias for a user-provided memory deallocation function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsfilterdestroy(_:))*