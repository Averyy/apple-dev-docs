# completeIO(for:offset:length:status:flags:operationID:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Required**: Yes

Completes an I/O operation for a given file.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
func completeIO(for file: FSItem, offset: off_t, length: Int, status: any Error, flags: FSCompleteIOFlags, operationID: FSOperationID) async throws -> FSCompleteIOResult
```

#### Discussion

`::::: Swift ::::::::::`

- reply: A block or closure to indicate success or failure. If completing I/O succeeds, pass an instance of [`FSCompleteIOResult`](fscompleteioresult.md) containing the updated [`FSItem.Attributes`](fsitem/attributes.md) of the file, along with a `nil` error. If completing I/O fails, pass the relevant error as the second parameter; FSKit ignores the [`FSCompleteIOResult`](fscompleteioresult.md) instance in this case. For an `async` Swift implementation, there’s no reply handler; simply return the result instance or throw an error.

`::::::::::::::::::::`

`::::: ObjC ::::::::::`

- result: A block or closure to indicate success or failure. If completing I/O succeeds, pass an instance of [`FSCompleteIOResult`](fscompleteioresult.md) containing the updated [`FSItem.Attributes`](fsitem/attributes.md) of the file, along with a `nil` error. If completing I/O fails, pass the relevant error as the second parameter; FSKit ignores the [`FSCompleteIOResult`](fscompleteioresult.md) instance in this case. For an `async` Swift implementation, there’s no reply handler; simply return the result instance or throw an error.

`::::::::::::::::::::`

#### Discussion

Implement this method by updating a file’s metadata, such as its size and modification time.

FSKit may call this method without an earlier call to [`blockmapFile(_:offset:length:flags:operationID:packer:replyHandler:)`](fsvolume/kerneloffloadediohandler/blockmapfile(_:offset:length:flags:operationid:packer:replyhandler:).md). In this case, the `operationID` is `0` (Objective-C) or [`unspecified`](fsoperationid/unspecified.md) (Swift).

## Parameters

- `file`: The file for which the I/O operation completed.
- `offset`: The starting logical offset at which I/O started.
- `length`: The length of the I/O range (in bytes).
- `status`: Any error that occurred during the operation. If no error occurred, this parameter is `nil`.
- `flags`: Flags that affect the behavior of the complete I/O operation.
- `operationID`: A unique identifier of the blockmap call. Any value other than `0` (Objective-C) or [`unspecified`](fsoperationid/unspecified.md) (Swift) corresponds to a previous call to [`blockmapFile(_:offset:length:flags:operationID:packer:replyHandler:)`](fsvolume/kerneloffloadediohandler/blockmapfile(_:offset:length:flags:operationid:packer:replyhandler:).md) with the same `operationID`.

## See Also

- [func blockmapFile(FSItem, offset: off_t, length: Int, flags: FSBlockmapFlags, operationID: FSOperationID, packer: FSExtentPacker, replyHandler: (FSBlockmapResult?, (any Error)?) -> Void)](fsvolume/kerneloffloadediohandler/blockmapfile(_:offset:length:flags:operationid:packer:replyhandler:).md)
  Maps a file’s disk space into extents, allowing the kernel to perform I/O with that space.
- [struct FSBlockmapFlags](fsblockmapflags.md)
  Flags that describe the behavior of a blockmap operation.
- [class FSBlockmapResult](fsblockmapresult.md)
  The result of a blockmap call.
- [struct FSCompleteIOFlags](fscompleteioflags.md)
  Flags that describe the behavior of an I/O completion operation.
- [class FSCompleteIOResult](fscompleteioresult.md)
  The result of a complete-I/O call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/kerneloffloadediohandler/completeio(for:offset:length:status:flags:operationid:replyhandler:))*