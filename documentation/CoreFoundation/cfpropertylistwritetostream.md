# CFPropertyListWriteToStream(_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Writes the bytes of a property list serialization out to a stream.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CFPropertyListWriteToStream(_ propertyList: CFPropertyList!, _ stream: CFWriteStream!, _ format: CFPropertyListFormat, _ errorString: UnsafeMutablePointer<Unmanaged<CFString>?>!) -> CFIndex
```

#### Return Value

The number of bytes written, or `0` if an error occurred. If `0` is returned, `errorString` will contain an error message.

#### Discussion

This function leaves the stream open after reading the content. When reading a property list, this function expects the reading stream to end wherever the writing ended, so that the end of the property list data can be identified.

##### Special Considerations

> ⚠️ **Warning**:  This function is obsolete and will be deprecated soon. Use [`CFPropertyListWrite(_:_:_:_:_:)`](cfpropertylistwrite(_:_:_:_:_:).md) instead.

## Parameters

- `propertyList`: The property list to write out.
- `stream`: The stream to write to. The stream must be opened and configured—this function simply writes bytes to the stream.
- `format`: A constant that specifies the format used to write `propertyList`. See [`CFPropertyListFormat`](cfpropertylistformat.md) for possible values.
- `errorString`: On return, `NULL` if the conversion is successful, otherwise a string that describes the nature of the errors. Error messages are not localized, but may be in the future, so they are not currently suitable for comparison. Pass `NULL` if you do not wish to receive an error string. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

- [func CFPropertyListCreateData(CFAllocator!, CFPropertyList!, CFPropertyListFormat, CFOptionFlags, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFData>!](cfpropertylistcreatedata(_:_:_:_:_:).md)
  Returns a CFData object containing a serialized representation of a given property list in a specified format.
- [func CFPropertyListWrite(CFPropertyList!, CFWriteStream!, CFPropertyListFormat, CFOptionFlags, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> CFIndex](cfpropertylistwrite(_:_:_:_:_:).md)
  Write the bytes of a serialized property list out to a stream.
- [func CFPropertyListCreateXMLData(CFAllocator!, CFPropertyList!) -> Unmanaged<CFData>!](cfpropertylistcreatexmldata(_:_:).md)
  Creates an XML representation of the specified property list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfpropertylistwritetostream(_:_:_:_:))*