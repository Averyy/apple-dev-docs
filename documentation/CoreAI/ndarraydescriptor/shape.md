# shape

**Framework**: Core AI  
**Kind**: property

The length of each dimension of the array.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var shape: [Int]
```

#### Discussion

The shape contains [`rank`](ndarraydescriptor/rank.md) elements. A value of `-1` in any dimension indicates a dynamic size.

## See Also

- [var scalarType: NDArray.ScalarType](ndarraydescriptor/scalartype.md)
  The scalar type of the array.
- [var rank: Int](ndarraydescriptor/rank.md)
  The number of dimensions in the array.
- [var hasDynamicShape: Bool](ndarraydescriptor/hasdynamicshape.md)
  A Boolean value that indicates whether the shape has any dynamic dimensions.
- [var interleaveLayout: NDArray.InterleaveLayout?](ndarraydescriptor/interleavelayout.md)
  Returns the interleaved layout of this ndArray, or `nil` if there is no interleave.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/ndarraydescriptor/shape)*