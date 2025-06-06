# CFWriteStreamCopyProperty(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Returns the value of a property for a stream.

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
func CFWriteStreamCopyProperty(_ stream: CFWriteStream!, _ propertyName: CFStreamPropertyKey!) -> CFTypeRef!
```

#### Return Value

The value of the property `propertyName`. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

#### Discussion

Each type of stream can define a set of properties that either describe or configure individual streams. A property can be any interesting information about a stream. Examples include the headers from an HTTP transmission, the expected number of bytes, file permission information, and so on. Use [`CFWriteStreamSetProperty(_:_:_:)`](cfwritestreamsetproperty(_:_:_:).md) to modify the value of a property, although some properties are read-only.

## Parameters

- `stream`: The stream to examine.
- `propertyName`: The name of the stream property to obtain. The available properties for standard Core Foundation streams are listed in Stream Properties.

## See Also

- [func CFWriteStreamCanAcceptBytes(CFWriteStream!) -> Bool](cfwritestreamcanacceptbytes(_:).md)
  Returns whether a writable stream can accept new data without blocking.
- [func CFWriteStreamCopyError(CFWriteStream!) -> CFError!](cfwritestreamcopyerror(_:).md)
  Returns the error associated with a stream.
- [func CFWriteStreamGetError(CFWriteStream!) -> CFStreamError](cfwritestreamgeterror(_:).md)
  Returns the error status of a stream.
- [func CFWriteStreamGetStatus(CFWriteStream!) -> CFStreamStatus](cfwritestreamgetstatus(_:).md)
  Returns the current state of a stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfwritestreamcopyproperty(_:_:))*