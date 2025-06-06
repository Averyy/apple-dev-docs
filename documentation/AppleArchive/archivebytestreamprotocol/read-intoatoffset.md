# read(into:atOffset:)

**Framework**: Apple Archive  
**Kind**: method  
**Required**: Yes

Reads data at the supplied offset to the specified buffer, not exceeding the buffer’s previously allocated size.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- tvOS 14.0+
- visionOS ?+
- watchOS 7.0+

## Declaration

```swift
func read(into buffer: UnsafeMutableRawBufferPointer, atOffset offset: Int64) throws -> Int
```

#### Return Value

The number of bytes read by the stream.

## Parameters

- `buffer`: The data buffer that the operation fills with the read bytes.
- `offset`: The stream position of the segment that the operation reads.

## See Also

- [func read(into: UnsafeMutableRawBufferPointer) throws -> Int](archivebytestreamprotocol/read(into:).md)
  Reads data to the specified buffer, not exceeding the buffer’s previously allocated size.
- [func write(from: UnsafeRawBufferPointer) throws -> Int](archivebytestreamprotocol/write(from:).md)
  Writes data from the specified buffer, not exceeding the buffer’s allocated size.
- [func write(from: UnsafeRawBufferPointer, atOffset: Int64) throws -> Int](archivebytestreamprotocol/write(from:atoffset:).md)
  Writes data at the supplied offset from the specified buffer, not exceeding the buffer’s allocated size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archivebytestreamprotocol/read(into:atoffset:))*