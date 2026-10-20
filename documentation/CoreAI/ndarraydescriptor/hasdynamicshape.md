# hasDynamicShape

**Framework**: Core AI  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the shape has any dynamic dimensions.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
var hasDynamicShape: Bool { get }
```

## See Also

### Inspecting descriptor properties
- [var shape: [Int]](./shape.md)
  The length of each dimension of the array.
- [var scalarType: NDArray.ScalarType](./scalartype.md)
  The scalar type of the array.
- [var rank: Int](./rank.md)
  The number of dimensions in the array.
- [var interleaveLayout: NDArray.InterleaveLayout?](./interleavelayout.md)
  Returns the interleaved layout of this ndArray, or `nil` if there is no interleave.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/ndarraydescriptor/hasdynamicshape)*