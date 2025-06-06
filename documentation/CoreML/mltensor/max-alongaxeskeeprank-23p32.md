# max(alongAxes:keepRank:)

**Framework**: Core ML  
**Kind**: method

Returns the maximum values along the specified axes.

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
func max(alongAxes axes: [Int], keepRank: Bool = false) -> MLTensor
```

#### Return Value

The reduced tensor.

#### Discussion

```swift
let x = MLTensor(shape: [3, 2], scalars: [2, 3, 4, 5, 6, 7], scalarType: Float.self)
let y = x.max(alongAxes: [0], keepRank: true)
y.shape // is [1, 2]
await y.shapedArray(of: Float.self) // is [6.0 7.0]
```

## Parameters

- `axes`: The axes to reduce.
- `keepRank`: A Boolean indicating whether to keep the reduced axes or not. The default value is  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltensor/max(alongaxes:keeprank:)-23p32)*