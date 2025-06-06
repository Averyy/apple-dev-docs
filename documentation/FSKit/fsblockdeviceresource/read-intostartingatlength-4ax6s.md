# read(into:startingAt:length:)

**Framework**: FSKit  
**Kind**: method

Synchronously reads data from the resource into a buffer.

**Availability**:
- macOS 15.4+

## Declaration

```swift
func read(into buffer: UnsafeMutableRawBufferPointer, startingAt offset: off_t, length: Int) throws -> Int
```

#### Return Value

The actual number of bytes read.

#### Discussion

This is a synchronous version of [`read(into:startingAt:length:)`](fsblockdeviceresource/read(into:startingat:length:)-4ax6s.md).

In some cases, this method performs a partial read. In this case, the return value is shorter than the requested length.

> **Note**: An error describing any read error. This value is `EFAULT` if `buffer` is `NULL`, or `errno` if reading from the resource failed.

An error describing any read error. This value is `EFAULT` if `buffer` is `NULL`, or `errno` if reading from the resource failed.

## Parameters

- `buffer`: A buffer to receive the data.
- `offset`: The offset into the resource from which to start reading.
- `length`: A maximum number of bytes to read. The method’s return value contains the actual number of bytes read.

## See Also

- [func read(into: UnsafeMutableRawBufferPointer, startingAt: off_t, length: Int) async throws -> Int](fsblockdeviceresource/read(into:startingat:length:)-5yozi.md)
  Asychronously reads data from the resource into a buffer.
- [func read(into: UnsafeMutableRawBufferPointer, startingAt: off_t, length: Int, completionHandler: (Int, (any Error)?) -> Void)](fsblockdeviceresource/read(into:startingat:length:completionhandler:).md)
  Reads data from the resource into a buffer and executes a closure afterwards.
- [func write(from: UnsafeRawBufferPointer, startingAt: off_t, length: Int) throws -> Int](fsblockdeviceresource/write(from:startingat:length:)-2fmgt.md)
  Synchronously writes data from from a buffer to the resource and executes a block afterwards.
- [func write(from: UnsafeRawBufferPointer, startingAt: off_t, length: Int) async throws -> Int](fsblockdeviceresource/write(from:startingat:length:)-9oa1x.md)
  Asynchronously writes data from from a buffer to the resource.
- [func write(from: UnsafeRawBufferPointer, startingAt: off_t, length: Int, completionHandler: (Int, (any Error)?) -> Void)](fsblockdeviceresource/write(from:startingat:length:completionhandler:).md)
  Writes data from from a buffer to the resource and executes a closure afterwards.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsblockdeviceresource/read(into:startingat:length:)-4ax6s)*