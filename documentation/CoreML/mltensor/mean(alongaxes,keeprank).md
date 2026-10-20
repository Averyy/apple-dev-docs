# mean(alongAxes:keepRank:)

**Framework**: Core ML  
**Kind**: method  
**Role**: Instance Method

Returns the mean along the specified axes.

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
func mean(alongAxes axes: Int..., keepRank: Bool = false) -> MLTensor
```

**Other overloads**:

```swift
func mean(alongAxes axes: [Int], keepRank: Bool = false) -> MLTensor
```

#### Return Value

The reduced tensor.

#### Discussion

For example:

```swift
let x = MLTensor(shape: [3, 2], scalars: [2, 3, 4, 5, 6, 7], scalarType: Float.self)
let y = x.mean(alongAxes: 0, keepRank: true)
y.shape // is [1, 2]
await y.shapedArray(of: Float.self) // is [4.0 5.0]
```

## Parameters

- `axes`: The axes to reduce.
- `keepRank`: A Boolean indicating whether to keep the reduced axes or not. The default value is `false`.

## See Also

### Accessing the minimum, maximum and mean
- [func min(alongAxes:keepRank:)](./min%28alongaxes,keeprank%29.md)
  Returns the minimum values along the specified axes.
- [func min(keepRank: Bool) -> MLTensor](./min%28keeprank%29.md)
  Returns the minimum value in the array.
- [func max(alongAxes:keepRank:)](./max%28alongaxes,keeprank%29.md)
  Returns the maximum values along the specified axes.
- [func max(keepRank: Bool) -> MLTensor](./max%28keeprank%29.md)
  Returns the maximum value in the array.
- [func mean(keepRank: Bool) -> MLTensor](./mean%28keeprank%29.md)
  Returns the mean along all axes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltensor/mean(alongaxes:keeprank:))*