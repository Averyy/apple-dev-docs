# CFReadStreamCopyError(_:)

**Framework**: Core Foundation  
**Kind**: func

Returns the error associated with a stream.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CFReadStreamCopyError(_ stream: CFReadStream!) -> CFError!
```

#### Return Value

A CFError object that describes the current problem with stream, or `NULL` if there is no error. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `stream`: The stream to examine.

## See Also

- [func CFReadStreamCopyProperty(CFReadStream!, CFStreamPropertyKey!) -> CFTypeRef!](cfreadstreamcopyproperty(_:_:).md)
  Returns the value of a property for a stream.
- [func CFReadStreamGetBuffer(CFReadStream!, CFIndex, UnsafeMutablePointer<CFIndex>!) -> UnsafePointer<UInt8>!](cfreadstreamgetbuffer(_:_:_:).md)
  Returns a pointer to a stream’s internal buffer of unread data, if possible.
- [func CFReadStreamGetError(CFReadStream!) -> CFStreamError](cfreadstreamgeterror(_:).md)
  Returns the error status of a stream.
- [func CFReadStreamGetStatus(CFReadStream!) -> CFStreamStatus](cfreadstreamgetstatus(_:).md)
  Returns the current state of a stream.
- [func CFReadStreamHasBytesAvailable(CFReadStream!) -> Bool](cfreadstreamhasbytesavailable(_:).md)
  Returns a Boolean value that indicates whether a readable stream has data that can be read without blocking.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfreadstreamcopyerror(_:))*