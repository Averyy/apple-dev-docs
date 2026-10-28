# write(from:)

**Framework**: Apple Archive  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Writes data from the specified buffer, not exceeding the buffer’s allocated size.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS
- watchOS 7.0+

## Declaration

```swift
func write(from buffer: UnsafeRawBufferPointer) throws -> Int
```

## Return Value

The number of bytes written by the stream.

## Discussion

This function increments the internal stream position by the number of bytes written by the stream.

## Parameters

- `buffer`: The data buffer that the operation uses as a source for the data.

## See Also

### Reading and Writing Data
- [func read(into: UnsafeMutableRawBufferPointer) throws -> Int](./read%28into%29.md)
  Reads data to the specified buffer, not exceeding the buffer’s previously allocated size.
- [func read(into: UnsafeMutableRawBufferPointer, atOffset: Int64) throws -> Int](./read%28into,atoffset%29.md)
  Reads data at the supplied offset to the specified buffer, not exceeding the buffer’s previously allocated size.
- [func write(from: UnsafeRawBufferPointer, atOffset: Int64) throws -> Int](./write%28from,atoffset%29.md)
  Writes data at the supplied offset from the specified buffer, not exceeding the buffer’s allocated size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archivebytestreamprotocol/write(from:))*