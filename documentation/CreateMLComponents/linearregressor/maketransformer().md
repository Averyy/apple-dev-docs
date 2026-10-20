# makeTransformer()

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Instance Method

Creates a default-initialized transformer suitable for incremental fitting.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
func makeTransformer() -> LinearRegressorModel<Scalar>
```

Available when `Scalar` conforms to `MLShapedArrayScalar` and `BinaryFloatingPoint`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/linearregressor/maketransformer())*