# slice(at:)

**Framework**: Core AI  
**Kind**: method

Returns a sub-view with the same rank as this view by slicing the dimensions at the provided ranges.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
@export(implementation)
consuming func slice(at ranges: [any NDArray.RangeExpression]) -> NDArray.MutableView<Element>
```

#### Discussion

For example if you have a 3D NDArray and want to increment a specific region, you can slice that region and then access a span over it (or use `withUnsafeMutablePointer` if not contiguous).

```swift
/// Updates the desired channel and range of rows
func incrementRegion(
  of mutableView: consuming NDArray.MutableView<Float>,
  channel: Int,
  startRow: Int,
  endRow: Int
) {
  var region = mutableView.slice(at: [channel, startRow..<endRow, .all])
  var mutableSpan = region.contiguousElements! // contiguous region expected in this case

  for i in mutableSpan.indices {
    mutableSpan[i] += 1
  }
}
```

> **Note**: If you need to avoid `consuming` the view which this is called on, you can use `mutatingSlice`.

## Parameters

- `ranges`: The range expressions describing where to slice along each dimension. `ranges.count` must be ≤ `rank`. Unspecified trailing dimensions are assumed to be `.all`.

## See Also

- [func slice<let indexRank : Int>(at: [indexRank of any NDArray.RangeExpression]) -> NDArray.MutableView<Element>](ndarray/mutableview/slice(at:)-50cpv.md)
  Returns a sub-view with the same rank as this view by slicing the dimensions at the provided ranges.
- [func mutatingSlice<let indexRank : Int>(at: [indexRank of any NDArray.RangeExpression]) -> NDArray.MutableView<Element>](ndarray/mutableview/mutatingslice(at:)-30asd.md)
  Returns a sub-view with the same rank as this view by slicing the dimensions at the provided ranges.
- [func mutatingSlice(at: [any NDArray.RangeExpression]) -> NDArray.MutableView<Element>](ndarray/mutableview/mutatingslice(at:)-9pmi4.md)
  Returns a sub-view with the same rank as this view by slicing the dimensions at the provided ranges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/ndarray/mutableview/slice(at:)-qyjq)*