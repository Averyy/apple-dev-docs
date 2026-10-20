# seekToEnd()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Places the file pointer at the end of the file referenced by the file handle and returns the new file offset.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- macOS 10.15.4+
- tvOS 13.4+
- visionOS 1.0+
- watchOS 6.2+

## Declaration

```swift
@discardableResult
func seekToEnd() throws -> UInt64
```

#### Return Value

The file offset with the file pointer at the end of the file. This is therefore equal to the size of the file.

#### Discussion

Throws an error if called a file handle representing a pipe or socket, or if the file descriptor is closed.

## See Also

### Seeking within a file
- [func offset() throws -> UInt64](./offset%28%29.md)
  Gets the position of the file pointer within the file.
- [func seek(toOffset: UInt64) throws](./seek%28tooffset%29.md)
  Moves the file pointer to the specified offset within the file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filehandle/seektoend())*