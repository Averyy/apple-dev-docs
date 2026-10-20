# Applying Filters

**Framework**: Accelerate  
**Role**: API Collection

## Topics

### Forward Propagation Functions
- [func BNNSFilterApply(BNNSFilter?, UnsafeRawPointer, UnsafeMutableRawPointer) -> Int32](./bnnsfilterapply%28_,_,_%29.md)
  Applies a filter to an input, writing the result to a specified output.
- [func BNNSFilterApplyBatch(BNNSFilter?, Int, UnsafeRawPointer, Int, UnsafeMutableRawPointer, Int) -> Int32](./bnnsfilterapplybatch%28_,_,_,_,_,_%29.md)
  Applies a filter to a set of input objects, writing the result to a set of output objects.
- [func BNNSFilterApplyTwoInput(BNNSFilter?, UnsafeRawPointer, UnsafeRawPointer, UnsafeMutableRawPointer) -> Int32](./bnnsfilterapplytwoinput%28_,_,_,_%29.md)
  Applies a filter to a pair of inputs, writing the result to a specified output.
- [func BNNSFilterApplyTwoInputBatch(BNNSFilter?, Int, UnsafeRawPointer, Int, UnsafeRawPointer, Int, UnsafeMutableRawPointer, Int) -> Int32](./bnnsfilterapplytwoinputbatch%28_,_,_,_,_,_,_,_%29.md)
  Applies a filter to a set of input object pairs, writing the result to a set of output objects.
### Backpropagation Functions
- [func BNNSFilterApplyBackwardBatch(BNNSFilter?, Int, UnsafeRawPointer?, Int, UnsafeMutablePointer<BNNSNDArrayDescriptor>?, Int, UnsafeRawPointer?, Int, UnsafePointer<BNNSNDArrayDescriptor>, Int, UnsafeMutablePointer<BNNSNDArrayDescriptor>?, UnsafeMutablePointer<BNNSNDArrayDescriptor>?) -> Int32](./bnnsfilterapplybackwardbatch%28_,_,_,_,_,_,_,_,_,_,_,_%29.md)
  Applies a filter backward to generate input delta, weights delta and bias delta.
- [func BNNSFilterApplyBackwardTwoInputBatch(BNNSFilter?, Int, UnsafeRawPointer?, Int, UnsafeMutablePointer<BNNSNDArrayDescriptor>?, Int, UnsafeRawPointer?, Int, UnsafeMutablePointer<BNNSNDArrayDescriptor>?, Int, UnsafeRawPointer?, Int, UnsafePointer<BNNSNDArrayDescriptor>, Int, UnsafeMutablePointer<BNNSNDArrayDescriptor>?, UnsafeMutablePointer<BNNSNDArrayDescriptor>?) -> Int32](./bnnsfilterapplybackwardtwoinputbatch%28_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_%29.md)
  Applies a filter backward to generate input deltas, weights delta and bias delta.

## See Also

### General filters
- [typealias BNNSFilter](./bnnsfilter.md)
  An opaque type that represents a filter.
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

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/applying-filters)*