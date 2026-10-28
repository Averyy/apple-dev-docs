# byteSourceForRelatedFileName(_:)

**Framework**: MediaExtension  
**Kind**: method  
**Role**: Instance Method

Creates a new byte source for a related file.

**Availability**:
- macOS 14.0+

## Declaration

```swift
func byteSourceForRelatedFileName(_ fileName: String) throws -> MEByteSource
```

```objc
- (MEByteSource *) byteSourceForRelatedFileName:(NSString *) fileName error:(NSError **) errorOut;
```

## Return Value

A byte source.

## Discussion

Requests creation of a new [`MEByteSource`](../mebytesource.md) for a file related to the receiving [`MEByteSource`](../mebytesource.md). Only file names returned by the [`relatedFileNamesInSameDirectory`](./relatedfilenamesinsamedirectory.md) method may be accessed.

## Parameters

- `fileName`: The related file name that exists in the byte source’s parent directory.

## See Also

### Performing operations on a byte source
- [func availableLength(at: Int64) -> Int64](./availablelength%28at%29.md)
  Gets the number of available bytes from the offset within the byte source.
- [func read(length: Int, from: Int64, completionHandler: (Data?, (any Error)?) -> Void)](./read%28length,from,completionhandler%29.md)
  Reads bytes from a byte source into a data object.
- [- readDataOfLength:fromOffset:toDestination:bytesRead:error:](./readdataoflength_fromoffset_todestination_bytesread_error_.md)
  Reads bytes from a byte source into a buffer.
- [- readDataOfLength:fromOffset:toDestination:completionHandler:](./readdataoflength_fromoffset_todestination_completionhandler_.md)
  Reads bytes from a byte source into a buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/mebytesource/bytesourceforrelatedfilename(_:))*