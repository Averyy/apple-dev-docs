# writeFrom:startingAt:length:error:

**Framework**: FSKit  
**Kind**: method  
**Role**: Instance Method

Synchronously writes data from from a buffer to the resource and executes a block afterwards.

**Availability**:
- macOS 15.4+

## Declaration

```objc
- (size_t) writeFrom:(void *) buffer startingAt:(off_t) offset length:(size_t) length error:(NSError **) error;
```

## Return Value

The actual number of bytes written.

## Discussion

This is a synchronous version of [`writeFrom:startingAt:length:completionHandler:`](./writefrom_startingat_length_completionhandler_.md).

> **Note**: In some cases, this method performs a partial write. In this case, the return value is shorter than the requested length, and the `error` is set to `nil`.

## Parameters

- `buffer`: A buffer to provide the data.
- `offset`: The offset into the resource from which to start writing.
- `length`: A maximum number of bytes to write. The completion handler receives a parameter with the actual number of bytes write.
- `error`: On return, any error encountered while writing data, or `nil` if no error occurred.

## See Also

### Reading and writing data
- [- readInto:startingAt:length:error:](./readinto_startingat_length_error_.md)
  Synchronously reads data from the resource into a buffer.
- [- readInto:startingAt:length:completionHandler:](./readinto_startingat_length_completionhandler_.md)
  Reads data from the resource into a buffer and executes a block afterwards.
- [- writeFrom:startingAt:length:completionHandler:](./writefrom_startingat_length_completionhandler_.md)
  Writes data from from a buffer to the resource and executes a block afterwards.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsblockdeviceresource/writefrom:startingat:length:error:)*