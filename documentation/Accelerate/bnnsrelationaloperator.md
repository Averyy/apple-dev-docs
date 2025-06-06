# BNNSRelationalOperator

**Framework**: Accelerate  
**Kind**: struct

Constants that describe relational operations.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct BNNSRelationalOperator
```

## Topics

### Relational Operators
- [var BNNSRelationalOperatorEqual: BNNSRelationalOperator](bnnsrelationaloperatorequal.md)
  The operator that indicates the equal-to relationship.
- [var BNNSRelationalOperatorGreater: BNNSRelationalOperator](bnnsrelationaloperatorgreater.md)
  The operator that indicates the greater-than relationship.
- [var BNNSRelationalOperatorGreaterEqual: BNNSRelationalOperator](bnnsrelationaloperatorgreaterequal.md)
  The operator that indicates the greater-than or equal-to relationship.
- [var BNNSRelationalOperatorLess: BNNSRelationalOperator](bnnsrelationaloperatorless.md)
  The operator that indicates the less-than relationship.
- [var BNNSRelationalOperatorLessEqual: BNNSRelationalOperator](bnnsrelationaloperatorlessequal.md)
  The operator that indicates the less-than or equal-to relationship.
- [var BNNSRelationalOperatorNotEqual: BNNSRelationalOperator](bnnsrelationaloperatornotequal.md)
  The operator that indicates the not-equal relationship.
### Logical Operators
- [var BNNSRelationalOperatorLogicalAND: BNNSRelationalOperator](bnnsrelationaloperatorlogicaland.md)
  The operator that indicates the logical AND relationship.
- [var BNNSRelationalOperatorLogicalNAND: BNNSRelationalOperator](bnnsrelationaloperatorlogicalnand.md)
  The operator that indicates the logical NAND relationship.
- [var BNNSRelationalOperatorLogicalNOR: BNNSRelationalOperator](bnnsrelationaloperatorlogicalnor.md)
  The operator that indicates the logical NOR relationship.
- [var BNNSRelationalOperatorLogicalNOT: BNNSRelationalOperator](bnnsrelationaloperatorlogicalnot.md)
  The operator that indicates the logical NOT relationship.
- [var BNNSRelationalOperatorLogicalOR: BNNSRelationalOperator](bnnsrelationaloperatorlogicalor.md)
  The operator that indicates the logical OR relationship.
- [var BNNSRelationalOperatorLogicalXOR: BNNSRelationalOperator](bnnsrelationaloperatorlogicalxor.md)
  The operator that indicates the logical XOR relationship.
### Raw Values
- [init(UInt32)](bnnsrelationaloperator/init(_:).md)
- [init(rawValue: UInt32)](bnnsrelationaloperator/init(rawvalue:).md)
- [var rawValue: UInt32](bnnsrelationaloperator/rawvalue.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [static func compare(BNNSNDArrayDescriptor, BNNSNDArrayDescriptor, using: BNNS.RelationalOperator, output: BNNSNDArrayDescriptor) throws](bnns/compare(_:_:using:output:).md)
  Performs an elementwise comparison of two array descriptors using the specified relational operator.
- [func BNNSCompareTensor(UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, BNNSRelationalOperator, UnsafeMutablePointer<BNNSNDArrayDescriptor>) -> Int32](bnnscomparetensor(_:_:_:_:).md)
  Returns a tensor of Boolean type by comparing or performing a logical operation between two inputs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsrelationaloperator)*