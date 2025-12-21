# product(keepRank:)

**Framework**: Core ML  
**Kind**: method

Returns the product along all axes.

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
func product(keepRank: Bool = false) -> MLTensor
```

#### Return Value

The reduced tensor.

#### Discussion

```swift
let x = MLTensor(shape: [3, 2], scalars: [2, 3, 4, 5, 6, 7], scalarType: Float.self)
let y = x.product()
y.shape // is []
await y.shapedArray(of: Float.self) // is [5040.0]
```

## Parameters

- `keepRank`: A Boolean indicating whether to keep the reduced axes or not. The default value is  .

## See Also

- [func product(alongAxes:keepRank:)](mltensor/product(alongaxes:keeprank:).md)
  Returns the product along the specified axes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltensor/product(keeprank:))*