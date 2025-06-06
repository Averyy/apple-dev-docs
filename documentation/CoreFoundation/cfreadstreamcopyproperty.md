# CFReadStreamCopyProperty(_:_:)

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
func CFReadStreamCopyProperty(_ stream: CFReadStream!, _ propertyName: CFStreamPropertyKey!) -> CFTypeRef!
```

#### Return Value

The value of the property `propertyName`. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

#### Discussion

Each type of stream can define a set of properties that either describe or configure individual streams. A property can be any information about a stream, other than the actual data the stream handles. Examples include the headers from an HTTP transmission, the expected number of bytes, file permission information, and so on. Use [`CFReadStreamSetProperty(_:_:_:)`](cfreadstreamsetproperty(_:_:_:).md) to modify the value of a property, although some properties are read-only.

## Parameters

- `stream`: The stream to examine.
- `propertyName`: The name of the stream property to obtain. The available properties for standard Core Foundation streams are listed in  .

## See Also

- [func CFReadStreamGetBuffer(CFReadStream!, CFIndex, UnsafeMutablePointer<CFIndex>!) -> UnsafePointer<UInt8>!](cfreadstreamgetbuffer(_:_:_:).md)
  Returns a pointer to a stream’s internal buffer of unread data, if possible.
- [func CFReadStreamCopyError(CFReadStream!) -> CFError!](cfreadstreamcopyerror(_:).md)
  Returns the error associated with a stream.
- [func CFReadStreamGetError(CFReadStream!) -> CFStreamError](cfreadstreamgeterror(_:).md)
  Returns the error status of a stream.
- [func CFReadStreamGetStatus(CFReadStream!) -> CFStreamStatus](cfreadstreamgetstatus(_:).md)
  Returns the current state of a stream.
- [func CFReadStreamHasBytesAvailable(CFReadStream!) -> Bool](cfreadstreamhasbytesavailable(_:).md)
  Returns a Boolean value that indicates whether a readable stream has data that can be read without blocking.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfreadstreamcopyproperty(_:_:))*