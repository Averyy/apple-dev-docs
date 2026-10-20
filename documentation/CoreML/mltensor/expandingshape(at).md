# expandingShape(at:)

**Framework**: Core ML  
**Kind**: method  
**Role**: Instance Method

Returns a shape-expanded tensor with a dimension of 1 inserted at the specified shape indices.

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
func expandingShape(at axes: Int...) -> MLTensor
```

**Other overloads**:

```swift
func expandingShape(at axes: [Int]) -> MLTensor
```

#### Discussion

For example:

```swift
let x = MLTensor(shape: [2], scalars: [1, 2], scalarType: Float.self)
let y = x.expandingShape(at: 0)
y.shape // is [1, 2]
```

## Parameters

- `axes`: The axes at which to expand the shape.

## See Also

### Accessing the extended tensor, sign and reciprocal
- [func bandPart(lowerBandCount: Int, upperBandCount: Int) -> MLTensor](./bandpart%28lowerbandcount,upperbandcount%29.md)
  Returns a new tensor with the same shape where everything outside a central band in each innermost matrix is set to zero.
- [func tiled(multiples: [Int]) -> MLTensor](./tiled%28multiples%29.md)
  Returns a tensor by replicating its elements multiple times.
- [func sign() -> MLTensor](./sign%28%29.md)
  Returns the sign of the tensor’s elements.
- [func reciprocal() -> MLTensor](./reciprocal%28%29.md)
  Computes the reciprocal of the tensor’s elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltensor/expandingshape(at:))*