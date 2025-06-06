# replacing(with:where:)

**Framework**: Core ML  
**Kind**: method

Returns a new tensor replacing values from `other` with the corresponding element in `self` where the associated element in `mask` is `true`.

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
func replacing(with replacement: MLTensor, where mask: MLTensor) -> MLTensor
```

#### Return Value

A new tensor of the same shape and type as `self`.

#### Discussion

For example:

```swift
let x = MLTensor([1, 2, 3], scalarType: Float.self)
let y = MLTensor([4, 5, 6], scalarType: Float.self)
let mask = MLTensor([false, true, false])
let z = x.replacing(with: y, where: mask)
await z.shapedArray(of: Float.self) // is [1, 5, 3]
```

## Parameters

- `replacement`: The replacement values where   is  .
- `mask`: The Boolean mask that determines whether the corresponding element / row should be taken from    (if the element in   is  ) or   (if  ).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltensor/replacing(with:where:)-1mnn)*