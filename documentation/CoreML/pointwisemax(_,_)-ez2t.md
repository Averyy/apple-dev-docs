# pointwiseMax(_:_:)

**Framework**: Core ML  
**Kind**: func  
**Role**: Function

Computes the element-wise maximum of two values.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
func pointwiseMax(_ lhs: MLTensor, _ rhs: some MLTensorScalar & Numeric) -> MLTensor
```

**Other overloads**:

```swift
func pointwiseMax(_ lhs: MLTensor, _ rhs: MLTensor) -> MLTensor
```

```swift
func pointwiseMax(_ lhs: some MLTensorScalar & Numeric, _ rhs: MLTensor) -> MLTensor
```

## Discussion

For example:

```swift
let x = MLTensor([1.0, 3.0, 6.0])
let y = pointwiseMax(x, 4)
await y.shapedArray(of: Float.self) // is [4.0, 4.0, 6.0]
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/pointwisemax(_:_:)-ez2t)*