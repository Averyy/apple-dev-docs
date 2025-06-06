# mean(keepRank:)

**Framework**: Core ML  
**Kind**: method

Returns the mean along all axes.

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
func mean(keepRank: Bool = false) -> MLTensor
```

#### Return Value

The reduced tensor.

#### Discussion

For example:

```swift
let x = MLTensor(shape: [3, 2], scalars: [2, 3, 4, 5, 6, 7], scalarType: Float.self)
let y = x.mean()
y.shape // is []
await y.shapedArray(of: Float.self) // is [4.5]
```

## Parameters

- `keepRank`: A Boolean indicating whether to keep the reduced axes or not. The default value is  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltensor/mean(keeprank:))*