# clip(to:input:output:)

**Framework**: Accelerate  
**Kind**: method

Clips the input tensor to a closed range and writes the result to the output tensor.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS ?+
- watchOS 8.0+

## Declaration

```swift
static func clip(to bounds: ClosedRange<Float>, input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor) throws
```

#### Discussion

Use this function to clip the values in an input tensor to a range. The function sets values below the minimum to the minimum and values above the maximum to the maximum.

The following code clips the values of the input tensor to the range `3...6`:

```swift
static func clipToBounds() {
    let input = BNNSNDArrayDescriptor.allocate(
        initializingFrom: [1, 2, 3, 4, 5, 6, 7, 8] as [Float],
        shape: .vector(8))
    
    let output = BNNSNDArrayDescriptor.allocateUninitialized(
        scalarType: Float.self,
        shape: .vector(8))
    
    try? BNNS.clip(to: 3...6,
                   input: input,
                   output: output)
    
    // Prints: `[3.0, 3.0, 3.0, 4.0, 5.0, 6.0, 6.0, 6.0]`
    print(output.makeArray(of: Float.self)!)

    input.deallocate()
    output.deallocate()
}
```

## Parameters

- `bounds`: The clipping values.
- `input`: The descriptor of the input.
- `output`: The descriptor of the output.

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

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/clip(to:input:output:))*