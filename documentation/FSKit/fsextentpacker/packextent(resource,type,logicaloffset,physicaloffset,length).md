# packExtent(resource:type:logicalOffset:physicalOffset:length:)

**Framework**: FSKit  
**Kind**: method  
**Role**: Instance Method

Packs a single extent to send to the kernel.

**Availability**:
- macOS 15.4+

## Declaration

```swift
func packExtent(resource: FSBlockDeviceResource, type: FSExtentType, logicalOffset: off_t, physicalOffset: off_t, length: Int) -> Bool
```

```objc
- (BOOL) packExtentWithResource:(FSBlockDeviceResource *) resource type:(FSExtentType) type logicalOffset:(off_t) logicalOffset physicalOffset:(off_t) physicalOffset length:(size_t) length;
```

#### Return Value

A Boolean value that indicates whether the packer can pack more extents.

## Parameters

- `resource`: The resource on which to perform I/O.
- `type`: The type of extent, indicating whether it contains valid data.
- `logicalOffset`: The extent offset within the file, in bytes.
- `physicalOffset`: The extent offset on disk, in bytes.
- `length`: The extent length, in bytes. The maximal valid length is `UINT32_MAX`.

## See Also

### Packing extents
- [enum FSExtentType](../fsextenttype.md)
  An enumeration of types of extents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsextentpacker/packextent(resource:type:logicaloffset:physicaloffset:length:))*