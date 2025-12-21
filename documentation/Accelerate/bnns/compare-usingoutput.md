# compare(_:_:using:output:)

**Framework**: Accelerate  
**Kind**: method

Performs an elementwise comparison of two array descriptors using the specified relational operator.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- tvOS 14.0+
- visionOS ?+
- watchOS 7.0+

## Declaration

```swift
static func compare(_ inputA: BNNSNDArrayDescriptor, _ inputB: BNNSNDArrayDescriptor, using relationalOperator: BNNS.RelationalOperator, output: BNNSNDArrayDescriptor) throws
```

## Parameters

- `inputA`: The descriptor of the first input.
- `inputB`: The descriptor of the second input.
- `relationalOperator`: The operator for comparison.
- `output`: The descriptor of the output.

## Topics

### Specifying a Relational Operator
- [struct RelationalOperator](bnns/relationaloperator.md)
  Constants that describe relational operations.

## See Also

- [struct BNNSRelationalOperator](bnnsrelationaloperator.md)
  Constants that describe relational operations.
- [func BNNSCompareTensor(UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, BNNSRelationalOperator, UnsafeMutablePointer<BNNSNDArrayDescriptor>) -> Int32](bnnscomparetensor(_:_:_:_:).md)
  Returns a tensor of Boolean type by comparing or performing a logical operation between two inputs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/compare(_:_:using:output:))*