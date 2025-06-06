# CFPropertyListWrite(_:_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Write the bytes of a serialized property list out to a stream.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CFPropertyListWrite(_ propertyList: CFPropertyList!, _ stream: CFWriteStream!, _ format: CFPropertyListFormat, _ options: CFOptionFlags, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> CFIndex
```

#### Return Value

The number of bytes written to `stream`. If an error occurs, returns `0`.

## Parameters

- `propertyList`: The property list to write out.
- `stream`: The CFWriteStream to which to write the data. The stream must be opened and configured.
- `format`: A CFPropertyListFormat constant to specify the data format. See   for possible values.
- `options`: This parameter is currently unused and should be set to  .
- `error`: If this parameter is non-NULL, if an error occurs, on return this will contain a CFError error describing the problem. Ownership follows the  .

## See Also

- [func CFPropertyListCreateData(CFAllocator!, CFPropertyList!, CFPropertyListFormat, CFOptionFlags, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFData>!](cfpropertylistcreatedata(_:_:_:_:_:).md)
  Returns a CFData object containing a serialized representation of a given property list in a specified format.
- [func CFPropertyListCreateXMLData(CFAllocator!, CFPropertyList!) -> Unmanaged<CFData>!](cfpropertylistcreatexmldata(_:_:).md)
  Creates an XML representation of the specified property list.
- [func CFPropertyListWriteToStream(CFPropertyList!, CFWriteStream!, CFPropertyListFormat, UnsafeMutablePointer<Unmanaged<CFString>?>!) -> CFIndex](cfpropertylistwritetostream(_:_:_:_:).md)
  Writes the bytes of a property list serialization out to a stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfpropertylistwrite(_:_:_:_:_:))*