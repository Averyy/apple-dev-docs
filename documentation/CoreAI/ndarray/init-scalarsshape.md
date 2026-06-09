# init(scalars:shape:)

**Framework**: Core AI  
**Kind**: init

Initialize an ndArray with a copy of some sequence of scalars, stored in the ndArray in row-major order.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init<Scalar>(scalars: some Sequence, shape: [Int]) where Scalar : BitwiseCopyable
```

#### Discussion

This utility will construct an ndArray with a copy of the contents of some sequence. For example to make an int32 ndArray with increasing values:

```swift
var ndArray = NDArray(scalars: (0..<4) as Range<Int32>, shape: [2, 2])
// The resulting NDArray has contents:
[[0, 1], [2, 3]]
```

## Parameters

- `scalars`: A sequence of scalars to be copied into the new ndArray. Note that `Scalar` must be a type that corresponds to a scalar type found on the `NDArray.ScalarType` enum.
- `shape`: The shape of the new ndArray. The ndArray will be stored in row-major order and the scalars will be assigned in row-major order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/ndarray/init(scalars:shape:))*