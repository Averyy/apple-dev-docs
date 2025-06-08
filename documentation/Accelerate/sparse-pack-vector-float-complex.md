# sparse_pack_vector_float_complex(_:_:_:_:_:_:)

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
func sparse_pack_vector_float_complex(_ N: sparse_dimension, _ nz: sparse_dimension, _ x: OpaquePointer!, _ incx: sparse_stride, _ y: OpaquePointer!, _ indy: UnsafeMutablePointer<sparse_index>!) -> Int
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparse_pack_vector_float_complex(_:_:_:_:_:_:))*