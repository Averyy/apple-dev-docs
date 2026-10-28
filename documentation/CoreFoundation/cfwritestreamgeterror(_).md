# CFWriteStreamGetError(_:)

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

> **Deprecated**: Use [`CFWriteStreamCopyError(_:)`](./cfwritestreamcopyerror%28_%29.md) instead.

## Declaration

```swift
func CFWriteStreamGetError(_ stream: CFWriteStream!) -> CFStreamError
```

```c
extern CFStreamError CFWriteStreamGetError(CFWriteStreamRef stream);
```

## Return Value

The error status of `stream` returned in a CFStreamError structure.

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
- [func CFWriteStreamGetStatus(CFWriteStream!) -> CFStreamStatus](./cfwritestreamgetstatus%28_%29.md)
  Returns the current state of a stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfwritestreamgeterror(_:))*