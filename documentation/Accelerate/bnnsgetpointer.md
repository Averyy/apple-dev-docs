# BNNSGetPointer(_:_:)

**Framework**: Accelerate  
**Kind**: func

Returns an n-dimensional array descriptor that contains a reference to a filter-data member.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
func BNNSGetPointer(_ filter: BNNSFilter?, _ target: BNNSPointerSpecifier) -> BNNSNDArrayDescriptor
```

## See Also

- [static func copy(BNNSNDArrayDescriptor, to: BNNSNDArrayDescriptor, filterParameters: BNNSFilterParameters?) throws](bnns/copy(_:to:filterparameters:).md)
  Copies the contents of an n-dimensional array descriptor to another descriptor of the same shape.
- [static func transpose(input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, firstTransposeAxis: Int, secondTransposeAxis: Int, filterParameters: BNNSFilterParameters?) throws](bnns/transpose(input:output:firsttransposeaxis:secondtransposeaxis:filterparameters:).md)
  Transposes a tensor by swapping two of its dimensions.
- [func BNNSCopy(UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSFilterParameters>?) -> Int32](bnnscopy(_:_:_:).md)
  Copies the contents of an n-dimensional array descriptor to another of the same shape.
- [func BNNSTranspose(UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, Int, Int, UnsafePointer<BNNSFilterParameters>?) -> Int32](bnnstranspose(_:_:_:_:_:).md)
  Transposes a tensor by swapping two of its dimensions.
- [struct BNNSPointerSpecifier](bnnspointerspecifier.md)
  Constants that specify which pointer the BNNS get filter function returns.
- [class GramLayer](bnns/gramlayer.md)
  A layer object that wraps a Gram matrix filter and manages its deinitialization.
- [struct BNNSLayerParametersGram](bnnslayerparametersgram.md)
  A set of parameters that define a Gram matrix layer.
- [func BNNSFilterCreateLayerGram(UnsafePointer<BNNSLayerParametersGram>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](bnnsfiltercreatelayergram(_:_:).md)
  Returns a new Gram matrix layer.
- [static func clip(to: ClosedRange<Float>, input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor) throws](bnns/clip(to:input:output:).md)
  Clips the input tensor to a closed range and writes the result to the output tensor.
- [static func clipByNorm(threshold: Float, input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, axes: [Int]?) throws](bnns/clipbynorm(threshold:input:output:axes:).md)
  Clips the input tensor to a Euclidean norm and writes the result to the output tensor.
- [static func clipByGlobalNorm(threshold: Float, inputs: [BNNSNDArrayDescriptor], outputs: [BNNSNDArrayDescriptor], globalNorm: Float) throws](bnns/clipbyglobalnorm(threshold:inputs:outputs:globalnorm:).md)
  Clips the input tensors to a global Euclidean norm and writes the result to the output tensors.
- [func BNNSClipByValue(UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, Float, Float) -> Int32](bnnsclipbyvalue(_:_:_:_:).md)
  Clips a tensor’s values to the specified minimum and maximum values.
- [func BNNSClipByNorm(UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, Float, UInt32) -> Int32](bnnsclipbynorm(_:_:_:_:).md)
  Clips a tensor’s values to a maximum Euclidean norm.
- [func BNNSClipByGlobalNorm(UnsafeMutablePointer<UnsafeMutablePointer<BNNSNDArrayDescriptor>>, UnsafeMutablePointer<UnsafePointer<BNNSNDArrayDescriptor>>, Int, Float, Float) -> Int32](bnnsclipbyglobalnorm(_:_:_:_:_:).md)
  Clips a tensor’s values to a maximum global Euclidean norm.
- [static func copyBandPart(BNNSNDArrayDescriptor, to: BNNSNDArrayDescriptor, lowerBandCount: Int?, upperBandCount: Int?, filterParameters: BNNSFilterParameters?) throws](bnns/copybandpart(_:to:lowerbandcount:upperbandcount:filterparameters:).md)
  Copies the specified subdiagonals and superdiagonals of a matrix, and sets other elements to zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgetpointer(_:_:))*