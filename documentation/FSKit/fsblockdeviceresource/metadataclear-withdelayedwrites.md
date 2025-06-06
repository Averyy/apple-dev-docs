# metadataClear(_:withDelayedWrites:)

**Framework**: FSKit  
**Kind**: method

Clears the given ranges within the buffer cache.

**Availability**:
- macOS 15.4+

## Declaration

```swift
func metadataClear(_ rangesToClear: [FSMetadataRange], withDelayedWrites: Bool) throws
```

#### Discussion

This method clears the specified ranges in the resource’s buffer cache by writing zeroes into them.

## Parameters

- `rangesToClear`: The metadata ranges to clear.
- `withDelayedWrites`: A Boolean value that determines whether to perform the clear operation with delayed writes. The delay works in the same manner as  . When using delayed writes, the client can flush the metadata with   or  . The system also flushes stale data in the buffer cache periodically.

## See Also

- [func metadataRead(into: UnsafeMutableRawBufferPointer, startingAt: off_t, length: Int) throws](fsblockdeviceresource/metadataread(into:startingat:length:).md)
  Synchronously reads file system metadata from the resource into a buffer.
- [func metadataWrite(from: UnsafeRawBufferPointer, startingAt: off_t, length: Int) throws](fsblockdeviceresource/metadatawrite(from:startingat:length:).md)
  Synchronously writes file system metadata from a buffer to the resource.
- [func delayedMetadataWrite(from: UnsafeRawBufferPointer, startingAt: off_t, length: Int) throws](fsblockdeviceresource/delayedmetadatawrite(from:startingat:length:).md)
  Writes file system metadata from a buffer to a cache, prior to flushing it to the resource.
- [func metadataFlush() throws](fsblockdeviceresource/metadataflush.md)
  Synchronously flushes the resource’s buffer cache.
- [func asynchronousMetadataFlush() throws](fsblockdeviceresource/asynchronousmetadataflush.md)
  Asynchronously flushes the resource’s buffer cache.
- [func metadataPurge([FSMetadataRange]) throws](fsblockdeviceresource/metadatapurge(_:).md)
  Synchronously purges the given ranges from the buffer cache.
- [class FSMetadataRange](fsmetadatarange.md)
  A range that describes contiguous metadata segments on disk.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsblockdeviceresource/metadataclear(_:withdelayedwrites:))*