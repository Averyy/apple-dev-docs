# readDataOfLength:fromOffset:toDestination:bytesRead:error:

**Framework**: MediaExtension  
**Kind**: method  
**Role**: Instance Method

Reads bytes from a byte source into a buffer.

**Availability**:
- macOS 14.0+

## Declaration

```objc
- (BOOL) readDataOfLength:(size_t) length fromOffset:(int64_t) offset toDestination:(void *) dest bytesRead:(size_t *) bytesReadOut error:(NSError **) error;
```

## Parameters

- `length`: The number of bytes to read.
- `offset`: The relative offset in bytes from the beginning of the file from which to start reading.
- `dest`: The block of memory to hold the data to read. Must be at least `length` bytes in length.
- `bytesReadOut`: The actual number of bytes read.
- `error`: The error if one occurs, such as [`MEError.Code.endOfStream`](../meerror-swift.struct/code/endofstream.md) if there are no more bytes to read; otherwise `nil`.

## See Also

### Performing operations on a byte source
- [func availableLength(at: Int64) -> Int64](./availablelength%28at%29.md)
  Gets the number of available bytes from the offset within the byte source.
- [func byteSourceForRelatedFileName(String) throws -> MEByteSource](./bytesourceforrelatedfilename%28_%29.md)
  Creates a new byte source for a related file.
- [func read(length: Int, from: Int64, completionHandler: (Data?, (any Error)?) -> Void)](./read%28length,from,completionhandler%29.md)
  Reads bytes from a byte source into a data object.
- [- readDataOfLength:fromOffset:toDestination:completionHandler:](./readdataoflength_fromoffset_todestination_completionhandler_.md)
  Reads bytes from a byte source into a buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/mebytesource/readdataoflength:fromoffset:todestination:bytesread:error:)*