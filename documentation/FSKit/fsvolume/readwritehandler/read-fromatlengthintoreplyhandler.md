# read(from:at:length:into:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Required**: Yes

Reads the contents of the given file item.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
func read(from item: FSItem, at offset: off_t, length: Int, into buffer: FSMutableFileDataBuffer) async throws -> FSReadFileResult
```

#### Discussion

If the number of bytes requested exceeds the number of bytes available before the end of the file, then the call copies only those bytes to `buffer`. If `offset` points past the last valid byte of the file, don’t reply with an error but set `actuallyRead` to `0`.

## Parameters

- `item`: The item from which to read. FSKit guarantees this item will be of type [`FSItem.ItemType.file`](fsitem/itemtype/file.md).
- `offset`: The offset in the file from which to start reading.
- `length`: The number of bytes to read.
- `buffer`: A buffer to receive the bytes read from the file.
- `reply`: A block or closure to indicate success or failure. If reading succeeds, pass an instance of [`FSReadFileResult`](fsreadfileresult.md) containing the number of bytes read and the updated [`FSItem.Attributes`](fsitem/attributes.md) of the file, along with a `nil` error. If reading fails, pass the relevant error as the second parameter; FSKit ignores the [`FSReadFileResult`](fsreadfileresult.md) instance in this case. For an `async` Swift implementation, there’s no reply handler; simply return the result instance or throw an error.

## See Also

- [class FSMutableFileDataBuffer](fsmutablefiledatabuffer.md)
  A wrapper object for a data buffer.
- [class FSReadFileResult](fsreadfileresult.md)
  The result of a read-file call.
- [func write(contents: Data, to: FSItem, at: off_t, replyHandler: (FSWriteFileResult?, (any Error)?) -> Void)](fsvolume/readwritehandler/write(contents:to:at:replyhandler:).md)
  Writes contents to the given file item.
- [class FSWriteFileResult](fswritefileresult.md)
  The result of a read-file call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/readwritehandler/read(from:at:length:into:replyhandler:))*