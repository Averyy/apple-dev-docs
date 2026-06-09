# mutatingSlice(at:)

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
mutating func mutatingSlice(at ranges: [any NDArray.RangeExpression]) -> NDArray.MutableRawView
```

#### Discussion

For example if you have a 3D NDArray and want to increment a specific region, you can slice that region, reintroduce the scalar type, and then access a span over it (or use `withUnsafeMutablePointer` if not contiguous).

```swift
/// Updates the desired channel and range of rows
func incrementRegion(
  of mutableRawView: inout NDArray.MutableRawView,
  channel: Int,
  startRow: Int,
  endRow: Int
) {
  var region = mutableRawView.mutatingSlice(at: [channel, startRow..<endRow, .all]).view(as: Float.self)
  var mutableSpan = region.contiguousElements! // contiguous region expected in this case

  for i in mutableSpan.indices {
    mutableSpan[i] += 1
  }
}
```

## Parameters

- `ranges`: The range expressions describing where to slice along each dimension. `ranges.count` must be ≤ `rank`. Unspecified trailing dimensions are assumed to be `.all`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/ndarray/mutablerawview/mutatingslice(at:)-5ts4w)*