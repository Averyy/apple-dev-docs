# blockmapFile(_:offset:length:flags:operationID:packer:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Required**: Yes

Maps a file’s disk space into extents, allowing the kernel to perform I/O with that space.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
func blockmapFile(_ file: FSItem, offset: off_t, length: Int, flags: FSBlockmapFlags, operationID: FSOperationID, packer: FSExtentPacker) async throws -> FSBlockmapResult
```

#### Discussion

FSKit calls this method when the kernel needs to get a mapping of logical-to-physical offsets of the file’s data. This call may occur as part of an I/O operation on the file, or just to get the mapping as part of an `fcntl(F_LOG2PHYS)` system call. In the case of an I/O operation on the file, `operationID` has a nonzero value; a future call to [`completeIO(for:offset:length:status:flags:operationID:replyHandler:)`](fsvolume/kerneloffloadediohandler/completeio(for:offset:length:status:flags:operationid:replyhandler:).md) uses the same `operationID` to indicate which operation it completes. In the case of an `fcntl(F_LOG2PHYS)` system call, the `operationID` parameter is `0` (Objective-C) or [`unspecified`](fsoperationid/unspecified.md) (Swift). In both cases the kernel retains the mapping, and it may perform I/O to this range (or a part of it) at any time.

If satisfying a blockmap request requires more extents than `packer` can handle, FSKit makes additional calls to this method with the same operation ID to collect the remainder.

## Parameters

- `file`: The file for which to map disk space.
- `offset`: The starting logical offset of the range to be mapped (in bytes).
- `length`: The length of the range to be mapped (in bytes).
- `flags`: Flags that affect the behavior of the blockmap operation.
- `operationID`: A unique identifier of the blockmap call. Any value other than `0` (Objective-C) or [`unspecified`](fsoperationid/unspecified.md) (Swift) indicates the beginning of an I/O operation. A value of `0` or [`unspecified`](fsoperationid/unspecified.md) indicates the kernel maps the file without performing I/O. In this case, FSKit doesn’t perform a corresponding call to [`completeIO(for:offset:length:status:flags:operationID:replyHandler:)`](fsvolume/kerneloffloadediohandler/completeio(for:offset:length:status:flags:operationid:replyhandler:).md).
- `packer`: An extent packer you use to pack the requested range of the file’s allocated disk space. FSKit sends all of the packed extents to the kernel when it invokes `reply`.
- `reply`: A block or closure to indicate success or failure. If mapping succeeds, pass an instance of [`FSBlockmapResult`](fsblockmapresult.md) containing the volume’s updated free space, along with a `nil` error. If mapping fails, pass the relevant error as the second parameter; FSKit ignores the [`FSBlockmapResult`](fsblockmapresult.md) instance in this case. For an `async` Swift implementation, there’s no reply handler; simply return the result instance or throw an error.

## See Also

- [struct FSBlockmapFlags](fsblockmapflags.md)
  Flags that describe the behavior of a blockmap operation.
- [class FSBlockmapResult](fsblockmapresult.md)
  The result of a blockmap call.
- [func completeIO(for: FSItem, offset: off_t, length: Int, status: any Error, flags: FSCompleteIOFlags, operationID: FSOperationID, replyHandler: (FSCompleteIOResult?, (any Error)?) -> Void)](fsvolume/kerneloffloadediohandler/completeio(for:offset:length:status:flags:operationid:replyhandler:).md)
  Completes an I/O operation for a given file.
- [struct FSCompleteIOFlags](fscompleteioflags.md)
  Flags that describe the behavior of an I/O completion operation.
- [class FSCompleteIOResult](fscompleteioresult.md)
  The result of a complete-I/O call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/kerneloffloadediohandler/blockmapfile(_:offset:length:flags:operationid:packer:replyhandler:))*