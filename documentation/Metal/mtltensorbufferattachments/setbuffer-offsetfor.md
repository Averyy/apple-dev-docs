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

The buffer must not be `nil`. The offset must be aligned to 128 bytes if the plane uses a format [`MTLTensorDataType`](mtltensordatatype.md), otherwise it must be aligned to the size of the plane’s data type in bytes.

## Parameters

- `buffer`: The buffer to back the plane.
- `offset`: The byte offset into the buffer.
- `plane`: The plane type to associate the buffer with.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltensorbufferattachments/setbuffer(_:offset:for:))*