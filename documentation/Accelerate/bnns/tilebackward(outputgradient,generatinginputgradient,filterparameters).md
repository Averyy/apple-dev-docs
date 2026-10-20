# tileBackward(outputGradient:generatingInputGradient:filterParameters:)

**Framework**: Accelerate  
**Kind**: method  
**Role**: Type Method

Applies a tile filter backward to generate an input gradient.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS
- watchOS 9.0+

> **Deprecated**: Use the BNNSGraph API instead.

## Declaration

```swift
static func tileBackward(outputGradient: BNNSNDArrayDescriptor, generatingInputGradient inputGradient: BNNSNDArrayDescriptor, filterParameters: BNNSFilterParameters? = nil) throws
```

## Parameters

- `outputGradient`: The output gradient descriptor.
- `inputGradient`: The input gradient descriptor.
- `filterParameters`: The runtime filter parameters.

## See Also

### Related Documentation
- [func BNNSTileBackward(UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSFilterParameters>?) -> Int32](../bnnstilebackward%28_,_,_%29.md)
  Applies a tile filter backward to generate an input gradient.
### Utility functions
- [static func copy(BNNSNDArrayDescriptor, to: BNNSNDArrayDescriptor, filterParameters: BNNSFilterParameters?) throws](./copy%28_,to,filterparameters%29.md)
  Copies the contents of an n-dimensional array descriptor to another descriptor of the same shape.
- [static func transpose(input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, firstTransposeAxis: Int, secondTransposeAxis: Int, filterParameters: BNNSFilterParameters?) throws](./transpose%28input,output,firsttransposeaxis,secondtransposeaxis,filterparameters%29.md)
  Transposes a tensor by swapping two of its dimensions.
- [func BNNSCopy(UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSFilterParameters>?) -> Int32](../bnnscopy%28_,_,_%29.md)
  Copies the contents of an n-dimensional array descriptor to another of the same shape.
- [func BNNSTranspose(UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, Int, Int, UnsafePointer<BNNSFilterParameters>?) -> Int32](../bnnstranspose%28_,_,_,_,_%29.md)
  Transposes a tensor by swapping two of its dimensions.
- [func BNNSGetPointer(BNNSFilter?, BNNSPointerSpecifier) -> BNNSNDArrayDescriptor](../bnnsgetpointer%28_,_%29.md)
  Returns an n-dimensional array descriptor that contains a reference to a filter-data member.
- [struct BNNSPointerSpecifier](../bnnspointerspecifier.md)
  Constants that specify which pointer the BNNS get filter function returns.
- [class GramLayer](./gramlayer.md)
  A layer object that wraps a Gram matrix filter and manages its deinitialization.
- [struct BNNSLayerParametersGram](../bnnslayerparametersgram.md)
  A set of parameters that define a Gram matrix layer.
- [func BNNSFilterCreateLayerGram(UnsafePointer<BNNSLayerParametersGram>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](../bnnsfiltercreatelayergram%28_,_%29.md)
  Returns a new Gram matrix layer.
- [static func clip(to: ClosedRange<Float>, input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor) throws](./clip%28to,input,output%29.md)
  Clips the input tensor to a closed range and writes the result to the output tensor.
- [static func clipByNorm(threshold: Float, input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, axes: [Int]?) throws](./clipbynorm%28threshold,input,output,axes%29.md)
  Clips the input tensor to a Euclidean norm and writes the result to the output tensor.
- [static func clipByGlobalNorm(threshold: Float, inputs: [BNNSNDArrayDescriptor], outputs: [BNNSNDArrayDescriptor], globalNorm: Float) throws](./clipbyglobalnorm%28threshold,inputs,outputs,globalnorm%29.md)
  Clips the input tensors to a global Euclidean norm and writes the result to the output tensors.
- [func BNNSClipByValue(UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, Float, Float) -> Int32](../bnnsclipbyvalue%28_,_,_,_%29.md)
  Clips a tensor’s values to the specified minimum and maximum values.
- [func BNNSClipByNorm(UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, Float, UInt32) -> Int32](../bnnsclipbynorm%28_,_,_,_%29.md)
  Clips a tensor’s values to a maximum Euclidean norm.
- [func BNNSClipByGlobalNorm(UnsafeMutablePointer<UnsafeMutablePointer<BNNSNDArrayDescriptor>>, UnsafeMutablePointer<UnsafePointer<BNNSNDArrayDescriptor>>, Int, Float, Float) -> Int32](../bnnsclipbyglobalnorm%28_,_,_,_,_%29.md)
  Clips a tensor’s values to a maximum global Euclidean norm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/tilebackward(outputgradient:generatinginputgradient:filterparameters:))*