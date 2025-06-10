# metadataRead(into:startingAt:length:)

**Framework**: FSKit  
**Kind**: method

Synchronously reads file system metadata from the resource into a buffer.

**Availability**:
- macOS 15.4+

## Declaration

```swift
func metadataRead(into buffer: UnsafeMutableRawBufferPointer, startingAt offset: off_t, length: Int) throws
```

#### Discussion

This method provides access to the Kernel Buffer Cache, which is the primary system cache for file system metadata. Unlike equivalent kernel APIs, this method doesn’t hold any kernel-level claim to the underlying buffers.

For the read to succeed, requests must conform to any transfer requirements of the underlying resource. Disk drives typically require sector-addressed operations of one or more sector-aligned offsets, where a sector equals `physicalBlockSize`.

This method doesn’t support partial reading of metadata.

> **Note**: Any error encountered while reading data.

## Parameters

- `buffer`: A buffer to receive the data.
- `offset`: The offset into the resource from which to start reading.
- `length`: The number of bytes to read.

## See Also

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
- [func metadataPurge([FSMetadataRange]) throws](fsblockdeviceresource/metadatapurge(_:).md)
  Synchronously purges the given ranges from the buffer cache.
- [class FSMetadataRange](fsmetadatarange.md)
  A range that describes contiguous metadata segments on disk.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsblockdeviceresource/metadataread(into:startingat:length:))*