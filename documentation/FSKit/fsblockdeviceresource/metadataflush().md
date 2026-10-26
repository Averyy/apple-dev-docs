# metadataFlush()

**Framework**: FSKit  
**Kind**: method  
**Role**: Instance Method

Synchronously flushes the resource’s buffer cache.

**Availability**:
- macOS 15.4+

## Declaration

```swift
func metadataFlush() throws
```

```objc
- (BOOL) metadataFlushWithError:(NSError **) error;
```

#### Discussion

This method flushes data previously written with [`delayedMetadataWriteFrom:startingAt:length:error:`](./delayedmetadatawritefrom_startingat_length_error_.md) to the resource.

## See Also

### Reading and writing data with kernel buffer cache
- [func metadataRead(into: UnsafeMutableRawBufferPointer, startingAt: off_t, length: Int) throws](./metadataread%28into,startingat,length%29.md)
  Synchronously reads file system metadata from the resource into a buffer.
- [func metadataWrite(from: UnsafeRawBufferPointer, startingAt: off_t, length: Int) throws](./metadatawrite%28from,startingat,length%29.md)
  Synchronously writes file system metadata from a buffer to the resource.
- [func delayedMetadataWrite(from: UnsafeRawBufferPointer, startingAt: off_t, length: Int) throws](./delayedmetadatawrite%28from,startingat,length%29.md)
  Writes file system metadata from a buffer to a cache, prior to flushing it to the resource.
- [func asynchronousMetadataFlush() throws](./asynchronousmetadataflush%28%29.md)
  Asynchronously flushes the resource’s buffer cache.
- [func metadataClear([FSMetadataRange], withDelayedWrites: Bool) throws](./metadataclear%28_,withdelayedwrites%29.md)
  Clears the given ranges within the buffer cache.
- [func metadataPurge([FSMetadataRange]) throws](./metadatapurge%28_%29.md)
  Synchronously purges the given ranges from the buffer cache.
- [class FSMetadataRange](../fsmetadatarange.md)
  A range that describes contiguous metadata segments on disk.
- [- metadataReadInto:startingAt:length:error:](./metadatareadinto_startingat_length_error_.md)
  Synchronously reads file system metadata from the resource into a buffer.
- [- metadataWriteFrom:startingAt:length:error:](./metadatawritefrom_startingat_length_error_.md)
  Synchronously writes file system metadata from a buffer to the resource.
- [- delayedMetadataWriteFrom:startingAt:length:error:](./delayedmetadatawritefrom_startingat_length_error_.md)
  Writes file system metadata from a buffer to a cache, prior to flushing it to the resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsblockdeviceresource/metadataflush())*