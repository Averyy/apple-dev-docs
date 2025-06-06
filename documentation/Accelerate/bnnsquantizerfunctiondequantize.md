# BNNSQuantizerFunctionDequantize

**Framework**: Accelerate  
**Kind**: var

A constant that specifes conversion to a higher precision.

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
var BNNSQuantizerFunctionDequantize: BNNSQuantizerFunction { get }
```

#### Discussion

The following code dequantizes a 16-bit integer matrix to a single-precision matrix. The code applies the scale along the zeroth axis and, therefore, the scale tensor contains four elements.

```swift
static func dequantize() {
    
    let inputData = UnsafeMutableBufferPointer<Int16>.allocate(capacity: 8)
    _ = inputData.initialize(from: [1000, 2000, 3000, 4000,
                                    5000, 6000, 7000, 8000])
    let inputDescriptor = BNNSNDArrayDescriptor(flags: BNNSNDArrayFlags(0),
                                                layout: BNNSDataLayoutRowMajorMatrix,
                                                size: (4, 2, 0, 0, 0, 0, 0, 0),
                                                stride: (0, 0, 0, 0, 0, 0, 0, 0),
                                                data: inputData.baseAddress!,
                                                data_type: BNNSDataType.int16,
                                                table_data: nil,
                                                table_data_type: BNNSDataType.int16,
                                                data_scale: 1, data_bias: 0)
    
    let outputData = UnsafeMutableBufferPointer<Float>.allocate(capacity: 8)
    let outputDescriptor = BNNSNDArrayDescriptor(flags: BNNSNDArrayFlags(0),
                                                 layout: BNNSDataLayoutRowMajorMatrix,
                                                 size: (4, 2, 0, 0, 0, 0, 0, 0),
                                                 stride: (0, 0, 0, 0, 0, 0, 0, 0),
                                                 data: outputData.baseAddress!,
                                                 data_type: BNNSDataType.float,
                                                 table_data: nil,
                                                 table_data_type: BNNSDataType.float,
                                                 data_scale: 1, data_bias: 0)
    
    let scaleData = UnsafeMutableBufferPointer<Int16>.allocate(capacity: 4)
    _ = scaleData.initialize(from: [1, 10, 100, 1000])
    let scaleDescriptor = BNNSNDArrayDescriptor(flags: BNNSNDArrayFlags(0),
                                                layout: BNNSDataLayoutVector,
                                                size: (4, 0, 0, 0, 0, 0, 0, 0),
                                                stride: (0, 0, 0, 0, 0, 0, 0, 0),
                                                data: scaleData.baseAddress!,
                                                data_type: BNNSDataType.int16,
                                                table_data: nil,
                                                table_data_type: BNNSDataType.int16,
                                                data_scale: 1, data_bias: 0)
    
    var layerParams = BNNSLayerParametersQuantization(axis_mask: 1,
                                                      function: BNNSQuantizerFunctionDequantize,
                                                      i_desc: inputDescriptor,
                                                      o_desc: outputDescriptor,
                                                      scale: scaleDescriptor,
                                                      bias: BNNSNDArrayDescriptor())
    
    BNNSDirectApplyQuantizer(&layerParams,
                              nil,
                              1,
                              8,
                              8)
    
    // Prints:
    //  [1000.0, 200.0, 30.0, 4.0,
    //   5000.0, 600.0, 70.0, 8.0]
    print(Array(outputData))
    
    inputData.deallocate()
    outputData.deallocate()
    scaleData.deallocate()
}
```

## See Also

- [init(UInt32)](bnnsquantizerfunction/init(_:).md)
  Creates a new instance with the specified raw value.
- [init(rawValue: UInt32)](bnnsquantizerfunction/init(rawvalue:).md)
  Creates a new instance with the specified raw value.
- [var rawValue: UInt32](bnnsquantizerfunction/rawvalue.md)
  The corresponding value of the raw type.
- [var BNNSQuantizerFunctionQuantize: BNNSQuantizerFunction](bnnsquantizerfunctionquantize.md)
  A constant that specifes conversion to a lower precision.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsquantizerfunctiondequantize)*