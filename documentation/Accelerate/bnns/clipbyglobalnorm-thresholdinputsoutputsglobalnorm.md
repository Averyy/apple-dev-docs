# clipByGlobalNorm(threshold:inputs:outputs:globalNorm:)

**Framework**: Accelerate  
**Kind**: method

Clips the input tensors to a global Euclidean norm and writes the result to the output tensors.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS ?+
- watchOS 8.0+
- Unknown ?+ - Deprecated
- Mac Catalyst ?+

## Declaration

```swift
static func clipByGlobalNorm(threshold: Float, inputs: [BNNSNDArrayDescriptor], outputs: [BNNSNDArrayDescriptor], globalNorm: Float = 0) throws
```

#### Discussion

Use this function to clip the values in an array of input tensors to a maximum global Euclidean norm. If you know the global norm of the input tensors, pass this value as the `globalNorm`. Otherwise, pass `0` to specify that the function calculates the norm.

The Euclidean norm is the square root of the sum of squares of the two tensors. The following code clips the Euclidean norm of two input tensors to half of the global Euclidean norm:

```swift
static func clipToGlobalNorm() {
    let inputOne = BNNSNDArrayDescriptor.allocate(
        initializingFrom: [1, 2, 3, 4] as [Float],
        shape: .vector(4))
    let inputTwo = BNNSNDArrayDescriptor.allocate(
        initializingFrom: [5, 6, 7, 8] as [Float],
        shape: .vector(4))
    
    let outputOne = BNNSNDArrayDescriptor.allocateUninitialized(
        scalarType: Float.self,
        shape: .vector(4))
    let outputTwo = BNNSNDArrayDescriptor.allocateUninitialized(
        scalarType: Float.self,
        shape: .vector(4))
    
    try? BNNS.clipByGlobalNorm(threshold: 0.5 * 14.2828568570857,
                               inputs: [inputOne, inputTwo],
                               outputs: [outputOne, outputTwo])
    
    // Prints: `[0.5, 1.0, 1.5, 2.0]`
    print(outputOne.makeArray(of: Float.self)!)
    
    // Prints: `[2.5, 3.0, 3.5, 4.0]`
    print(outputTwo.makeArray(of: Float.self)!)

    inputOne.deallocate()
    inputTwo.deallocate()
    outputOne.deallocate()
    outputTwo.deallocate()
}
```

## Parameters

- `threshold`: The maximum Euclidean norm to clip the gradient to.
- `inputs`: An array of input descriptors.
- `outputs`: An array of output descriptors.
- `globalNorm`: The global norm to use. Set to   to specify that the function computes the norm from the input descriptors.

## See Also

- [static func copy(BNNSNDArrayDescriptor, to: BNNSNDArrayDescriptor, filterParameters: BNNSFilterParameters?) throws](bnns/copy(_:to:filterparameters:).md)
  Copies the contents of an n-dimensional array descriptor to another descriptor of the same shape.
- [static func transpose(input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, firstTransposeAxis: Int, secondTransposeAxis: Int, filterParameters: BNNSFilterParameters?) throws](bnns/transpose(input:output:firsttransposeaxis:secondtransposeaxis:filterparameters:).md)
  Transposes a tensor by swapping two of its dimensions.
- [func BNNSCopy(UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSFilterParameters>?) -> Int32](bnnscopy(_:_:_:).md)
  Copies the contents of an n-dimensional array descriptor to another of the same shape.
- [func BNNSTranspose(UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, Int, Int, UnsafePointer<BNNSFilterParameters>?) -> Int32](bnnstranspose(_:_:_:_:_:).md)
  Transposes a tensor by swapping two of its dimensions.
- [func BNNSGetPointer(BNNSFilter?, BNNSPointerSpecifier) -> BNNSNDArrayDescriptor](bnnsgetpointer(_:_:).md)
  Returns an n-dimensional array descriptor that contains a reference to a filter-data member.
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
- [func BNNSClipByValue(UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, Float, Float) -> Int32](bnnsclipbyvalue(_:_:_:_:).md)
  Clips a tensor’s values to the specified minimum and maximum values.
- [func BNNSClipByNorm(UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, Float, UInt32) -> Int32](bnnsclipbynorm(_:_:_:_:).md)
  Clips a tensor’s values to a maximum Euclidean norm.
- [func BNNSClipByGlobalNorm(UnsafeMutablePointer<UnsafeMutablePointer<BNNSNDArrayDescriptor>>, UnsafeMutablePointer<UnsafePointer<BNNSNDArrayDescriptor>>, Int, Float, Float) -> Int32](bnnsclipbyglobalnorm(_:_:_:_:_:).md)
  Clips a tensor’s values to a maximum global Euclidean norm.
- [static func copyBandPart(BNNSNDArrayDescriptor, to: BNNSNDArrayDescriptor, lowerBandCount: Int?, upperBandCount: Int?, filterParameters: BNNSFilterParameters?) throws](bnns/copybandpart(_:to:lowerbandcount:upperbandcount:filterparameters:).md)
  Copies the specified subdiagonals and superdiagonals of a matrix, and sets other elements to zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/clipbyglobalnorm(threshold:inputs:outputs:globalnorm:))*