# CFWriteStreamGetStatus(_:)

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
func CFWriteStreamGetStatus(_ stream: CFWriteStream!) -> CFStreamStatus
```

#### Return Value

The current state of `stream`. See [`CFStreamStatus`](cfstreamstatus.md) for the list of possible states.

## Parameters

- `stream`: The stream to examine.

## See Also

- [func CFWriteStreamCanAcceptBytes(CFWriteStream!) -> Bool](cfwritestreamcanacceptbytes(_:).md)
  Returns whether a writable stream can accept new data without blocking.
- [func CFWriteStreamCopyProperty(CFWriteStream!, CFStreamPropertyKey!) -> CFTypeRef!](cfwritestreamcopyproperty(_:_:).md)
  Returns the value of a property for a stream.
- [func CFWriteStreamCopyError(CFWriteStream!) -> CFError!](cfwritestreamcopyerror(_:).md)
  Returns the error associated with a stream.
- [func CFWriteStreamGetError(CFWriteStream!) -> CFStreamError](cfwritestreamgeterror(_:).md)
  Returns the error status of a stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfwritestreamgetstatus(_:))*