# BNNSClipByGlobalNorm(_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Clips a tensor’s values to a maximum global Euclidean norm.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
func BNNSClipByGlobalNorm(_ dest: UnsafeMutablePointer<UnsafeMutablePointer<BNNSNDArrayDescriptor>>, _ src: UnsafeMutablePointer<UnsafePointer<BNNSNDArrayDescriptor>>, _ count: Int, _ max_norm: Float, _ use_norm: Float) -> Int32
```

#### Discussion

Use this function to clip the values in an array of input tensors to a maximum Euclidean norm. If you know the global norm of the input tensors, pass this value as the `use_norm`. Otherwise, pass `0` to specify that the function calculates the norm.

The Euclidean norm is the square root of the sum of squares of the two tensors. The following code clips the Euclidean norm of two input tensors to half of the global Euclidean norm:

```swift
static func clipToGlobalNorm() {
    
    let inputOneData = UnsafeMutableBufferPointer<Float>.allocate(capacity: 4)
    _ = inputOneData.initialize(from: [1, 2, 3, 4])
    let inputOneDescriptor = BNNSNDArrayDescriptor(flags: BNNSNDArrayFlags(0),
                                                   layout: BNNSDataLayoutVector,
                                                   size: (4, 0, 0, 0, 0, 0, 0, 0),
                                                   stride: (0, 0, 0, 0, 0, 0, 0, 0),
                                                   data: inputOneData.baseAddress!,
                                                   data_type: BNNSDataType.float,
                                                   table_data: nil,
                                                   table_data_type: BNNSDataType.float,
                                                   data_scale: 1, data_bias: 0)
    
    let inputTwoData = UnsafeMutableBufferPointer<Float>.allocate(capacity: 4)
    _ = inputTwoData.initialize(from: [5, 6, 7, 8])
    let inputTwoDescriptor = BNNSNDArrayDescriptor(flags: BNNSNDArrayFlags(0),
                                                   layout: BNNSDataLayoutVector,
                                                   size: (4, 0, 0, 0, 0, 0, 0, 0),
                                                   stride: (0, 0, 0, 0, 0, 0, 0, 0),
                                                   data: inputTwoData.baseAddress!,
                                                   data_type: BNNSDataType.float,
                                                   table_data: nil,
                                                   table_data_type: BNNSDataType.float,
                                                   data_scale: 1, data_bias: 0)
    
    let outputOneData = UnsafeMutableBufferPointer<Float>.allocate(capacity: 4)
    let outputOneDescriptor = BNNSNDArrayDescriptor(flags: BNNSNDArrayFlags(0),
                                                    layout: BNNSDataLayoutVector,
                                                    size: (4, 0, 0, 0, 0, 0, 0, 0),
                                                    stride: (0, 0, 0, 0, 0, 0, 0, 0),
                                                    data: outputOneData.baseAddress!,
                                                    data_type: BNNSDataType.float,
                                                    table_data: nil,
                                                    table_data_type: BNNSDataType.float,
                                                    data_scale: 1, data_bias: 0)
    
    let outputTwoData = UnsafeMutableBufferPointer<Float>.allocate(capacity: 4)
    let outputTwoDescriptor = BNNSNDArrayDescriptor(flags: BNNSNDArrayFlags(0),
                                                    layout: BNNSDataLayoutVector,
                                                    size: (4, 0, 0, 0, 0, 0, 0, 0),
                                                    stride: (0, 0, 0, 0, 0, 0, 0, 0),
                                                    data: outputTwoData.baseAddress!,
                                                    data_type: BNNSDataType.float,
                                                    table_data: nil,
                                                    table_data_type: BNNSDataType.float,
                                                    data_scale: 1, data_bias: 0)
    
    let inputs = [inputOneDescriptor, inputTwoDescriptor]
    var inputsPointers: [UnsafePointer<BNNSNDArrayDescriptor>] = inputs.map { input in
        var descriptor = input
        
        let inputPtr = UnsafeMutablePointer<BNNSNDArrayDescriptor>.allocate(capacity: 1)
        inputPtr.initialize(from: &descriptor, count: 1)
        
        return UnsafePointer(inputPtr)
    }
    
    let outputs = [outputOneDescriptor, outputTwoDescriptor]
    var outputsPointers: [UnsafeMutablePointer<BNNSNDArrayDescriptor>] = outputs.map { output in
        var descriptor = output
        
        let outputPtr = UnsafeMutablePointer<BNNSNDArrayDescriptor>.allocate(capacity: 1)
        outputPtr.initialize(from: &descriptor, count: 1)
        
        return outputPtr
    }
    
    BNNSClipByGlobalNorm(&outputsPointers,
                         &inputsPointers,
                         2,
                         0.5 * 14.2828568570857,
                         0)
    
    // Prints: `[0.5, 1.0, 1.5, 2.0]`
    print(Array(outputOneData))
    
    // Prints: `[2.5, 3.0, 3.5, 4.0]`
    print(Array(outputTwoData))
    
    inputOneData.deallocate()
    inputTwoData.deallocate()
    outputOneData.deallocate()
    outputTwoData.deallocate()
}
```

On return, `outputOne` contains the values `[0.5, 1.0, 1.5, 2.0]`, and `outputTwo` contains the values `[2.5, 3.0, 3.5, 4.0]`.

## Parameters

- `dest`: An array of output descriptors.
- `src`: An array of input descriptors.
- `count`: The number of input and output descriptors.
- `max_norm`: The maximum global Euclidean norm.
- `use_norm`: An optional value for a known global Euclidean norm. Set to   to specify that the function computes the norm from the input descriptors.

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
- [static func clipByGlobalNorm(threshold: Float, inputs: [BNNSNDArrayDescriptor], outputs: [BNNSNDArrayDescriptor], globalNorm: Float) throws](bnns/clipbyglobalnorm(threshold:inputs:outputs:globalnorm:).md)
  Clips the input tensors to a global Euclidean norm and writes the result to the output tensors.
- [func BNNSClipByValue(UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, Float, Float) -> Int32](bnnsclipbyvalue(_:_:_:_:).md)
  Clips a tensor’s values to the specified minimum and maximum values.
- [func BNNSClipByNorm(UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, Float, UInt32) -> Int32](bnnsclipbynorm(_:_:_:_:).md)
  Clips a tensor’s values to a maximum Euclidean norm.
- [static func copyBandPart(BNNSNDArrayDescriptor, to: BNNSNDArrayDescriptor, lowerBandCount: Int?, upperBandCount: Int?, filterParameters: BNNSFilterParameters?) throws](bnns/copybandpart(_:to:lowerbandcount:upperbandcount:filterparameters:).md)
  Copies the specified subdiagonals and superdiagonals of a matrix, and sets other elements to zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsclipbyglobalnorm(_:_:_:_:_:))*