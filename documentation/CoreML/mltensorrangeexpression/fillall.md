# fillAll

**Framework**: Core ML  
**Kind**: property

The same as the ellipsis literal `...` used to indicate unspecified dimensions of the tensor.

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
static var fillAll: any MLTensorRangeExpression { get }
```

#### Discussion

For example:

```swift
let x = MLTensor(randomNormal: [1, 3, 28, 28], scalarType: Float.self)
let y = x[..., 0] // or x[.fillAll, 0]
y.shape // is [1, 3, 28]
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltensorrangeexpression/fillall)*