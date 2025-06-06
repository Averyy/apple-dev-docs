# CFReadStreamHasBytesAvailable(_:)

**Framework**: Core Foundation  
**Kind**: func

Returns a Boolean value that indicates whether a readable stream has data that can be read without blocking.

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
func CFReadStreamHasBytesAvailable(_ stream: CFReadStream!) -> Bool
```

#### Return Value

`TRUE` if data can be read from `stream` without blocking, otherwise `FALSE`. If `stream` cannot tell if data is available without actually trying to read the data, this function returns `TRUE`.

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
- [func CFReadStreamGetStatus(CFReadStream!) -> CFStreamStatus](cfreadstreamgetstatus(_:).md)
  Returns the current state of a stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfreadstreamhasbytesavailable(_:))*