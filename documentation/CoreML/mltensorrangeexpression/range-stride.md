# range(_:stride:)

**Framework**: Core ML  
**Kind**: method

Slice the tensor at the specified dimension.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
static func range(_ range: Range<Int>, stride: Int = 1) -> any MLTensorRangeExpression
```

#### Discussion

```swift
let x = MLTensor(randomNormal: [1, 3, 28, 28], scalarType: Float.self)
let y = x[..., 0..<2] // or x[..., .range(0..<2, stride: 1)]
y.shape // is [1, 3, 28, 2]
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltensorrangeexpression/range(_:stride:))*