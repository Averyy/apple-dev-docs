# getBytes(_:strides:sliceOrigin:sliceDimensions:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Copies data from a slice of the data plane of this tensor into a pointer you provide.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func getBytes(_ bytes: UnsafeMutableRawPointer, strides: MTLTensorExtents, sliceOrigin: MTLTensorExtents, sliceDimensions: MTLTensorExtents)
```

#### Discussion

Create the tensor with [`storageModeShared`](mtlresourceoptions/storagemodeshared.md) for CPU access via this method.

Strides need to be monotonically non-decreasing: for any `i > 0`, `strides[i] >= strides[i-1] * dimensions[i-1]`.

The first dimension of `sliceOrigin` and `sliceDimensions` needs to be byte aligned.

## Parameters

- `bytes`: A pointer to bytes of data that this method copies the slice into.
- `strides`: An array of strides, in elements, that describes the layout of the data in `bytes`.
- `sliceOrigin`: An array of per-dimension offsets that together locate the first element to copy in the tensor. Each element in this array corresponds to the dimension at the same index in `sliceDimensions`. Each offset value represents the number of elements from the start of that dimension.
- `sliceDimensions`: An array of per-dimension sizes that together define the extent of the slice to copy from the tensor. Each element in this array corresponds to the dimension at the same index in `sliceOrigin`. Each size value represents the number of elements to include along that dimension, starting from the corresponding offset in `sliceOrigin`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltensor/getbytes(_:strides:sliceorigin:slicedimensions:))*