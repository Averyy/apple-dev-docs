# CFReadStreamGetStatus(_:)

**Framework**: Core Foundation  
**Kind**: func

Returns the current state of a stream.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func CFReadStreamGetStatus(_ stream: CFReadStream!) -> CFStreamStatus
```

#### Return Value

The current state of `stream`. See [`CFStreamStatus`](cfstreamstatus.md) for the list of possible states.

## Parameters

- `stream`: The stream to examine.

## See Also

- [func CFReadStreamCopyProperty(CFReadStream!, CFStreamPropertyKey!) -> CFTypeRef!](cfreadstreamcopyproperty(_:_:).md)
  Returns the value of a property for a stream.
- [func CFReadStreamGetBuffer(CFReadStream!, CFIndex, UnsafeMutablePointer<CFIndex>!) -> UnsafePointer<UInt8>!](cfreadstreamgetbuffer(_:_:_:).md)
  Returns a pointer to a stream’s internal buffer of unread data, if possible.
- [func CFReadStreamCopyError(CFReadStream!) -> CFError!](cfreadstreamcopyerror(_:).md)
  Returns the error associated with a stream.
- [func CFReadStreamGetError(CFReadStream!) -> CFStreamError](cfreadstreamgeterror(_:).md)
  Returns the error status of a stream.
- [func CFReadStreamHasBytesAvailable(CFReadStream!) -> Bool](cfreadstreamhasbytesavailable(_:).md)
  Returns a Boolean value that indicates whether a readable stream has data that can be read without blocking.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfreadstreamgetstatus(_:))*