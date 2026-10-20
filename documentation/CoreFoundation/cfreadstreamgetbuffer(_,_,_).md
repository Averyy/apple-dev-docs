# CFReadStreamGetBuffer(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns a pointer to a stream’s internal buffer of unread data, if possible.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func CFReadStreamGetBuffer(_ stream: CFReadStream!, _ maxBytesToRead: CFIndex, _ numBytesRead: UnsafeMutablePointer<CFIndex>!) -> UnsafePointer<UInt8>!
```

```c
extern const UInt8 *CFReadStreamGetBuffer(CFReadStreamRef stream, CFIndex maxBytesToRead, CFIndex *numBytesRead);
```

#### Return Value

A pointer to the internal buffer of unread data for `stream`, if possible; `NULL` otherwise. The buffer is good only until the next stream operation called on the stream. You should neither change the contents of the returned buffer nor attempt to deallocate the buffer; it is still owned by the stream. The bytes returned in the buffer are considered read from the stream.

## Parameters

- `stream`: The stream to examine.
- `maxBytesToRead`: The maximum number of bytes to read. If greater than `0`, `maxBytesToRead` limits the number of bytes read; if `0` or less, all available bytes are read.
- `numBytesRead`: On return, contains the length of returned buffer. If `stream` is not open or has encountered an error, `numBytesRead` is set to `-1`.

## See Also

### Examining Stream Properties
- [func CFReadStreamCopyProperty(CFReadStream!, CFStreamPropertyKey!) -> CFTypeRef!](./cfreadstreamcopyproperty%28_,_%29.md)
  Returns the value of a property for a stream.
- [func CFReadStreamCopyError(CFReadStream!) -> CFError!](./cfreadstreamcopyerror%28_%29.md)
  Returns the error associated with a stream.
- [func CFReadStreamGetError(CFReadStream!) -> CFStreamError](./cfreadstreamgeterror%28_%29.md)
  Returns the error status of a stream.
- [func CFReadStreamGetStatus(CFReadStream!) -> CFStreamStatus](./cfreadstreamgetstatus%28_%29.md)
  Returns the current state of a stream.
- [func CFReadStreamHasBytesAvailable(CFReadStream!) -> Bool](./cfreadstreamhasbytesavailable%28_%29.md)
  Returns a Boolean value that indicates whether a readable stream has data that can be read without blocking.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfreadstreamgetbuffer(_:_:_:))*