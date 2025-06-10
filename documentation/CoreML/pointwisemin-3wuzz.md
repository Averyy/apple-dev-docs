# pointwiseMin(_:_:)

**Framework**: Core ML  
**Kind**: func

Computes the element-wise minimum of two values.

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
func pointwiseMin(_ lhs: MLTensor, _ rhs: some MLTensorScalar & Numeric) -> MLTensor
```

#### Discussion

For example:

```swift
let x = MLTensor([1.0, 3.0, 6.0])
let y = pointwiseMin(x, 4)
await y.shapedArray(of: Float.self) // is [1.0, 3.0, 4.0]
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/pointwisemin(_:_:)-3wuzz)*