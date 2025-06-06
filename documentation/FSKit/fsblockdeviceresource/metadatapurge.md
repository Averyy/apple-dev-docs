# metadataPurge(_:)

**Framework**: FSKit  
**Kind**: method

Synchronously purges the given ranges from the buffer cache.

**Availability**:
- macOS 15.4+

## Declaration

```swift
func metadataPurge(_ rangesToPurge: [FSMetadataRange]) throws
```

#### Discussion

This method removes the given ranges from the resource’s buffer cache. This process drops any dirty data in the cache, preventing the data from reaching the device.

## Parameters

- `rangesToPurge`: The metadata ranges to purge.

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
- [func metadataClear([FSMetadataRange], withDelayedWrites: Bool) throws](fsblockdeviceresource/metadataclear(_:withdelayedwrites:).md)
  Clears the given ranges within the buffer cache.
- [class FSMetadataRange](fsmetadatarange.md)
  A range that describes contiguous metadata segments on disk.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsblockdeviceresource/metadatapurge(_:))*