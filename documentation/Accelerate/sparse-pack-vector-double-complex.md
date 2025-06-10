# sparse_pack_vector_double_complex(_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

**Availability**:
- iOS 18.5+
- iPadOS 18.5+
- Mac Catalyst 18.5+
- macOS 15.5+
- tvOS 18.5+
- visionOS 2.5+
- watchOS 11.5+

## Declaration

```swift
func sparse_pack_vector_double_complex(_ N: sparse_dimension, _ nz: sparse_dimension, _ x: OpaquePointer!, _ incx: sparse_stride, _ y: OpaquePointer!, _ indy: UnsafeMutablePointer<sparse_index>!) -> Int
```

## See Also

- [func sparse_pack_vector_float_complex(sparse_dimension, sparse_dimension, OpaquePointer!, sparse_stride, OpaquePointer!, UnsafeMutablePointer<sparse_index>!) -> Int](sparse_pack_vector_float_complex(_:_:_:_:_:_:).md)
- [func sparse_unpack_vector_double_complex(sparse_dimension, sparse_dimension, Bool, OpaquePointer!, UnsafePointer<sparse_index>!, OpaquePointer!, sparse_stride)](sparse_unpack_vector_double_complex(_:_:_:_:_:_:_:).md)
- [func sparse_unpack_vector_float_complex(sparse_dimension, sparse_dimension, Bool, OpaquePointer!, UnsafePointer<sparse_index>!, OpaquePointer!, sparse_stride)](sparse_unpack_vector_float_complex(_:_:_:_:_:_:_:).md)
- [func sparse_vector_norm_double_complex(sparse_dimension, OpaquePointer!, UnsafePointer<sparse_index>!, sparse_norm) -> Double](sparse_vector_norm_double_complex(_:_:_:_:).md)
- [func sparse_vector_norm_float_complex(sparse_dimension, OpaquePointer!, UnsafePointer<sparse_index>!, sparse_norm) -> Float](sparse_vector_norm_float_complex(_:_:_:_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparse_pack_vector_double_complex(_:_:_:_:_:_:))*