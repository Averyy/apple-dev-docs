# replace(sliceOrigin:sliceDimensions:withBytes:strides:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Replaces the contents of a slice of this tensor with data you provide.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func replace(sliceOrigin: MTLTensorExtents, sliceDimensions: MTLTensorExtents, withBytes bytes: UnsafeRawPointer, strides: MTLTensorExtents)
```

## Parameters

- `sliceOrigin`: An array of offsets, in elements, to the first element of the slice that this method writes data to.
- `sliceDimensions`: An array of sizes, in elements, of the slice this method writes data to.
- `bytes`: A pointer to bytes of data that this method copies into the slice you specify with `sliceOrigin` and `sliceDimensions`.
- `strides`: An array of strides, in elements, that describes the layout of the data in `bytes`. You are responsible for ensuring `strides` meets the following requirements: - Elements of `strides`are in monotonically non-decreasing order.
- For any `i` larger than zero, `strides[i]` is greater than or equal to `strides[i-1] * dimensions[i-1]`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltensor/replace(sliceorigin:slicedimensions:withbytes:strides:))*