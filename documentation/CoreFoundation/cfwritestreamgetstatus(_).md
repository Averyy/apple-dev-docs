# CFWriteStreamGetStatus(_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns the current state of a stream.

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
func CFWriteStreamGetStatus(_ stream: CFWriteStream!) -> CFStreamStatus
```

```c
extern CFStreamStatus CFWriteStreamGetStatus(CFWriteStreamRef stream);
```

#### Return Value

The current state of `stream`. See [`CFStreamStatus`](./cfstreamstatus.md) for the list of possible states.

## Parameters

- `stream`: The stream to examine.

## See Also

### Examining Stream Properties
- [func CFWriteStreamCanAcceptBytes(CFWriteStream!) -> Bool](./cfwritestreamcanacceptbytes%28_%29.md)
  Returns whether a writable stream can accept new data without blocking.
- [func CFWriteStreamCopyProperty(CFWriteStream!, CFStreamPropertyKey!) -> CFTypeRef!](./cfwritestreamcopyproperty%28_,_%29.md)
  Returns the value of a property for a stream.
- [func CFWriteStreamCopyError(CFWriteStream!) -> CFError!](./cfwritestreamcopyerror%28_%29.md)
  Returns the error associated with a stream.
- [func CFWriteStreamGetError(CFWriteStream!) -> CFStreamError](./cfwritestreamgeterror%28_%29.md)
  Returns the error status of a stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfwritestreamgetstatus(_:))*