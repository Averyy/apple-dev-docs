# CFReadStreamHasBytesAvailable(_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns a Boolean value that indicates whether a readable stream has data that can be read without blocking.

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
func CFReadStreamHasBytesAvailable(_ stream: CFReadStream!) -> Bool
```

```c
extern Boolean CFReadStreamHasBytesAvailable(CFReadStreamRef stream);
```

#### Return Value

`TRUE` if data can be read from `stream` without blocking, otherwise `FALSE`. If `stream` cannot tell if data is available without actually trying to read the data, this function returns `TRUE`.

## Parameters

- `stream`: The stream to examine.

## See Also

### Examining Stream Properties
- [func CFReadStreamCopyProperty(CFReadStream!, CFStreamPropertyKey!) -> CFTypeRef!](./cfreadstreamcopyproperty%28_,_%29.md)
  Returns the value of a property for a stream.
- [func CFReadStreamGetBuffer(CFReadStream!, CFIndex, UnsafeMutablePointer<CFIndex>!) -> UnsafePointer<UInt8>!](./cfreadstreamgetbuffer%28_,_,_%29.md)
  Returns a pointer to a stream’s internal buffer of unread data, if possible.
- [func CFReadStreamCopyError(CFReadStream!) -> CFError!](./cfreadstreamcopyerror%28_%29.md)
  Returns the error associated with a stream.
- [func CFReadStreamGetError(CFReadStream!) -> CFStreamError](./cfreadstreamgeterror%28_%29.md)
  Returns the error status of a stream.
- [func CFReadStreamGetStatus(CFReadStream!) -> CFStreamStatus](./cfreadstreamgetstatus%28_%29.md)
  Returns the current state of a stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfreadstreamhasbytesavailable(_:))*