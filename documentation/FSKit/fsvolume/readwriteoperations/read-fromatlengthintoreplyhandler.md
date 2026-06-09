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

- `item`: The item from which to read. FSKit guarantees this item will be of type [`FSItem.ItemType.file`](fsitem/itemtype/file.md).
- `offset`: The offset in the file from which to start reading.
- `length`: The number of bytes to read.
- `buffer`: A buffer to receive the bytes read from the file.
- `reply`: A block or closure to indicate success or failure. If reading succeeds, pass the number of bytes read and a `nil` error. If reading fails, pass the number of bytes read prior to the error along with the relevant error. For an `async` Swift implementation, there’s no reply handler; simply return the byte count or throw an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/readwriteoperations/read(from:at:length:into:replyhandler:))*