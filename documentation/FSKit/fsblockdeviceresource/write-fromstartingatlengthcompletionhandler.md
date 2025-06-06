# write(from:startingAt:length:completionHandler:)

**Framework**: FSKit  
**Kind**: method

Writes data from from a buffer to the resource and executes a closure afterwards.

**Availability**:
- macOS 15.4+

## Declaration

```swift
func write(from buffer: UnsafeRawBufferPointer, startingAt offset: off_t, length: Int, completionHandler: @escaping (Int, (any Error)?) -> Void)
```

#### Discussion

For the read to succeed, requests must conform to any transfer requirements of the underlying resource. Disk drives typically require sector (`physicalBlockSize`) addressed operations of one or more sector-aligned offsets.

## Parameters

- `buffer`: A buffer to provide the data.
- `offset`: The offset into the resource from which to start writing.
- `length`: A maximum number of bytes to write. The completion handler receives a parameter with the actual number of bytes write.
- `completionHandler`: A closure that executes after the write operation completes. If successful, the first parameter contains the number of bytes actually written. In the case of an error, the second parameter contains a non-  error. This value is   if   is  , or   if writing to the resource failed.

## See Also

- [func read(into: UnsafeMutableRawBufferPointer, startingAt: off_t, length: Int) throws -> Int](fsblockdeviceresource/read(into:startingat:length:)-4ax6s.md)
  Synchronously reads data from the resource into a buffer.
- [func read(into: UnsafeMutableRawBufferPointer, startingAt: off_t, length: Int) async throws -> Int](fsblockdeviceresource/read(into:startingat:length:)-5yozi.md)
  Asychronously reads data from the resource into a buffer.
- [func read(into: UnsafeMutableRawBufferPointer, startingAt: off_t, length: Int, completionHandler: (Int, (any Error)?) -> Void)](fsblockdeviceresource/read(into:startingat:length:completionhandler:).md)
  Reads data from the resource into a buffer and executes a closure afterwards.
- [func write(from: UnsafeRawBufferPointer, startingAt: off_t, length: Int) throws -> Int](fsblockdeviceresource/write(from:startingat:length:)-2fmgt.md)
  Synchronously writes data from from a buffer to the resource and executes a block afterwards.
- [func write(from: UnsafeRawBufferPointer, startingAt: off_t, length: Int) async throws -> Int](fsblockdeviceresource/write(from:startingat:length:)-9oa1x.md)
  Asynchronously writes data from from a buffer to the resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsblockdeviceresource/write(from:startingat:length:completionhandler:))*