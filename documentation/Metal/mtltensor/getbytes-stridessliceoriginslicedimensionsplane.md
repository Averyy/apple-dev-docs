# getBytes(_:strides:sliceOrigin:sliceDimensions:plane:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Copies data from a slice of a plane of this tensor into a pointer you provide.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func getBytes(_ bytes: UnsafeMutableRawPointer, strides: MTLTensorExtents, sliceOrigin: MTLTensorExtents, sliceDimensions: MTLTensorExtents, plane: MTLTensorPlaneType)
```

#### Discussion

When reading from auxiliary planes, specify `sliceOrigin` and `sliceDimensions` in plane coordinates by applying the auxiliary plane’s block factors.

Create the tensor with [`storageModeShared`](mtlresourceoptions/storagemodeshared.md) for CPU access via this method.

Strides need to be monotonically non-decreasing: for any `i > 0`, `strides[i] >= strides[i-1] * dimensions[i-1]`.

The first dimension of `sliceOrigin` and `sliceDimensions` needs to be byte aligned.

## Parameters

- `bytes`: A pointer to bytes of data that this method copies the slice into.
- `strides`: An array of strides, in elements, that describes the layout of the data in `bytes`.
- `sliceOrigin`: An array of per-dimension offsets that together locate the first element to copy in the tensor. Each element in this array corresponds to the dimension at the same index in `sliceDimensions`. Each offset value represents the number of elements from the start of that dimension.
- `sliceDimensions`: An array of per-dimension sizes that together define the extent of the slice to copy from the tensor. Each element in this array corresponds to the dimension at the same index in `sliceOrigin`. Each size value represents the number of elements to include along that dimension, starting from the corresponding offset in `sliceOrigin`.
- `plane`: The plane the method reads data from.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltensor/getbytes(_:strides:sliceorigin:slicedimensions:plane:))*