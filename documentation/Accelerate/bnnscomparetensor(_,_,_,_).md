# BNNSCompareTensor(_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Returns a tensor of Boolean type by comparing or performing a logical operation between two inputs.

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
func BNNSCompareTensor(_ in0: UnsafePointer<BNNSNDArrayDescriptor>, _ in1: UnsafePointer<BNNSNDArrayDescriptor>, _ op: BNNSRelationalOperator, _ out: UnsafeMutablePointer<BNNSNDArrayDescriptor>) -> Int32
```

#### Discussion

Use relational operators, for example [`BNNSRelationalOperatorGreater`](bnnsrelationaloperatorgreater.md) and [`BNNSRelationalOperatorLess`](bnnsrelationaloperatorless.md), to compare floating-point elements. The following code compares the elements of two arrays of single-precision values for equality:

```swift
let a: [Float] = [1, 2, 3, 4]
let b: [Float] = [5, 4, 3, 2]

let size = (a.count, 0, 0, 0, 0, 0, 0, 0)
let stride = (0, 0, 0, 0, 0, 0, 0, 0)

var destination = [Bool](repeating: false,
                         count: size.0)

a.withUnsafeBufferPointer { aPtr in
    b.withUnsafeBufferPointer { bPtr in
        destination.withUnsafeMutableBufferPointer { destinationPtr in
            var aDescription = BNNSNDArrayDescriptor(flags: BNNSNDArrayFlags(0),
                                                     layout: BNNSDataLayoutVector,
                                                     size: size,
                                                     stride: stride,
                                                     data: UnsafeMutableRawPointer(mutating: aPtr.baseAddress!),
                                                     data_type: .float,
                                                     table_data: nil,
                                                     table_data_type: .float,
                                                     data_scale: 1,
                                                     data_bias: 0)
            
            var bDescription = BNNSNDArrayDescriptor(flags: BNNSNDArrayFlags(0),
                                                     layout: BNNSDataLayoutVector,
                                                     size: size,
                                                     stride: stride,
                                                     data: UnsafeMutableRawPointer(mutating: bPtr.baseAddress!),
                                                     data_type: .float,
                                                     table_data: nil,
                                                     table_data_type: .float,
                                                     data_scale: 1,
                                                     data_bias: 0)
            
            var destinationDescription = BNNSNDArrayDescriptor(flags: BNNSNDArrayFlags(0),
                                                               layout: BNNSDataLayoutVector,
                                                               size: size,
                                                               stride: stride,
                                                               data: destinationPtr.baseAddress!,
                                                               data_type: BNNSDataTypeBoolean,
                                                               table_data: nil,
                                                               table_data_type: BNNSDataTypeBoolean,
                                                               data_scale: 1,
                                                               data_bias: 0)
            
            BNNSCompareTensor(&aDescription,
                              &bDescription,
                              BNNSRelationalOperatorEqual,
                              &destinationDescription)
        }
    }
}
```

On return, `destination` contains the values `[false, false, true, false]`.

Use logical operators, for example [`BNNSRelationalOperatorLogicalAND`](bnnsrelationaloperatorlogicaland.md) and [`BNNSRelationalOperatorLogicalOR`](bnnsrelationaloperatorlogicalor.md), to compare Boolean elements. The following code performs a logical AND operation on the elements of two arrays of Boolean values:

```swift

let a: [Bool] = [ true, false, false, true]
let b: [Bool] = [false, false,  true, true]

let size = (a.count, 0, 0, 0, 0, 0, 0, 0)
let stride = (0, 0, 0, 0, 0, 0, 0, 0)

var destination = [Bool](repeating: false,
                         count: size.0)

a.withUnsafeBufferPointer { aPtr in
    b.withUnsafeBufferPointer { bPtr in
        destination.withUnsafeMutableBufferPointer { destinationPtr in
            var aDescription = BNNSNDArrayDescriptor(flags: BNNSNDArrayFlags(0),
                                                     layout: BNNSDataLayoutVector,
                                                     size: size,
                                                     stride: stride,
                                                     data: UnsafeMutableRawPointer(mutating: aPtr.baseAddress!),
                                                     data_type: BNNSDataTypeBoolean,
                                                     table_data: nil,
                                                     table_data_type: BNNSDataTypeBoolean,
                                                     data_scale: 1,
                                                     data_bias: 0)
            
            var bDescription = BNNSNDArrayDescriptor(flags: BNNSNDArrayFlags(0),
                                                     layout: BNNSDataLayoutVector,
                                                     size: size,
                                                     stride: stride,
                                                     data: UnsafeMutableRawPointer(mutating: bPtr.baseAddress!),
                                                     data_type: BNNSDataTypeBoolean,
                                                     table_data: nil,
                                                     table_data_type: BNNSDataTypeBoolean,
                                                     data_scale: 1,
                                                     data_bias: 0)
            
            var destinationDescription = BNNSNDArrayDescriptor(flags: BNNSNDArrayFlags(0),
                                                               layout: BNNSDataLayoutVector,
                                                               size: size,
                                                               stride: stride,
                                                               data: destinationPtr.baseAddress!,
                                                               data_type: BNNSDataTypeBoolean,
                                                               table_data: nil,
                                                               table_data_type: BNNSDataTypeBoolean,
                                                               data_scale: 1,
                                                               data_bias: 0)
            
            BNNSCompareTensor(&aDescription,
                              &bDescription,
                              BNNSRelationalOperatorLogicalAND,
                              &destinationDescription)
            
        }
    }
}
```

On return, `destination` contains the values `[false, false, false, true]`.

## Parameters

- `in0`: The descriptor of the first input.
- `in1`: The descriptor of the second input.
- `op`: The operator for comparison.
- `out`: The descriptor of the output.

## See Also

- [static func compare(BNNSNDArrayDescriptor, BNNSNDArrayDescriptor, using: BNNS.RelationalOperator, output: BNNSNDArrayDescriptor) throws](bnns/compare(_:_:using:output:).md)
  Performs an elementwise comparison of two array descriptors using the specified relational operator.
- [struct BNNSRelationalOperator](bnnsrelationaloperator.md)
  Constants that describe relational operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnscomparetensor(_:_:_:_:))*