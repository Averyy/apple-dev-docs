# clamped(to:)

**Framework**: Core ML  
**Kind**: method

Clamps all elements to the given upper bound, inclusively.

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
func clamped(to bounds: PartialRangeThrough<Float>) -> MLTensor
```

#### Discussion

For example:

```swift
let x = MLTensor([-1.0, 1.0, 2.0])
let y = x.clamped(to: ...1)
await y.shapedArray(of: Float.self) // is [-1.0, 1.0, 1.0]
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltensor/clamped(to:)-1objz)*