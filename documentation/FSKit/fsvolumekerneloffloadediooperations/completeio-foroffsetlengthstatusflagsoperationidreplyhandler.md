# completeIO(for:offset:length:status:flags:operationID:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Required**: Yes

Completes an I/O operation for a given file.

**Availability**:
- macOS 15.4+

## Declaration

```swift
func completeIO(for file: FSItem, offset: off_t, length: Int, status: any Error, flags: FSCompleteIOFlags, operationID: FSOperationID) async throws
```

#### Discussion

Implement this method by updating a file’s metadata, such as its size and modification time.

FSKit may call this method without an earlier call to [`blockmapFile(_:offset:length:flags:operationID:packer:replyHandler:)`](fsvolumekerneloffloadediooperations/blockmapfile(_:offset:length:flags:operationid:packer:replyhandler:).md). In this case, the `operationID` is `0` (Objective-C) or [`unspecified`](fsoperationid/unspecified.md) (Swift).

## Parameters

- `file`: The file for which the I/O operation completed.
- `offset`: The starting logical offset at which I/O started.
- `length`: The length of the I/O range (in bytes).
- `status`: Any error that occurred during the operation. If no error occurred, this parameter is  .
- `flags`: Flags that affect the behavior of the complete I/O operation.
- `operationID`: A unique identifier of the blockmap call. Any value other than   (Objective-C) or   (Swift) corresponds to a previous call to   with the same  .
- `reply`: A block or closure to indicate success or failure. If completing I/O fails, pass an error as the one parameter to the reply handler. If completing I/O succeeds, pass  . For an   Swift implementation, there’s no reply handler; simply throw an error or return normally.

## See Also

- [func blockmapFile(FSItem, offset: off_t, length: Int, flags: FSBlockmapFlags, operationID: FSOperationID, packer: FSExtentPacker, replyHandler: ((any Error)?) -> Void)](fsvolumekerneloffloadediooperations/blockmapfile(_:offset:length:flags:operationid:packer:replyhandler:).md)
  Maps a file’s disk space into extents, allowing the kernel to perform I/O with that space.
- [struct FSBlockmapFlags](fsblockmapflags.md)
  Flags that describe the behavior of a blockmap operation.
- [struct FSCompleteIOFlags](fscompleteioflags.md)
  Flags that describe the behavior of an I/O completion operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolumekerneloffloadediooperations/completeio(for:offset:length:status:flags:operationid:replyhandler:))*