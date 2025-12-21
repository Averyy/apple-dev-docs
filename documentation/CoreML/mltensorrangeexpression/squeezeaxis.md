# squeezeAxis

**Framework**: Core ML  
**Kind**: property

Squeeze the tensor at the specified dimension.

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
static var squeezeAxis: any MLTensorRangeExpression { get }
```

#### Discussion

For example:

```swift
let x = MLTensor(randomNormal: [1, 3, 28, 28], scalarType: Float.self)
let y = x[.squeezeAxis, ...]
y.shape // is [3, 28, 28]
```

## See Also

- [static var newAxis: any MLTensorRangeExpression](mltensorrangeexpression/newaxis.md)
  Expand the tensor at the specified dimension.
- [static var fillAll: any MLTensorRangeExpression](mltensorrangeexpression/fillall.md)
  The same as the ellipsis literal `...` used to indicate unspecified dimensions of the tensor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltensorrangeexpression/squeezeaxis)*