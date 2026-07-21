# interleaveLayout

**Framework**: Core AI  
**Kind**: property

Returns the interleaved layout of this ndArray, or `nil` if there is no interleave.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
var interleaveLayout: NDArray.InterleaveLayout? { get }
```

#### Discussion

In the common case where the model was not explicitly converted with interleave specified on a tensor, this property will be `nil`.

See [`NDArray.InterleaveLayout`](ndarray/interleavelayout-swift.struct.md) for full documentation on interleaved layouts.

## See Also

- [var shape: [Int]](ndarraydescriptor/shape.md)
  The length of each dimension of the array.
- [var scalarType: NDArray.ScalarType](ndarraydescriptor/scalartype.md)
  The scalar type of the array.
- [var rank: Int](ndarraydescriptor/rank.md)
  The number of dimensions in the array.
- [var hasDynamicShape: Bool](ndarraydescriptor/hasdynamicshape.md)
  A Boolean value that indicates whether the shape has any dynamic dimensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/ndarraydescriptor/interleavelayout)*