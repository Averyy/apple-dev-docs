# !=(_:_:)

**Framework**: Create ML  
**Kind**: op

Returns a Boolean value indicating whether two values are not equal.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- visionOS 1.0+

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

- [static func == (MLHandPoseClassifier.ModelParameters.ModelAlgorithmType, MLHandPoseClassifier.ModelParameters.ModelAlgorithmType) -> Bool](mlhandposeclassifier/modelparameters-swift.struct/modelalgorithmtype/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlhandposeclassifier/modelparameters-swift.struct/modelalgorithmtype/!=(_:_:))*