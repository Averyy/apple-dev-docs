# rank

**Framework**: Core AI  
**Kind**: property

The number of dimensions in the array.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
var rank: Int { get }
```

## See Also

- [var shape: [Int]](ndarraydescriptor/shape.md)
  The length of each dimension of the array.
- [var scalarType: NDArray.ScalarType](ndarraydescriptor/scalartype.md)
  The scalar type of the array.
- [var hasDynamicShape: Bool](ndarraydescriptor/hasdynamicshape.md)
  A Boolean value that indicates whether the shape has any dynamic dimensions.
- [var interleaveLayout: NDArray.InterleaveLayout?](ndarraydescriptor/interleavelayout.md)
  Returns the interleaved layout of this ndArray, or `nil` if there is no interleave.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/ndarraydescriptor/rank)*