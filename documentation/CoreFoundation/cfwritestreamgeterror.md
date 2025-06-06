# CFWriteStreamGetError(_:)

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
func CFWriteStreamGetError(_ stream: CFWriteStream!) -> CFStreamError
```

#### Return Value

The error status of `stream` returned in a CFStreamError structure.

## Parameters

- `stream`: The stream to examine.

## See Also

- [func CFWriteStreamCanAcceptBytes(CFWriteStream!) -> Bool](cfwritestreamcanacceptbytes(_:).md)
  Returns whether a writable stream can accept new data without blocking.
- [func CFWriteStreamCopyProperty(CFWriteStream!, CFStreamPropertyKey!) -> CFTypeRef!](cfwritestreamcopyproperty(_:_:).md)
  Returns the value of a property for a stream.
- [func CFWriteStreamCopyError(CFWriteStream!) -> CFError!](cfwritestreamcopyerror(_:).md)
  Returns the error associated with a stream.
- [func CFWriteStreamGetStatus(CFWriteStream!) -> CFStreamStatus](cfwritestreamgetstatus(_:).md)
  Returns the current state of a stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfwritestreamgeterror(_:))*