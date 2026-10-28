# pointwiseMin(_:_:)

**Framework**: Core ML  
**Kind**: func  
**Role**: Function

Computes the element-wise minimum between two values.

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
func pointwiseMin(_ lhs: some MLTensorScalar & Numeric, _ rhs: MLTensor) -> MLTensor
```

**Other overloads**:

```swift
func pointwiseMin(_ lhs: MLTensor, _ rhs: MLTensor) -> MLTensor
```

```swift
func pointwiseMin(_ lhs: MLTensor, _ rhs: some MLTensorScalar & Numeric) -> MLTensor
```

## Discussion

For example:

```swift
let x = MLTensor([1.0, 3.0, 6.0])
let y = pointwiseMin(4, x)
await y.shapedArray(of: Float.self) // is [1.0, 3.0, 4.0]
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/pointwisemin(_:_:)-44bbv)*