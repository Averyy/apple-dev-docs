# slice(at:)

**Framework**: Core AI  
**Kind**: method

Returns a sub-view with the same rank as this view by slicing the dimensions at the provided ranges.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
@export(implementation)
func slice(at ranges: [any NDArray.RangeExpression]) -> NDArray.RawView
```

#### Discussion

For example if you have a 2D NDArray and want to compute the sum of a specific row, you can slice that row, reintroduce the scalar type, and then access a span over it (or use `withUnsafePointer` if not contiguous).

```swift
/// Returns the sum of the given row.
func sumOfRow(
  of rawView: borrowing NDArray.RawView,
  row: Int
) -> Float {
  let rowSlice = rawView.slice(at: [row]).view(as: Float.self)
  let elements = rowSlice.contiguousElements! // contiguous row expected in this case

  var sum: Float = 0
  for i in elements.indices {
    sum += elements[i]
  }
  return sum
}
```

## Parameters

- `ranges`: The range expressions describing where to slice along each dimension. `ranges.count` must be ≤ `rank`. Unspecified trailing dimensions are assumed to be `.all`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/ndarray/rawview/slice(at:)-kd5b)*