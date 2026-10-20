# metadataClear(_:withDelayedWrites:)

**Framework**: FSKit  
**Kind**: method  
**Role**: Instance Method

Clears the given ranges within the buffer cache.

**Availability**:
- macOS 15.4+

## Declaration

```swift
func metadataClear(_ rangesToClear: [FSMetadataRange], withDelayedWrites: Bool) throws
```

```objc
- (BOOL) metadataClear:(NSArray<FSMetadataRange *> *) rangesToClear withDelayedWrites:(BOOL) withDelayedWrites error:(NSError **) error;
```

#### Discussion

This method clears the specified ranges in the resource’s buffer cache by writing zeroes into them.

## Parameters

- `rangesToClear`: The metadata ranges to clear.
- `withDelayedWrites`: A Boolean value that determines whether to perform the clear operation with delayed writes. The delay works in the same manner as [`delayedMetadataWriteFrom:startingAt:length:error:`](./delayedmetadatawritefrom_startingat_length_error_.md). When using delayed writes, the client can flush the metadata with [`metadataFlush()`](./metadataflush%28%29.md) or [`asynchronousMetadataFlush()`](./asynchronousmetadataflush%28%29.md). The system also flushes stale data in the buffer cache periodically.

## See Also

### Reading and writing data with kernel buffer cache
- [func metadataRead(into: UnsafeMutableRawBufferPointer, startingAt: off_t, length: Int) throws](./metadataread%28into,startingat,length%29.md)
  Synchronously reads file system metadata from the resource into a buffer.
- [func metadataWrite(from: UnsafeRawBufferPointer, startingAt: off_t, length: Int) throws](./metadatawrite%28from,startingat,length%29.md)
  Synchronously writes file system metadata from a buffer to the resource.
- [func delayedMetadataWrite(from: UnsafeRawBufferPointer, startingAt: off_t, length: Int) throws](./delayedmetadatawrite%28from,startingat,length%29.md)
  Writes file system metadata from a buffer to a cache, prior to flushing it to the resource.
- [func metadataFlush() throws](./metadataflush%28%29.md)
  Synchronously flushes the resource’s buffer cache.
- [func asynchronousMetadataFlush() throws](./asynchronousmetadataflush%28%29.md)
  Asynchronously flushes the resource’s buffer cache.
- [func metadataPurge([FSMetadataRange]) throws](./metadatapurge%28_%29.md)
  Synchronously purges the given ranges from the buffer cache.
- [class FSMetadataRange](../fsmetadatarange.md)
  A range that describes contiguous metadata segments on disk.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsblockdeviceresource/metadataclear(_:withdelayedwrites:))*