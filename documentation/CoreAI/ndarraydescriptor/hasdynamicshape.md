# hasDynamicShape

**Framework**: Core AI  
**Kind**: property

A Boolean value that indicates whether the shape has any dynamic dimensions.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var hasDynamicShape: Bool { get }
```

## See Also

- [var shape: [Int]](ndarraydescriptor/shape.md)
  The length of each dimension of the array.
- [var scalarType: NDArray.ScalarType](ndarraydescriptor/scalartype.md)
  The scalar type of the array.
- [var rank: Int](ndarraydescriptor/rank.md)
  The number of dimensions in the array.
- [var interleaveLayout: NDArray.InterleaveLayout?](ndarraydescriptor/interleavelayout.md)
  Returns the interleaved layout of this ndArray, or `nil` if there is no interleave.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/ndarraydescriptor/hasdynamicshape)*