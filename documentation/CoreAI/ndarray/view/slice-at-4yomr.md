# slice(at:)

**Framework**: Core AI  
**Kind**: method

Returns a sub-view with the same rank as this view by slicing the dimensions at the provided ranges.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
@export(implementation)
func slice<let indexRank : Int>(at ranges: [indexRank of any NDArray.RangeExpression]) -> NDArray.View<Element>
```

#### Discussion

For example if you have a 2D NDArray and want to compute the sum of a specific row, you can slice that row and then access a span over it (or use `withUnsafePointer` if not contiguous).

```swift
/// Returns the sum of the given row.
func sumOfRow(
  of view: borrowing NDArray.View<Float>,
  row: Int
) -> Float {
  let rowSlice = view.slice(at: [row])
  let elements = rowSlice.contiguousElements! // contiguous row expected in this case

  var sum: Float = 0
  for i in elements.indices {
    sum += elements[i]
  }
  return sum
}
```

## Parameters

- `ranges`: The range expressions describing where to slice along each dimension. `indexRank` must be ≤ `rank`. Unspecified trailing dimensions are assumed to be `.all`.

## See Also

- [func slice(at: [any NDArray.RangeExpression]) -> NDArray.View<Element>](ndarray/view/slice(at:)-32gsh.md)
  Returns a sub-view with the same rank as this view by slicing the dimensions at the provided ranges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/ndarray/view/slice(at:)-4yomr)*