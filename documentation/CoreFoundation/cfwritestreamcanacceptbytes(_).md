# CFWriteStreamCanAcceptBytes(_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns whether a writable stream can accept new data without blocking.

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
func CFWriteStreamCanAcceptBytes(_ stream: CFWriteStream!) -> Bool
```

```c
extern Boolean CFWriteStreamCanAcceptBytes(CFWriteStreamRef stream);
```

#### Return Value

`true` if data can be written to `stream` without blocking, `false` otherwise. If `stream` cannot tell if data can be written without actually trying to write the data, this function returns `true`.

## Parameters

- `stream`: The stream to examine.

## See Also

### Examining Stream Properties
- [func CFWriteStreamCopyProperty(CFWriteStream!, CFStreamPropertyKey!) -> CFTypeRef!](./cfwritestreamcopyproperty%28_,_%29.md)
  Returns the value of a property for a stream.
- [func CFWriteStreamCopyError(CFWriteStream!) -> CFError!](./cfwritestreamcopyerror%28_%29.md)
  Returns the error associated with a stream.
- [func CFWriteStreamGetError(CFWriteStream!) -> CFStreamError](./cfwritestreamgeterror%28_%29.md)
  Returns the error status of a stream.
- [func CFWriteStreamGetStatus(CFWriteStream!) -> CFStreamStatus](./cfwritestreamgetstatus%28_%29.md)
  Returns the current state of a stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfwritestreamcanacceptbytes(_:))*