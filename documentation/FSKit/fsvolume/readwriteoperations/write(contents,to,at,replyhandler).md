# write(contents:to:at:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Writes contents to the given file item.

**Availability**:
- macOS 15.4+ - Deprecated in 27.0

## Declaration

```swift
func write(contents: Data, to item: FSItem, at offset: off_t, replyHandler reply: @escaping @Sendable (Int, (any Error)?) -> Void)
```

```swift
func write(contents: Data, to item: FSItem, at offset: off_t) async throws -> Int
```

```objc
- (void) writeContents:(NSData *) contents toFile:(FSItem *) item atOffset:(off_t) offset replyHandler:(void (^)(size_t actuallyWritten, NSError *error)) reply;
```

#### Discussion

FSKit expects this routine to allocate space in the file system to extend the file as necessary.

If the volume experiences an out-of-space condition, reply with an error of domain [`NSPOSIXErrorDomain`](../../../Foundation/nsposixerrordomain.md) and code `ENOSPC`.

## Parameters

- `contents`: A buffer containing the data to write to the file.
- `item`: The item to which to write. FSKit guarantees this item will be of type [`FSItem.ItemType.file`](../../fsitem/itemtype/file.md).
- `offset`: The offset in the file from which to start writing.
- `reply`: A block or closure to indicate success or failure. If writing succeeds, pass the number of bytes written and a `nil` error. If writing fails, pass the number of bytes written prior to the error along with the relevant error. For an `async` Swift implementation, there’s no reply handler; simply return the byte count or throw an error.

## See Also

### Reading and writing
- [func read(from: FSItem, at: off_t, length: Int, into: FSMutableFileDataBuffer, replyHandler: (Int, (any Error)?) -> Void)](./read%28from,at,length,into,replyhandler%29.md)
  Reads the contents of the given file item.
- [class FSMutableFileDataBuffer](../../fsmutablefiledatabuffer.md)
  A wrapper object for a data buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/readwriteoperations/write(contents:to:at:replyhandler:))*