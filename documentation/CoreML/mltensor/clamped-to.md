# clamped(to:)

**Framework**: Core ML  
**Kind**: method

Clamps all elements to the given lower and upper bounds, inclusively.

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
func clamped(to bounds: ClosedRange<Float>) -> MLTensor
```

#### Discussion

For example:

```swift
let x = MLTensor([-1.0, 1.0, 2.0])
let y = x.clamped(to: 0...1)
await y.shapedArray(of: Float.self) // is [0.0, 1.0, 1.0]
```

## See Also

- [func concatenated(with: MLTensor, alongAxis: Int) -> MLTensor](mltensor/concatenated(with:alongaxis:).md)
  Returns a concatenated tensor along the specified axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltensor/clamped(to:))*