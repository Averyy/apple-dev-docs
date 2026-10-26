# BNNSPoolingFunction

**Framework**: Accelerate  
**Kind**: struct  
**Role**: Structure

Constants that describe pooling functions.

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
struct BNNSPoolingFunction
```

```c
typedef enum { ... } BNNSPoolingFunction;
```

## Topics

### Pooling Functions
- [static var max: BNNSPoolingFunction](./bnnspoolingfunction/max.md)
  A function for pooling that computes the maximum of each element in the pooling kernel.
- [static var average: BNNSPoolingFunction](./bnnspoolingfunction/average.md)
  A function for pooling that computes the average of each element in the pooling kernel.
### Raw Values
- [init(UInt32)](./bnnspoolingfunction/init%28_%29.md)
- [init(rawValue: UInt32)](./bnnspoolingfunction/init%28rawvalue%29.md)
- [var rawValue: UInt32](./bnnspoolingfunction/rawvalue.md)
- [var BNNSPoolingFunctionUnMax: BNNSPoolingFunction](./bnnspoolingfunctionunmax.md)
  A function for pooling that’s the partial inverse of max pooling and sets all nonmaximal values to zero.
- [var BNNSPoolingFunctionAverageCountIncludePadding: BNNSPoolingFunction](./bnnspoolingfunctionaveragecountincludepadding.md)
  A function for pooling that computes the average of each element in the pooling kernel, including zero-padding.
- [var BNNSPoolingFunctionAverageCountExcludePadding: BNNSPoolingFunction](./bnnspoolingfunctionaveragecountexcludepadding.md)
  A function for pooling that computes the average of each element in the pooling kernel, excluding zero-padding.
- [var BNNSPoolingFunctionL2Norm: BNNSPoolingFunction](./bnnspoolingfunctionl2norm.md)
  A function for pooling that computes the square root of the sum of squares of each element in the pooling kernel.
- [BNNSPoolingFunctionMax](./bnnspoolingfunction/bnnspoolingfunctionmax.md)
  A function for pooling that computes the maximum of each element in the pooling kernel.
- [BNNSPoolingFunctionAverage](./bnnspoolingfunction/bnnspoolingfunctionaverage.md)
  A function for pooling that computes the average of each element in the pooling kernel.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Pooling layers
- [struct BNNSPoolingLayerParameters](./bnnspoolinglayerparameters.md)
  A structure containing pooling layer parameters.
- [func BNNSFilterCreatePoolingLayer(UnsafePointer<BNNSImageStackDescriptor>, UnsafePointer<BNNSImageStackDescriptor>, UnsafePointer<BNNSPoolingLayerParameters>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](./bnnsfiltercreatepoolinglayer%28_,_,_,_%29.md)
  Returns a pooling  filter, initialized with input, output, layer, and filter parameters.
- [class PoolingLayer](./bnns/poolinglayer.md)
  A layer object that wraps a pooling filter and manages its deinitialization.
- [var BNNSPoolingFunctionAverage: BNNSPoolingFunction](./bnnspoolingfunctionaverage.md)
- [var BNNSPoolingFunctionMax: BNNSPoolingFunction](./bnnspoolingfunctionmax.md)
- [struct BNNSLayerParametersPooling](./bnnslayerparameterspooling.md)
  A structure that contains the parameters of a pooling layer.
- [func BNNSFilterCreateLayerPooling(UnsafePointer<BNNSLayerParametersPooling>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](./bnnsfiltercreatelayerpooling%28_,_%29.md)
  Returns a new pooling layer.
- [func BNNSPoolingFilterApplyBatch(BNNSFilter?, Int, UnsafeRawPointer, Int, UnsafeMutableRawPointer, Int, UnsafeMutablePointer<Int>?, Int) -> Int32](./bnnspoolingfilterapplybatch%28_,_,_,_,_,_,_,_%29.md)
  Applies a pooling filter to a set of input objects, writing the result to a set of output objects.
- [func BNNSPoolingFilterApplyBackwardBatch(BNNSFilter?, Int, UnsafeRawPointer?, Int, UnsafeMutablePointer<BNNSNDArrayDescriptor>?, Int, UnsafeRawPointer?, Int, UnsafeMutablePointer<BNNSNDArrayDescriptor>, Int, UnsafeMutablePointer<BNNSNDArrayDescriptor>?, UnsafePointer<Int>?, Int) -> Int32](./bnnspoolingfilterapplybackwardbatch%28_,_,_,_,_,_,_,_,_,_,_,_,_%29.md)
  Applies a pooling filter backward to generate gradients.
- [func BNNSPoolingFilterApplyBatchEx(BNNSFilter?, Int, UnsafeRawPointer, Int, UnsafeMutableRawPointer, Int, BNNSDataType, UnsafeMutableRawPointer?, Int) -> Int32](./bnnspoolingfilterapplybatchex%28_,_,_,_,_,_,_,_,_%29.md)
  Applies a pooling filter to a set of input objects with support for multiple data types for indices.
- [func BNNSPoolingFilterApplyBackwardBatchEx(BNNSFilter?, Int, UnsafeRawPointer?, Int, UnsafeMutablePointer<BNNSNDArrayDescriptor>?, Int, UnsafeRawPointer?, Int, UnsafeMutablePointer<BNNSNDArrayDescriptor>, Int, UnsafeMutablePointer<BNNSNDArrayDescriptor>?, BNNSDataType, UnsafeRawPointer?, Int) -> Int32](./bnnspoolingfilterapplybackwardbatchex%28_,_,_,_,_,_,_,_,_,_,_,_,_,_%29.md)
  Applies a pooling filter backward to generate gradients with support for multiple data types for indices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnspoolingfunction)*