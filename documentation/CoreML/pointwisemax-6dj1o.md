# pointwiseMax(_:_:)

**Framework**: Core ML  
**Kind**: func

Computes the element-wise maximum of two values.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
func pointwiseMax(_ lhs: some MLTensorScalar & Numeric, _ rhs: MLTensor) -> MLTensor
```

#### Discussion

For example:

```swift
let x = MLTensor([1.0, 3.0, 6.0])
let y = pointwiseMax(4, x)
await y.shapedArray(of: Float.self) // is [4.0, 4.0, 6.0]
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/pointwisemax(_:_:)-6dj1o)*