# BNNSArithmeticUnary

**Framework**: Accelerate  
**Kind**: struct

A structure that contains the input and output of an arithmetic operation with a single input.

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
struct BNNSArithmeticUnary
```

#### Overview

Use a [`BNNSArithmeticUnary`](bnnsarithmeticunary.md) structure to pass the descriptions and types of the input and output of a unary arithmetic operation to [`BNNSLayerParametersArithmetic`](bnnslayerparametersarithmetic.md).

The following code shows how to calculate the element-wise square roots of a vector:

```swift
let input: [Float] = [4, 16, 9, 25, 100]
let count = input.count
var output = [Float](repeating: .nan,
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

var fields = BNNSArithmeticUnary(in: descriptor,
                                 in_type: BNNSSample,
                                 out: descriptor,
                                 out_type: BNNSSample)

withUnsafeMutablePointer(to: &fields) { fieldsPtr in
    
    var layerParameters = BNNSLayerParametersArithmetic(arithmetic_function: BNNSArithmeticSquareRoot,
                                                        arithmetic_function_fields: fieldsPtr,
                                                        activation: .identity)
    
    guard let arithmeticLayer = BNNSFilterCreateLayerArithmetic(&layerParameters, nil) else {
        print("Unary BNNSFilterCreateLayerArithmetic returns nil")
        return
    }
    defer {
        BNNSFilterDestroy(arithmeticLayer)
    }
    
    input.withUnsafeBytes { inPtr in
        var rawPtr = inPtr.baseAddress!
        
        BNNSArithmeticFilterApplyBatch(arithmeticLayer, 1, 1,
                                       &rawPtr,
                                       [count],
                                       &output,
                                       count)
    }
}

// Prints "[2.0, 4.0, 3.0, 5.0, 10.0]"
print("Unary Arithmetic: outputs", output)
```

## Topics

### Creating an Arithmetic Structure
- [init(in: BNNSNDArrayDescriptor, in_type: BNNSDescriptorType, out: BNNSNDArrayDescriptor, out_type: BNNSDescriptorType)](bnnsarithmeticunary/init(in:in_type:out:out_type:).md)
  Returns a new arithmetic structure that takes a single input from the specified parameters.
- [init()](bnnsarithmeticunary/init.md)
  Returns a new arithmetic structure that takes a single input.
### Inspecting the Properties of an Arithmetic Structure
- [var `in`: BNNSNDArrayDescriptor](bnnsarithmeticunary/in.md)
  The descriptor of the input.
- [var in_type: BNNSDescriptorType](bnnsarithmeticunary/in_type.md)
  The descriptor type of the input.
- [var out: BNNSNDArrayDescriptor](bnnsarithmeticunary/out.md)
  The descriptor of the output.
- [var out_type: BNNSDescriptorType](bnnsarithmeticunary/out_type.md)
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
- [struct BNNSArithmeticBinary](bnnsarithmeticbinary.md)
  A structure that contains the inputs and output of an arithmetic operation with two inputs.
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

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsarithmeticunary)*