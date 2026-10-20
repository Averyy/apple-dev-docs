# write(from:startingAt:length:)

**Framework**: FSKit  
**Kind**: method

Synchronously writes data from from a buffer to the resource and executes a block afterwards.

**Availability**:
- macOS 15.4+

## Declaration

```swift
func write(from buffer: UnsafeRawBufferPointer, startingAt offset: off_t, length: Int) throws -> Int
```

#### Return Value

The actual number of bytes written.

#### Discussion

This method is a synchronous version of [`writeFrom:startingAt:length:completionHandler:`](fsblockdeviceresource/writefrom:startingat:length:completionhandler:.md).

In some cases, this method performs a partial write. In this case, the return value is shorter than the requested length, and the `error` is set to `nil`.

> **Note**: Any error encountered while writing data.

## Parameters

- `buffer`: A buffer to provide the data.
- `offset`: The offset into the resource from which to start writing.
- `length`: A maximum number of bytes to write. The completion handler receives a parameter with the actual number of bytes write.

## See Also

- [func read(into: UnsafeMutableRawBufferPointer, startingAt: off_t, length: Int) throws -> Int](fsblockdeviceresource/read(into:startingat:length:)-4ax6s.md)
  Synchronously reads data from the resource into a buffer.
- [func read(into: UnsafeMutableRawBufferPointer, startingAt: off_t, length: Int) async throws -> Int](fsblockdeviceresource/read(into:startingat:length:)-5yozi.md)
  Asychronously reads data from the resource into a buffer.
- [func read(into: UnsafeMutableRawBufferPointer, startingAt: off_t, length: Int, completionHandler: (Int, (any Error)?) -> Void)](fsblockdeviceresource/read(into:startingat:length:completionhandler:).md)
  Reads data from the resource into a buffer and executes a closure afterwards.
- [func write(from: UnsafeRawBufferPointer, startingAt: off_t, length: Int) async throws -> Int](fsblockdeviceresource/write(from:startingat:length:)-9oa1x.md)
  Asynchronously writes data from from a buffer to the resource.
- [func write(from: UnsafeRawBufferPointer, startingAt: off_t, length: Int, completionHandler: (Int, (any Error)?) -> Void)](fsblockdeviceresource/write(from:startingat:length:completionhandler:).md)
  Writes data from from a buffer to the resource and executes a closure afterwards.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsblockdeviceresource/write(from:startingat:length:)-2fmgt)*