# CFReadStreamGetError(_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns the error status of a stream.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

> **Deprecated**: Use [`CFReadStreamCopyError(_:)`](./cfreadstreamcopyerror%28_%29.md) instead.

## Declaration

```swift
func CFReadStreamGetError(_ stream: CFReadStream!) -> CFStreamError
```

```c
extern CFStreamError CFReadStreamGetError(CFReadStreamRef stream);
```

## Return Value

The error status of `stream` returned in a [`CFStreamError`](./cfstreamerror.md) structure.

## Discussion

The error field is `0` if no error has occurred. If the error field is not `0`, the `domain` field contains a code that identifies the domain in which the value of the `error` field should be interpreted.

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
- [func CFReadStreamGetStatus(CFReadStream!) -> CFStreamStatus](./cfreadstreamgetstatus%28_%29.md)
  Returns the current state of a stream.
- [func CFReadStreamHasBytesAvailable(CFReadStream!) -> Bool](./cfreadstreamhasbytesavailable%28_%29.md)
  Returns a Boolean value that indicates whether a readable stream has data that can be read without blocking.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfreadstreamgeterror(_:))*