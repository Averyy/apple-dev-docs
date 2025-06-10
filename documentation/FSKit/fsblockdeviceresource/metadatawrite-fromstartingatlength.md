# metadataWrite(from:startingAt:length:)

**Framework**: FSKit  
**Kind**: method

Synchronously writes file system metadata from a buffer to the resource.

**Availability**:
- macOS 15.4+

## Declaration

```swift
func metadataWrite(from buffer: UnsafeRawBufferPointer, startingAt offset: off_t, length: Int) throws
```

#### Discussion

This method provides access to the Kernel Buffer Cache, which is the primary system cache for file system metadata. Unlike equivalent kernel APIs, this method doesn’t hold any kernel-level claim to the underlying buffers.

For the write to succeed, requests must conform to any transfer requirements of the underlying resource. Disk drives typically require sector-addressed operations of one or more sector-aligned offsets, where a sector equals `physicalBlockSize`.

This method doesn’t support partial writing of metadata.

> **Note**: Any error encountered while reading data.

## Parameters

- `buffer`: A buffer to provide the data.
- `offset`: The offset into the resource from which to start writing.
- `length`: The number of bytes to writing.

## See Also

- [func metadataRead(into: UnsafeMutableRawBufferPointer, startingAt: off_t, length: Int) throws](fsblockdeviceresource/metadataread(into:startingat:length:).md)
  Synchronously reads file system metadata from the resource into a buffer.
- [func delayedMetadataWrite(from: UnsafeRawBufferPointer, startingAt: off_t, length: Int) throws](fsblockdeviceresource/delayedmetadatawrite(from:startingat:length:).md)
  Writes file system metadata from a buffer to a cache, prior to flushing it to the resource.
- [func metadataFlush() throws](fsblockdeviceresource/metadataflush.md)
  Synchronously flushes the resource’s buffer cache.
- [func asynchronousMetadataFlush() throws](fsblockdeviceresource/asynchronousmetadataflush.md)
  Asynchronously flushes the resource’s buffer cache.
- [func metadataClear([FSMetadataRange], withDelayedWrites: Bool) throws](fsblockdeviceresource/metadataclear(_:withdelayedwrites:).md)
  Clears the given ranges within the buffer cache.
- [func metadataPurge([FSMetadataRange]) throws](fsblockdeviceresource/metadatapurge(_:).md)
  Synchronously purges the given ranges from the buffer cache.
- [class FSMetadataRange](fsmetadatarange.md)
  A range that describes contiguous metadata segments on disk.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsblockdeviceresource/metadatawrite(from:startingat:length:))*