# reshaped(to:)

**Framework**: Core ML  
**Kind**: method

Reshape to the specified shape.

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
func reshaped(to newShape: [Int]) -> MLTensor
```

#### Discussion

For example:

```swift
let x = MLTensor(shape: [2], scalars: [1, 2], scalarType: Float.self)
let y = x.reshaped(at: [1, 2, 1])
y.shape // is [1, 2, 1]
```

## Parameters

- `newShape`: The new shape of the array. The number of scalars matches the new shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltensor/reshaped(to:))*