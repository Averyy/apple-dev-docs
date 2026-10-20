# read(into:startingAt:length:completionHandler:)

**Framework**: FSKit  
**Kind**: method  
**Role**: Instance Method

Reads data from the resource into a buffer and executes a closure afterwards.

**Availability**:
- macOS 15.4+

## Declaration

```swift
func read(into buffer: UnsafeMutableRawBufferPointer, startingAt offset: off_t, length: Int, completionHandler: @escaping (Int, (any Error)?) -> Void)
```

#### Discussion

For the read to succeed, requests must conform to any transfer requirements of the underlying resource. Disk drives typically require sector (`physicalBlockSize`) addressed operations of one or more sector-aligned offsets.

## Parameters

- `buffer`: A buffer to receive the data.
- `offset`: The offset into the resource from which to start reading.
- `length`: A maximum number of bytes to read. The completion handler receives a parameter with the actual number of bytes read.
- `completionHandler`: A closure that executes after the read operation completes. If successful, the first parameter contains the number of bytes actually read. In the case of an error, the second parameter contains a non-`nil` error. This value is `EFAULT` if `buffer` is `nil`, or `errno` if reading from the resource failed.

## See Also

### Reading and writing data
- [func read(into: UnsafeMutableRawBufferPointer, startingAt: off_t, length: Int) throws -> Int](./read%28into,startingat,length%29-4ax6s.md)
  Synchronously reads data from the resource into a buffer.
- [func read(into: UnsafeMutableRawBufferPointer, startingAt: off_t, length: Int) async throws -> Int](./read%28into,startingat,length%29-5yozi.md)
  Asychronously reads data from the resource into a buffer.
- [func write(from: UnsafeRawBufferPointer, startingAt: off_t, length: Int) throws -> Int](./write%28from,startingat,length%29-2fmgt.md)
  Synchronously writes data from from a buffer to the resource and executes a block afterwards.
- [func write(from: UnsafeRawBufferPointer, startingAt: off_t, length: Int) async throws -> Int](./write%28from,startingat,length%29-9oa1x.md)
  Asynchronously writes data from from a buffer to the resource.
- [func write(from: UnsafeRawBufferPointer, startingAt: off_t, length: Int, completionHandler: (Int, (any Error)?) -> Void)](./write%28from,startingat,length,completionhandler%29.md)
  Writes data from from a buffer to the resource and executes a closure afterwards.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsblockdeviceresource/read(into:startingat:length:completionhandler:))*