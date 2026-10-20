# compare(_:_:using:output:)

**Framework**: Accelerate  
**Kind**: method  
**Role**: Type Method

Performs an elementwise comparison of two array descriptors using the specified relational operator.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS
- watchOS 7.0+

> **Deprecated**: Use the BNNSGraph API instead.

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
- [struct RelationalOperator](./relationaloperator.md)
  Constants that describe relational operations.

## See Also

### Tensor comparison layers
- [struct BNNSRelationalOperator](../bnnsrelationaloperator.md)
  Constants that describe relational operations.
- [func BNNSCompareTensor(UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, BNNSRelationalOperator, UnsafeMutablePointer<BNNSNDArrayDescriptor>) -> Int32](../bnnscomparetensor%28_,_,_,_%29.md)
  Returns a tensor of Boolean type by comparing or performing a logical operation between two inputs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/compare(_:_:using:output:))*