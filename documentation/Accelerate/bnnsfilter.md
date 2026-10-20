# BNNSFilter

**Framework**: Accelerate  
**Kind**: typealias  
**Role**: Type Alias

An opaque type that represents a filter.

**Availability**:
- iOS 10.0+ - Deprecated in 18.0
- iPadOS 10.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.12+ - Deprecated in 15.0
- tvOS 10.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 3.0+ - Deprecated in 11.0

> **Deprecated**: Use BNNSGraph* APIs

## Declaration

```swift
typealias BNNSFilter = UnsafeMutableRawPointer
```

```c
typedef void * BNNSFilter;
```

## See Also

### General filters
- [Applying Filters](./applying-filters.md)
- [class Layer](./bnns/layer.md)
  The base class for layer objects that wrap filters and manage deinitialization.
- [class UnaryLayer](./bnns/unarylayer.md)
  The base class for layers that accept a single input.
- [class BinaryLayer](./bnns/binarylayer.md)
  The base class for layers that accept two inputs.
- [struct BNNSFilterParameters](./bnnsfilterparameters.md)
  A structure that contains common filter parameters.
- [func BNNSFilterDestroy(BNNSFilter?)](./bnnsfilterdestroy%28_%29.md)
  Destroys the specified filter, releasing all resources allocated for it.
- [typealias BNNSAlloc](./bnnsalloc.md)
  A type-alias for a user-provided memory allocation function.
- [typealias BNNSFree](./bnnsfree.md)
  A type-alias for a user-provided memory deallocation function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsfilter)*