# metadataReadInto:startingAt:length:error:

**Framework**: FSKit  
**Kind**: method  
**Role**: Instance Method

Synchronously reads file system metadata from the resource into a buffer.

**Availability**:
- macOS 15.4+

## Declaration

```objc
- (BOOL) metadataReadInto:(void *) buffer startingAt:(off_t) offset length:(size_t) length error:(NSError **) error;
```

#### Return Value

A Boolean value indicating whether the metadata read succeeded.

#### Discussion

This method provides access to the Kernel Buffer Cache, which is the primary system cache for file system metadata. Unlike equivalent kernel APIs, this method doesn’t hold any kernel-level claim to the underlying buffers.

For the read to succeed, requests must conform to any transfer requirements of the underlying resource. Disk drives typically require sector (`physicalBlockSize`) addressed operations of one or more sector-aligned offsets.

> ❗ **Important**: The Kernel Buffer Cache is keyed by offset alone and doesn’t detect overlapping byte ranges between buffers. As a result, the byte ranges of any two metadata operations must never intersect. All accesses to a given disk region must use the same (offset, length) pair.

## Parameters

- `buffer`: A buffer to receive the data.
- `offset`: The offset into the resource from which to start reading.
- `length`: The number of bytes to read.
- `error`: On return, any error encountered while reading data, or `nil` if no error occurred.

## See Also

### Reading and writing data with kernel buffer cache
- [- metadataWriteFrom:startingAt:length:error:](./metadatawritefrom_startingat_length_error_.md)
  Synchronously writes file system metadata from a buffer to the resource.
- [- delayedMetadataWriteFrom:startingAt:length:error:](./delayedmetadatawritefrom_startingat_length_error_.md)
  Writes file system metadata from a buffer to a cache, prior to flushing it to the resource.
- [func metadataFlush() throws](./metadataflush%28%29.md)
  Synchronously flushes the resource’s buffer cache.
- [func asynchronousMetadataFlush() throws](./asynchronousmetadataflush%28%29.md)
  Asynchronously flushes the resource’s buffer cache.
- [func metadataClear([FSMetadataRange], withDelayedWrites: Bool) throws](./metadataclear%28_,withdelayedwrites%29.md)
  Clears the given ranges within the buffer cache.
- [func metadataPurge([FSMetadataRange]) throws](./metadatapurge%28_%29.md)
  Synchronously purges the given ranges from the buffer cache.
- [class FSMetadataRange](../fsmetadatarange.md)
  A range that describes contiguous metadata segments on disk.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsblockdeviceresource/metadatareadinto:startingat:length:error:)*