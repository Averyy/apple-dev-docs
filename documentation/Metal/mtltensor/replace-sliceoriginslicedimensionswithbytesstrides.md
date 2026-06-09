# replace(sliceOrigin:sliceDimensions:withBytes:strides:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Replaces a slice of the data plane plane of this tensor with data from a pointer you provide.

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

#### Discussion

Create the tensor with [`storageModeShared`](mtlresourceoptions/storagemodeshared.md) for CPU access via this method. Strides must be monotonically non-decreasing: for any `i > 0`, `strides[i] >= strides[i-1] * dimensions[i-1]`.

The first dimension of `sliceOrigin` and `sliceDimensions` must be byte aligned.

## Parameters

- `sliceOrigin`: An array of per-dimension offsets that together locate the first element to write to in the tensor. Each element in this array corresponds to the dimension at the same index in `sliceDimensions`. Each offset value represents the number of elements from the start of that dimension.
- `sliceDimensions`: An array of per-dimension sizes that together define the extent of the slice to write to in the tensor. Each element in this array corresponds to the dimension at the same index in `sliceOrigin`. Each size value represents the number of elements to include along that dimension, starting from the corresponding offset in `sliceOrigin`.
- `bytes`: A pointer to bytes of data to copy into the slice.
- `strides`: An array of strides, in elements, that describes the layout of the data in `bytes`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltensor/replace(sliceorigin:slicedimensions:withbytes:strides:))*