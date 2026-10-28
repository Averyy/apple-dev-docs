# metadataPurge(_:)

**Framework**: FSKit  
**Kind**: method  
**Role**: Instance Method

Synchronously purges the given ranges from the buffer cache.

**Availability**:
- macOS 15.4+

## Declaration

```swift
func metadataPurge(_ rangesToPurge: [FSMetadataRange]) throws
```

```objc
- (BOOL) metadataPurge:(NSArray<FSMetadataRange *> *) rangesToPurge error:(NSError **) error;
```

## Discussion

This method removes the given ranges from the resource’s buffer cache. This process drops any dirty data in the cache, preventing the data from reaching the device.

## Parameters

- `rangesToPurge`: The metadata ranges to purge.

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
- [func metadataClear([FSMetadataRange], withDelayedWrites: Bool) throws](./metadataclear%28_,withdelayedwrites%29.md)
  Clears the given ranges within the buffer cache.
- [class FSMetadataRange](../fsmetadatarange.md)
  A range that describes contiguous metadata segments on disk.
- [- metadataReadInto:startingAt:length:error:](./metadatareadinto_startingat_length_error_.md)
  Synchronously reads file system metadata from the resource into a buffer.
- [- metadataWriteFrom:startingAt:length:error:](./metadatawritefrom_startingat_length_error_.md)
  Synchronously writes file system metadata from a buffer to the resource.
- [- delayedMetadataWriteFrom:startingAt:length:error:](./delayedmetadatawritefrom_startingat_length_error_.md)
  Writes file system metadata from a buffer to a cache, prior to flushing it to the resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsblockdeviceresource/metadatapurge(_:))*