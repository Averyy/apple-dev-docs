# BNNSArithmeticBinary

**Framework**: Accelerate  
**Kind**: struct

A structure that contains the inputs and output of an arithmetic operation with two inputs.

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
struct BNNSArithmeticBinary
```

#### Overview

Use a [`BNNSArithmeticUnary`](bnnsarithmeticunary.md) structure to pass the descriptions and types of the inputs and output of a binary arithmetic operation to [`BNNSLayerParametersArithmetic`](bnnslayerparametersarithmetic.md).

The following code shows how to calculate the element-wise sums of two vectors:

```swift
let inputOne: [Float] = [ 1,  2,  3,  4,  5,  6,  7,  8,  9,  10]
let inputTwo: [Float] = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
let count = inputOne.count
var outputs = [Float](repeating: 0,
                      count: count)

let descriptor = BNNSNDArrayDescriptor(flags: BNNSNDArrayFlags(0),
                                       layout: BNNSDataLayoutVector,
                                       size: (count, 0, 0, 0, 0, 0, 0, 0),
                                       stride: (0, 0, 0, 0, 0, 0, 0, 0),
                                       data: nil,
                                       data_type: .float,
                                       table_data: nil,
                                       table_data_type: .float,
                                       data_scale: 1,
                                       data_bias: 0)

var fields = BNNSArithmeticBinary(in1: descriptor, in1_type: BNNSSample,
                                  in2: descriptor, in2_type: BNNSConstant,
                                  out: descriptor, out_type: BNNSSample)

let function = BNNSArithmeticAdd

withUnsafeMutableBytes(of: &fields) { fieldsPtr in
    
    var layerParameters = BNNSLayerParametersArithmetic(arithmetic_function: function,
                                                        arithmetic_function_fields: fieldsPtr.baseAddress!,
                                                        activation: .identity)
    
    guard let arithmeticLayer = BNNSFilterCreateLayerArithmetic(&layerParameters, nil) else {
        print("Binary BNNSFilterCreateLayerArithmetic returned nil")
        return
    }
    defer {
        BNNSFilterDestroy(arithmeticLayer)
    }
    
    inputOne.withUnsafeBytes { in1Ptr in
        inputTwo.withUnsafeBytes { in2Ptr in
            
            var input = [in1Ptr.baseAddress!, in2Ptr.baseAddress!]
            
            let error = BNNSArithmeticFilterApplyBatch(arithmeticLayer,
                                                       1,
                                                       2,
                                                       &input,
                                                       [inputOne.count, inputTwo.count],
                                                       &outputs,
                                                       outputs.count)
            
            print("BNNSArithmeticFilterApplyBatch: error", error)
        }
    }
}

// Prints "[11.0, 22.0, 33.0, 44.0, 55.0, 66.0, 77.0, 88.0, 99.0, 110.0]"
print("Binary Arithmetic: outputs", outputs)
```

## Topics

### Creating an Arithmetic Structure
- [init(in1: BNNSNDArrayDescriptor, in1_type: BNNSDescriptorType, in2: BNNSNDArrayDescriptor, in2_type: BNNSDescriptorType, out: BNNSNDArrayDescriptor, out_type: BNNSDescriptorType)](bnnsarithmeticbinary/init(in1:in1_type:in2:in2_type:out:out_type:).md)
  Returns a new arithmetic structure that takes two inputs from the specified parameters.
- [init()](bnnsarithmeticbinary/init.md)
  Returns a new arithmetic structure that takes two inputs.
### Inspecting the Properties of an Arithmetic Structure
- [var in1: BNNSNDArrayDescriptor](bnnsarithmeticbinary/in1.md)
  The descriptor of the first input.
- [var in1_type: BNNSDescriptorType](bnnsarithmeticbinary/in1_type.md)
  The descriptor type of the first input.
- [var in2: BNNSNDArrayDescriptor](bnnsarithmeticbinary/in2.md)
  The descriptor of the second input.
- [var in2_type: BNNSDescriptorType](bnnsarithmeticbinary/in2_type.md)
  The descriptor type of the second input.
- [var out: BNNSNDArrayDescriptor](bnnsarithmeticbinary/out.md)
  The descriptor of the output.
- [var out_type: BNNSDescriptorType](bnnsarithmeticbinary/out_type.md)
  The descriptor type of the output.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [class UnaryArithmeticLayer](bnns/unaryarithmeticlayer.md)
  A layer object that wraps a unary arithmetic filter and manages its deinitialization.
- [class BinaryArithmeticLayer](bnns/binaryarithmeticlayer.md)
  A layer object that wraps a binary arithmetic filter and manages its deinitialization.
- [class TernaryArithmeticLayer](bnns/ternaryarithmeticlayer.md)
  A layer object that wraps a ternary arithmetic filter and manages its deinitialization.
- [struct BNNSDescriptorType](bnnsdescriptortype.md)
  Constants that describe the input and output types of an arithmetic operation.
- [struct BNNSArithmeticUnary](bnnsarithmeticunary.md)
  A structure that contains the input and output of an arithmetic operation with a single input.
- [struct BNNSArithmeticTernary](bnnsarithmeticternary.md)
  A structure that contains the inputs and output of an arithmetic operation with three inputs.
- [struct BNNSArithmeticFunction](bnnsarithmeticfunction.md)
  Constants that define arithmetic operations.
- [struct BNNSLayerParametersArithmetic](bnnslayerparametersarithmetic.md)
  A structure that contains the parameters of an arithmetic layer.
- [func BNNSFilterCreateLayerArithmetic(UnsafePointer<BNNSLayerParametersArithmetic>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](bnnsfiltercreatelayerarithmetic(_:_:).md)
  Returns a new arithmetic layer.
- [func BNNSArithmeticFilterApplyBatch(BNNSFilter?, Int, Int, UnsafeMutablePointer<UnsafeRawPointer>, UnsafePointer<Int>, UnsafeMutableRawPointer, Int) -> Int32](bnnsarithmeticfilterapplybatch(_:_:_:_:_:_:_:).md)
  Applies an arithmetic filter to a set of input objects, writing the result to a set of output objects.
- [func BNNSArithmeticFilterApplyBackwardBatch(BNNSFilter?, Int, Int, UnsafeMutablePointer<UnsafeRawPointer?>?, UnsafePointer<Int>?, UnsafeMutablePointer<UnsafeMutablePointer<BNNSNDArrayDescriptor>>, UnsafePointer<Int>, UnsafeRawPointer?, Int, UnsafeMutablePointer<BNNSNDArrayDescriptor>, Int) -> Int32](bnnsarithmeticfilterapplybackwardbatch(_:_:_:_:_:_:_:_:_:_:_:).md)
  Applies an arithmetic filter backward to generate input gradients.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsarithmeticbinary)*