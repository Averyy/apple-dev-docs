# init(concatenating:alongAxis:)

**Framework**: Core ML  
**Kind**: init

Concatenates `tensors` along the `axis` dimension.

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
init(concatenating tensors: some Collection<MLTensor>, alongAxis axis: Int = 0)
```

#### Discussion

For example:

```swift
// t1 is [[1, 2, 3], [4, 5, 6]]
// t2 is [[7, 8, 9], [10, 11, 12]]
MLTensor(concatenating: [t1, t2]) // is [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
MLTensor(concatenating: [t1, t2], alongAxis: 1) // is [[1, 2, 3, 7, 8, 9], [4, 5, 6, 10, 11, 12]]

// t3 has shape [2, 3]
// t4 has shape [2, 3]
MLTensor(concatenating: [t3, t4]) // has shape [4, 3]
MLTensor(concatenating: [t3, t4], alongAxis: 1) // has shape [2, 6]
```

> **Note**: If you are concatenating along a new axis consider using `MLTensor(stacking:alongAxis:)`.

If you are concatenating along a new axis consider using `MLTensor(stacking:alongAxis:)`.

## Parameters

- `tensors`: The tensors to concatenate. All tensors must have the same rank and all dimensions except   must be equal.
- `axis`: The axis along which to concatenate. Negative values wrap around but must be in the range  , where    is the rank of the provided tensors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltensor/init(concatenating:alongaxis:))*