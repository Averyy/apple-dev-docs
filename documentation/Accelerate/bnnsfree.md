# BNNSFree

**Framework**: Accelerate  
**Kind**: typealias  
**Role**: Type Alias

A type-alias for a user-provided memory deallocation function.

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
typealias BNNSFree = (UnsafeMutableRawPointer?) -> Void
```

```c
typedef void (*)(void *) BNNSFree;
```

## See Also

### General filters
- [typealias BNNSFilter](./bnnsfilter.md)
  An opaque type that represents a filter.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsfree)*