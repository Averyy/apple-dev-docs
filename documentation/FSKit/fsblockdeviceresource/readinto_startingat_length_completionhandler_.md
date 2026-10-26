# readInto:startingAt:length:completionHandler:

**Framework**: FSKit  
**Kind**: method  
**Role**: Instance Method

Reads data from the resource into a buffer and executes a block afterwards.

**Availability**:
- macOS 15.4+

## Declaration

```objc
- (void) readInto:(void *) buffer startingAt:(off_t) offset length:(size_t) length completionHandler:(void (^)(size_t actuallyRead, NSError *error)) completionHandler;
```

#### Discussion

For the read to succeed, requests must conform to any transfer requirements of the underlying resource. Disk drives typically require sector (`physicalBlockSize`) addressed operations of one or more sector-aligned offsets.

## Parameters

- `buffer`: A buffer to receive the data.
- `offset`: The offset into the resource from which to start reading.
- `length`: A maximum number of bytes to read. The completion handler receives a parameter with the actual number of bytes read.
- `completionHandler`: A block that executes after the read operation completes. If successful, the first parameter contains the number of bytes actually read. In the case of an error, the second parameter contains a non-`nil` error. This value is `EFAULT` if `buffer` is `NULL`, or `errno` if reading from the resource failed.

## See Also

### Reading and writing data
- [- readInto:startingAt:length:error:](./readinto_startingat_length_error_.md)
  Synchronously reads data from the resource into a buffer.
- [- writeFrom:startingAt:length:error:](./writefrom_startingat_length_error_.md)
  Synchronously writes data from from a buffer to the resource and executes a block afterwards.
- [- writeFrom:startingAt:length:completionHandler:](./writefrom_startingat_length_completionhandler_.md)
  Writes data from from a buffer to the resource and executes a block afterwards.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsblockdeviceresource/readinto:startingat:length:completionhandler:)*