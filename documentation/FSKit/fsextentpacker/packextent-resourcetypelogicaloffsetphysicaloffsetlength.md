# packExtent(resource:type:logicalOffset:physicalOffset:length:)

**Framework**: FSKit  
**Kind**: method

Packs a single extent to send to the kernel.

**Availability**:
- macOS 15.4+

## Declaration

```swift
func packExtent(resource: FSBlockDeviceResource, type: FSExtentType, logicalOffset: off_t, physicalOffset: off_t, length: Int) -> Bool
```

#### Return Value

A Boolean value that indicates whether the packer can pack more extents.

## Parameters

- `resource`: The resource on which to perform I/O.
- `type`: The type of extent, indicating whether it contains valid data.
- `logicalOffset`: The extent offset within the file, in bytes.
- `physicalOffset`: The extent offset on disk, in bytes.
- `length`: The extent length, in bytes.

## See Also

- [enum FSExtentType](fsextenttype.md)
  An enumeration of types of extents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsextentpacker/packextent(resource:type:logicaloffset:physicaloffset:length:))*