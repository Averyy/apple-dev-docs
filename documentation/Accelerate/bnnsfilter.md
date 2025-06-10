# BNNSFilter

**Framework**: Accelerate  
**Kind**: typealias

An opaque type that represents a filter.

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
typealias BNNSFilter = UnsafeMutableRawPointer
```

## See Also

- [Applying Filters](applying-filters.md)
- [class Layer](bnns/layer.md)
  The base class for layer objects that wrap filters and manage deinitialization.
- [class UnaryLayer](bnns/unarylayer.md)
  The base class for layers that accept a single input.
- [class BinaryLayer](bnns/binarylayer.md)
  The base class for layers that accept two inputs.
- [struct BNNSFilterParameters](bnnsfilterparameters.md)
  A structure that contains common filter parameters.
- [func BNNSFilterDestroy(BNNSFilter?)](bnnsfilterdestroy(_:).md)
  Destroys the specified filter, releasing all resources allocated for it.
- [typealias BNNSAlloc](bnnsalloc.md)
  A type-alias for a user-provided memory allocation function.
- [typealias BNNSFree](bnnsfree.md)
  A type-alias for a user-provided memory deallocation function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsfilter)*