# readDataOfLength:fromOffset:toDestination:completionHandler:

**Framework**: MediaExtension  
**Kind**: method  
**Role**: Instance Method

Reads bytes from a byte source into a buffer.

**Availability**:
- macOS 14.0+

## Declaration

```objc
- (void) readDataOfLength:(size_t) length fromOffset:(int64_t) offset toDestination:(void *) dest completionHandler:(void (^)(size_t bytesRead, NSError *error)) completionHandler;
```

## Parameters

- `length`: The number of bytes to read.
- `offset`: The relative offset in bytes from the beginning of the file from which to start reading.
- `dest`: The block of memory to hold the data to read. Must be at least `length` bytes in length.
- `completionHandler`: The completion block to execute when the read operation finishes.

## See Also

### Performing operations on a byte source
- [func availableLength(at: Int64) -> Int64](./availablelength%28at%29.md)
  Gets the number of available bytes from the offset within the byte source.
- [func byteSourceForRelatedFileName(String) throws -> MEByteSource](./bytesourceforrelatedfilename%28_%29.md)
  Creates a new byte source for a related file.
- [func read(length: Int, from: Int64, completionHandler: (Data?, (any Error)?) -> Void)](./read%28length,from,completionhandler%29.md)
  Reads bytes from a byte source into a data object.
- [- readDataOfLength:fromOffset:toDestination:bytesRead:error:](./readdataoflength_fromoffset_todestination_bytesread_error_.md)
  Reads bytes from a byte source into a buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/mebytesource/readdataoflength:fromoffset:todestination:completionhandler:)*