# BNNSArithmeticTernary

**Framework**: Accelerate  
**Kind**: struct  
**Role**: Structure

A structure that contains the inputs and output of an arithmetic operation with three inputs.

**Availability**:
- iOS 14.0+ - Deprecated in 18.0
- iPadOS 14.0+ - Deprecated in 18.0
- Mac Catalyst 14.0+ - Deprecated in 18.0
- macOS 11.0+ - Deprecated in 15.0
- tvOS 14.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 7.0+ - Deprecated in 11.0

> **Deprecated**: Use BNNSGraph* APIs

## Declaration

```swift
struct BNNSArithmeticTernary
```

```c
typedef struct { ... } BNNSArithmeticTernary;
```

#### Overview

Use a [`BNNSArithmeticTernary`](./bnnsarithmeticternary.md) structure to pass the descriptions and types of the inputs and output of a binary arithmetic operation to [`BNNSLayerParametersArithmetic`](./bnnslayerparametersarithmetic.md).

The following code shows how to calculate the element-wise multiply-add of two vectors:

```swift
static func ternaryArithmetic() {
    
    let aData = UnsafeMutableBufferPointer<Float>.allocate(capacity: 1)
    _ = aData.initialize(from: [10])
    let aDescriptor = BNNSNDArrayDescriptor(flags: BNNSNDArrayFlags(0),
                                            layout: BNNSDataLayoutVector,
                                            size: (1, 0, 0, 0, 0, 0, 0, 0),
                                            stride: (0, 0, 0, 0, 0, 0, 0, 0),
                                            data: aData.baseAddress!,
                                            data_type: BNNSDataType.float,
                                            table_data: nil,
                                            table_data_type: BNNSDataType.float,
                                            data_scale: 1, data_bias: 0)
    
    let bData = UnsafeMutableBufferPointer<Float>.allocate(capacity: 1)
    _ = bData.initialize(from: [20])
    let bDescriptor = BNNSNDArrayDescriptor(flags: BNNSNDArrayFlags(0),
                                            layout: BNNSDataLayoutVector,
                                            size: (1, 0, 0, 0, 0, 0, 0, 0),
                                            stride: (0, 0, 0, 0, 0, 0, 0, 0),
                                            data: bData.baseAddress!,
                                            data_type: BNNSDataType.float,
                                            table_data: nil,
                                            table_data_type: BNNSDataType.float,
                                            data_scale: 1, data_bias: 0)
    
    let cData = UnsafeMutableBufferPointer<Float>.allocate(capacity: 1)
    _ = cData.initialize(from: [100])
    let cDescriptor = BNNSNDArrayDescriptor(flags: BNNSNDArrayFlags(0),
                                            layout: BNNSDataLayoutVector,
                                            size: (1, 0, 0, 0, 0, 0, 0, 0),
                                            stride: (0, 0, 0, 0, 0, 0, 0, 0),
                                            data: cData.baseAddress!,
                                            data_type: BNNSDataType.float,
                                            table_data: nil,
                                            table_data_type: BNNSDataType.float,
                                            data_scale: 1, data_bias: 0)
    
    let outputData = UnsafeMutableBufferPointer<Float>.allocate(capacity: 1)
    let outputDescriptor = BNNSNDArrayDescriptor(flags: BNNSNDArrayFlags(0),
                                                 layout: BNNSDataLayoutVector,
                                                 size: (1, 0, 0, 0, 0, 0, 0, 0),
                                                 stride: (0, 0, 0, 0, 0, 0, 0, 0),
                                                 data: outputData.baseAddress!,
                                                 data_type: BNNSDataType.float,
                                                 table_data: nil,
                                                 table_data_type: BNNSDataType.float,
                                                 data_scale: 1, data_bias: 0)
    
    let fields = BNNSArithmeticTernary(in1: aDescriptor, in1_type: BNNSSample,
                                       in2: bDescriptor, in2_type: BNNSSample,
                                       in3: cDescriptor, in3_type: BNNSSample,
                                       out: outputDescriptor, out_type: BNNSSample)
    
    let arithmeticLayer: BNNSFilter? = withUnsafePointer(to: fields) { fieldsPtr in
        
        var layerParameters = BNNSLayerParametersArithmetic(
            arithmetic_function: BNNSArithmeticMultiplyAdd,
            arithmetic_function_fields: UnsafeMutableRawPointer(mutating: fieldsPtr),
            activation: .identity)
        
        return BNNSFilterCreateLayerArithmetic(&layerParameters, nil)
    }
    
    var rawInputPointer = [ UnsafeRawPointer(aDescriptor.data!),
                            UnsafeRawPointer(bDescriptor.data!),
                            UnsafeRawPointer(cDescriptor.data!)]
    
    BNNSArithmeticFilterApplyBatch(arithmeticLayer,
                                   1,
                                   3,
                                   &rawInputPointer,
                                   [1, 1, 1],
                                   outputDescriptor.data!,
                                   1)
    
    // Prints "[300.0]" (10 * 20 + 100).
    print(Array(outputData))
    
    aData.deallocate()
    bData.deallocate()
    cData.deallocate()
    outputData.deallocate()
}
```

## Topics

### Creating an Arithmetic Structure
- [init(in1: BNNSNDArrayDescriptor, in1_type: BNNSDescriptorType, in2: BNNSNDArrayDescriptor, in2_type: BNNSDescriptorType, in3: BNNSNDArrayDescriptor, in3_type: BNNSDescriptorType, out: BNNSNDArrayDescriptor, out_type: BNNSDescriptorType)](./bnnsarithmeticternary/init%28in1,in1_type,in2,in2_type,in3,in3_type,out,out_type%29.md)
  Returns a new arithmetic structure that takes three inputs from the specified parameters.
- [init()](./bnnsarithmeticternary/init%28%29.md)
  Returns a new arithmetic structure that takes three inputs.
### Inspecting the Properties of an Arithmetic Structure
- [var in1: BNNSNDArrayDescriptor](./bnnsarithmeticternary/in1.md)
  The descriptor of the first input.
- [var in1_type: BNNSDescriptorType](./bnnsarithmeticternary/in1_type.md)
  The descriptor type of the first input.
- [var in2: BNNSNDArrayDescriptor](./bnnsarithmeticternary/in2.md)
  The descriptor of the second input.
- [var in2_type: BNNSDescriptorType](./bnnsarithmeticternary/in2_type.md)
  The descriptor type of the second input.
- [var in3: BNNSNDArrayDescriptor](./bnnsarithmeticternary/in3.md)
  The descriptor of the third input.
- [var in3_type: BNNSDescriptorType](./bnnsarithmeticternary/in3_type.md)
  The descriptor type of the third input.
- [var out: BNNSNDArrayDescriptor](./bnnsarithmeticternary/out.md)
  The descriptor of the output.
- [var out_type: BNNSDescriptorType](./bnnsarithmeticternary/out_type.md)
  The descriptor type of the output.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)

## See Also

### Arithmetic layers
- [class UnaryArithmeticLayer](./bnns/unaryarithmeticlayer.md)
  A layer object that wraps a unary arithmetic filter and manages its deinitialization.
- [class BinaryArithmeticLayer](./bnns/binaryarithmeticlayer.md)
  A layer object that wraps a binary arithmetic filter and manages its deinitialization.
- [class TernaryArithmeticLayer](./bnns/ternaryarithmeticlayer.md)
  A layer object that wraps a ternary arithmetic filter and manages its deinitialization.
- [struct BNNSDescriptorType](./bnnsdescriptortype.md)
  Constants that describe the input and output types of an arithmetic operation.
- [struct BNNSArithmeticUnary](./bnnsarithmeticunary.md)
  A structure that contains the input and output of an arithmetic operation with a single input.
- [struct BNNSArithmeticBinary](./bnnsarithmeticbinary.md)
  A structure that contains the inputs and output of an arithmetic operation with two inputs.
- [struct BNNSArithmeticFunction](./bnnsarithmeticfunction.md)
  Constants that define arithmetic operations.
- [struct BNNSLayerParametersArithmetic](./bnnslayerparametersarithmetic.md)
  A structure that contains the parameters of an arithmetic layer.
- [func BNNSFilterCreateLayerArithmetic(UnsafePointer<BNNSLayerParametersArithmetic>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](./bnnsfiltercreatelayerarithmetic%28_,_%29.md)
  Returns a new arithmetic layer.
- [func BNNSArithmeticFilterApplyBatch(BNNSFilter?, Int, Int, UnsafeMutablePointer<UnsafeRawPointer>, UnsafePointer<Int>, UnsafeMutableRawPointer, Int) -> Int32](./bnnsarithmeticfilterapplybatch%28_,_,_,_,_,_,_%29.md)
  Applies an arithmetic filter to a set of input objects, writing the result to a set of output objects.
- [func BNNSArithmeticFilterApplyBackwardBatch(BNNSFilter?, Int, Int, UnsafeMutablePointer<UnsafeRawPointer?>?, UnsafePointer<Int>?, UnsafeMutablePointer<UnsafeMutablePointer<BNNSNDArrayDescriptor>>, UnsafePointer<Int>, UnsafeRawPointer?, Int, UnsafeMutablePointer<BNNSNDArrayDescriptor>, Int) -> Int32](./bnnsarithmeticfilterapplybackwardbatch%28_,_,_,_,_,_,_,_,_,_,_%29.md)
  Applies an arithmetic filter backward to generate input gradients.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsarithmeticternary)*