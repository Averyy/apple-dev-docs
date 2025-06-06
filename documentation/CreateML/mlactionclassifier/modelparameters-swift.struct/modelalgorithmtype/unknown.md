# !=(_:_:)

**Framework**: Create ML  
**Kind**: op

Returns a Boolean value indicating whether two values are not equal.

**Availability**:
- macOS 10.14+

## Declaration

```swift
static func != (lhs: Self, rhs: Self) -> Bool
```

#### Discussion

Inequality is the inverse of equality. For any values `a` and `b`, `a != b` implies that `a == b` is `false`.

This is the default implementation of the not-equal-to operator (`!=`) for any type that conforms to `Equatable`.

## Parameters

- `lhs`: A value to compare.
- `rhs`: Another value to compare.

## See Also

- [static func == (MLActionClassifier.ModelParameters.ModelAlgorithmType, MLActionClassifier.ModelParameters.ModelAlgorithmType) -> Bool](mlactionclassifier/modelparameters-swift.struct/modelalgorithmtype/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactionclassifier/modelparameters-swift.struct/modelalgorithmtype/!=(_:_:))*