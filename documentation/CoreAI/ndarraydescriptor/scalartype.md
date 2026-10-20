# scalarType

**Framework**: Core AI  
**Kind**: property  
**Role**: Instance Property

The scalar type of the array.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
var scalarType: NDArray.ScalarType { get }
```

## See Also

### Inspecting descriptor properties
- [var shape: [Int]](./shape.md)
  The length of each dimension of the array.
- [var rank: Int](./rank.md)
  The number of dimensions in the array.
- [var hasDynamicShape: Bool](./hasdynamicshape.md)
  A Boolean value that indicates whether the shape has any dynamic dimensions.
- [var interleaveLayout: NDArray.InterleaveLayout?](./interleavelayout.md)
  Returns the interleaved layout of this ndArray, or `nil` if there is no interleave.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/ndarraydescriptor/scalartype)*