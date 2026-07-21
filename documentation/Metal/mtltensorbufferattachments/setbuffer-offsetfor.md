# setBuffer(_:offset:for:)

**Framework**: Metal  
**Kind**: method

Sets the buffer and byte offset to use as backing storage for the given plane.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func setBuffer(_ buffer: any MTLBuffer, offset: Int, for plane: MTLTensorPlaneType)
```

#### Discussion

The offset needs to be aligned to 128 bytes if the plane uses [`MTLTensorDataType.int2`](mtltensordatatype/int2.md), [`MTLTensorDataType.uint2`](mtltensordatatype/uint2.md), [`MTLTensorDataType.int4`](mtltensordatatype/int4.md), [`MTLTensorDataType.uint4`](mtltensordatatype/uint4.md), [`MTLTensorDataType.metalFloat4e2m1`](mtltensordatatype/metalfloat4e2m1.md), [`MTLTensorDataType.metalFloat8e4m3`](mtltensordatatype/metalfloat8e4m3.md), [`MTLTensorDataType.metalFloat8e5m2`](mtltensordatatype/metalfloat8e5m2.md), or [`MTLTensorDataType.metalFloat8ue8m0`](mtltensordatatype/metalfloat8ue8m0.md), otherwise it needs to be aligned to the size of the plane’s data type in bytes.

## Parameters

- `buffer`: The buffer to back the plane.
- `offset`: The byte offset into the buffer.
- `plane`: The plane type to associate the buffer with.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltensorbufferattachments/setbuffer(_:offset:for:))*