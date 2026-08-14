# write(contents:to:at:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Required**: Yes

Writes contents to the given file item.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
func write(contents: Data, to item: FSItem, at offset: off_t) async throws -> FSWriteFileResult
```

#### Discussion

FSKit expects this routine to allocate space in the file system to extend the file as necessary.

If the volume experiences an out-of-space condition, reply with an error of domain [`NSPOSIXErrorDomain`](https://developer.apple.com/documentation/foundation/nsposixerrordomain) and code `ENOSPC`.

## Parameters

- `contents`: A buffer containing the data to write to the file.
- `item`: The item to which to write. FSKit guarantees this item will be of type [`FSItem.ItemType.file`](fsitem/itemtype/file.md).
- `offset`: The offset in the file from which to start writing.
- `reply`: A block or closure to indicate success or failure. If writing succeeds, pass an instance of [`FSWriteFileResult`](fswritefileresult.md) containing the number of bytes written, the updated [`FSItem.Attributes`](fsitem/attributes.md) of the file, and the volume’s updated free space, along with a `nil` error. If writing fails, pass the relevant error as the second parameter; FSKit ignores the [`FSWriteFileResult`](fswritefileresult.md) instance in this case. For an `async` Swift implementation, there’s no reply handler; simply return the result instance or throw an error.

## See Also

- [func read(from: FSItem, at: off_t, length: Int, into: FSMutableFileDataBuffer, replyHandler: (FSReadFileResult?, (any Error)?) -> Void)](fsvolume/readwritehandler/read(from:at:length:into:replyhandler:).md)
  Reads the contents of the given file item.
- [class FSMutableFileDataBuffer](fsmutablefiledatabuffer.md)
  A wrapper object for a data buffer.
- [class FSReadFileResult](fsreadfileresult.md)
  The result of a read-file call.
- [class FSWriteFileResult](fswritefileresult.md)
  The result of a read-file call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/readwritehandler/write(contents:to:at:replyhandler:))*