# CFWriteStreamCopyError(_:)

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
func CFWriteStreamCopyError(_ stream: CFWriteStream!) -> CFError!
```

#### Return Value

A CFError object that describes the current problem with stream, or `NULL` if there is no error. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `stream`: The stream to examine.

## See Also

- [func CFWriteStreamCanAcceptBytes(CFWriteStream!) -> Bool](cfwritestreamcanacceptbytes(_:).md)
  Returns whether a writable stream can accept new data without blocking.
- [func CFWriteStreamCopyProperty(CFWriteStream!, CFStreamPropertyKey!) -> CFTypeRef!](cfwritestreamcopyproperty(_:_:).md)
  Returns the value of a property for a stream.
- [func CFWriteStreamGetError(CFWriteStream!) -> CFStreamError](cfwritestreamgeterror(_:).md)
  Returns the error status of a stream.
- [func CFWriteStreamGetStatus(CFWriteStream!) -> CFStreamStatus](cfwritestreamgetstatus(_:).md)
  Returns the current state of a stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfwritestreamcopyerror(_:))*