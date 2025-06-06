# CFReadStreamGetError(_:)

**Framework**: Core Foundation  
**Kind**: func

Returns the error status of a stream.

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
func CFReadStreamGetError(_ stream: CFReadStream!) -> CFStreamError
```

#### Return Value

The error status of `stream` returned in a [`CFStreamError`](cfstreamerror.md) structure.

#### Discussion

The error field is `0` if no error has occurred. If the error field is not `0`, the `domain` field contains a code that identifies the domain in which the value of the `error` field should be interpreted.

## Parameters

- `stream`: The stream to examine.

## See Also

- [func CFReadStreamCopyProperty(CFReadStream!, CFStreamPropertyKey!) -> CFTypeRef!](cfreadstreamcopyproperty(_:_:).md)
  Returns the value of a property for a stream.
- [func CFReadStreamGetBuffer(CFReadStream!, CFIndex, UnsafeMutablePointer<CFIndex>!) -> UnsafePointer<UInt8>!](cfreadstreamgetbuffer(_:_:_:).md)
  Returns a pointer to a stream’s internal buffer of unread data, if possible.
- [func CFReadStreamCopyError(CFReadStream!) -> CFError!](cfreadstreamcopyerror(_:).md)
  Returns the error associated with a stream.
- [func CFReadStreamGetStatus(CFReadStream!) -> CFStreamStatus](cfreadstreamgetstatus(_:).md)
  Returns the current state of a stream.
- [func CFReadStreamHasBytesAvailable(CFReadStream!) -> Bool](cfreadstreamhasbytesavailable(_:).md)
  Returns a Boolean value that indicates whether a readable stream has data that can be read without blocking.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfreadstreamgeterror(_:))*