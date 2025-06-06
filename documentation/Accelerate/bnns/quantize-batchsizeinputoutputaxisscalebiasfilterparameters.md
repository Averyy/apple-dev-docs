# quantize(batchSize:input:output:axis:scale:bias:filterParameters:)

**Framework**: Accelerate  
**Kind**: method

Quantizes the input tensor and writes the result to the output tensor.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- visionOS ?+
- watchOS 8.0+
- Unknown ?+ - Deprecated
- tvOS 15.0+

## Declaration

```swift
static func quantize(batchSize: Int, input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, axis: Int? = nil, scale: BNNSNDArrayDescriptor?, bias: BNNSNDArrayDescriptor?, filterParameters: BNNSFilterParameters? = nil) throws
```

#### Discussion

The following code quantizes a single-precision matrix to a 16-bit integer matrix. The code applies the scale along the zeroth axis and, therefore, the scale tensor contains four elements.

```swift
static func quantize() {
    
    let inputValues = [1, 2, 3, 4,
                       5, 6, 7, 8] as [Float]
    
    let input = BNNSNDArrayDescriptor.allocate(
        initializingFrom: inputValues,
        shape: .matrixRowMajor(4, 2))
    
    let output = BNNSNDArrayDescriptor.allocateUninitialized(
        scalarType: Int16.self,
        shape: input.shape)
    
    let scale = BNNSNDArrayDescriptor.allocate(
        initializingFrom: [1, 10, 100, 1000] as [Float],
        shape: .vector(4))
    
    try? BNNS.quantize(batchSize: 1,
                       input: input,
                       output: output,
                       axis: 0,
                       scale: scale,
                       bias: nil)

    // Prints:
    //  [1, 20, 300, 4000,
    //   5, 60, 700, 8000]
    print(output.makeArray(of: Int16.self)!)
    
    input.deallocate()
    output.deallocate()
    scale.deallocate()
}
```

## Parameters

- `batchSize`: The number of input-output pairs to process.
- `input`: The descriptor of the input.
- `output`: The descriptor of the output.
- `axis`: The index of the axis to which the function applies scale and bias. Set to   to dequantize the entire tensor using scale and bias.
- `scale`: The scale, set to   for a scale of  .
- `bias`: The bias, set to   for a bias of  .
- `filterParameters`: Runtime filter parameters.

## See Also

- [var BNNSQuantizerFunctionQuantize: BNNSQuantizerFunction](bnnsquantizerfunctionquantize.md)
  A constant that specifes conversion to a lower precision.
- [static func dequantize(batchSize: Int, input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, axis: Int?, scale: BNNSNDArrayDescriptor?, bias: BNNSNDArrayDescriptor?, filterParameters: BNNSFilterParameters?) throws](bnns/dequantize(batchsize:input:output:axis:scale:bias:filterparameters:).md)
  Dequantizes the input tensor and writes the result to the output tensor.
- [struct BNNSQuantizerFunction](bnnsquantizerfunction.md)
  Constants that describe quantization functions.
- [struct BNNSLayerParametersQuantization](bnnslayerparametersquantization.md)
  A structure that contains the parameters of a quantization layer.
- [func BNNSDirectApplyQuantizer(UnsafePointer<BNNSLayerParametersQuantization>, UnsafePointer<BNNSFilterParameters>?, Int, Int, Int) -> Int32](bnnsdirectapplyquantizer(_:_:_:_:_:).md)
  Applies a quantization layer directly to two input matrices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/quantize(batchsize:input:output:axis:scale:bias:filterparameters:))*