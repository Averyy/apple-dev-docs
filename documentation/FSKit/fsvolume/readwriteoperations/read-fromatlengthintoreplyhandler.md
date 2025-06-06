# read(from:at:length:into:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Required**: Yes

Reads the contents of the given file item.

**Availability**:
- macOS 15.4+

## Declaration

```swift
func read(from item: FSItem, at offset: off_t, length: Int, into buffer: FSMutableFileDataBuffer) async throws -> Int
```

#### Discussion

If the number of bytes requested exceeds the number of bytes available before the end of the file, then the call copies only those bytes to `buffer`. If `offset` points past the last valid byte of the file, don’t reply with an error but set `actuallyRead` to `0`.

## Parameters

- `item`: The item from which to read. FSKit guarantees this item will be of type  .
- `offset`: The offset in the file from which to start reading.
- `length`: The number of bytes to read.
- `buffer`: A buffer to receive the bytes read from the file.
- `reply`: A block or closure to indicate success or failure. If reading succeeds, pass the number of bytes read and a   error. If reading fails, pass the number of bytes read prior to the error along with the relevant error. For an   Swift implementation, there’s no reply handler; simply return the byte count or throw an error.

## See Also

- [class FSMutableFileDataBuffer](fsmutablefiledatabuffer.md)
  A wrapper object for a data buffer.
- [func write(contents: Data, to: FSItem, at: off_t, replyHandler: (Int, (any Error)?) -> Void)](fsvolume/readwriteoperations/write(contents:to:at:replyhandler:).md)
  Writes contents to the given file item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/readwriteoperations/read(from:at:length:into:replyhandler:))*