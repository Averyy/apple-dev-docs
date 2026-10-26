# seekToEndReturningOffset:error:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Places the file pointer at the end of the file referenced by the file handle and returns the new file offset.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```objc
- (BOOL) seekToEndReturningOffset:(unsigned long long *) offsetInFile error:(NSError **) error;
```

#### Return Value

Returns [`false`](../../Swift/false.md) when there was an error. Otherwise, returns  [`true`](../../Swift/true.md) and sets the `offsetInFile` parameter’s pointee to the current position of the file pointer within the file.

#### Discussion

Returns [`false`](../../Swift/false.md) if called on a file handle representing a pipe or socket, or if the file descriptor is closed.

## Parameters

- `offsetInFile`: When the return value is [`true`](../../Swift/true.md), this provides the file pointer’s offset at the end of the file. This should therefore equal to the size of the file.
- `error`: When the return value is [`false`](../../Swift/false.md), this provides an [`NSError`](../nserror.md) indicating why the operation failed.

## See Also

### Seeking within a file
- [- getOffset:error:](./getoffset_error_.md)
  Get the current position of the file pointer within the file.
- [func seek(toOffset: UInt64) throws](../filehandle/seek%28tooffset%29.md)
  Moves the file pointer to the specified offset within the file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfilehandle/seektoendreturningoffset:error:)*