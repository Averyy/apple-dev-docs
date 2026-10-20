# read(length:from:completionHandler:)

**Framework**: MediaExtension  
**Kind**: method  
**Role**: Instance Method

Reads bytes from a byte source into a data object.

**Availability**:
- macOS 14.0+

## Declaration

```swift
func read(length: Int, from offset: Int64, completionHandler: @escaping @Sendable (Data?, (any Error)?) -> Void)
```

```swift
func read(length: Int, from offset: Int64) async throws -> Data
```

```objc
- (void) readDataOfLength:(size_t) length fromOffset:(int64_t) offset completionHandler:(void (^)(NSData *data, NSError *error)) completionHandler;
```

## Parameters

- `length`: The number of bytes to read.
- `offset`: The relative offset in bytes from the beginning of the file from which to start reading.
- `completionHandler`: The completion block to execute when the read operation finishes.

## See Also

### Performing operations on a byte source
- [func availableLength(at: Int64) -> Int64](./availablelength%28at%29.md)
  Gets the number of available bytes from the offset within the byte source.
- [func byteSourceForRelatedFileName(String) throws -> MEByteSource](./bytesourceforrelatedfilename%28_%29.md)
  Creates a new byte source for a related file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/mebytesource/read(length:from:completionhandler:))*