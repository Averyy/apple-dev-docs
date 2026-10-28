# seek(toOffset:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Moves the file pointer to the specified offset within the file.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func seek(toOffset offset: UInt64) throws
```

```objc
- (BOOL) seekToOffset:(unsigned long long) offset error:(NSError **) error;
```

## Discussion

> **Throws**: Throws an error if called on a file handle representing a pipe or socket, if the file descriptor is closed, or if any other error occurs while seeking.

## Parameters

- `offset`: The offset to seek to.

## See Also

### Seeking within a file
- [func offset() throws -> UInt64](./offset%28%29.md)
  Gets the position of the file pointer within the file.
- [func seekToEnd() throws -> UInt64](./seektoend%28%29.md)
  Places the file pointer at the end of the file referenced by the file handle and returns the new file offset.
- [- getOffset:error:](../nsfilehandle/getoffset_error_.md)
  Get the current position of the file pointer within the file.
- [- seekToEndReturningOffset:error:](../nsfilehandle/seektoendreturningoffset_error_.md)
  Places the file pointer at the end of the file referenced by the file handle and returns the new file offset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filehandle/seek(tooffset:))*