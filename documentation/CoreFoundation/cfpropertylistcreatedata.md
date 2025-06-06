# CFPropertyListCreateData(_:_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Returns a CFData object containing a serialized representation of a given property list in a specified format.

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
func CFPropertyListCreateData(_ allocator: CFAllocator!, _ propertyList: CFPropertyList!, _ format: CFPropertyListFormat, _ options: CFOptionFlags, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFData>!
```

#### Return Value

A CFData object containing a serialized representation of `propertyList` in a the format specified by `format`. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

#### Discussion

## Parameters

- `allocator`: The allocator to use to allocate memory for the new data object. Pass   or kCFAllocatorDefault to use the current default allocator.
- `propertyList`: The property list to write out.
- `format`: A CFPropertyListFormat constant to specify the data format. See   for possible values.
- `options`: This parameter is currently unused and should be set to  .
- `error`: If this parameter is non-NULL, if an error occurs, on return this will contain a CFError error describing the problem. Ownership follows the  .

## See Also

- [func CFPropertyListWrite(CFPropertyList!, CFWriteStream!, CFPropertyListFormat, CFOptionFlags, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> CFIndex](cfpropertylistwrite(_:_:_:_:_:).md)
  Write the bytes of a serialized property list out to a stream.
- [func CFPropertyListCreateXMLData(CFAllocator!, CFPropertyList!) -> Unmanaged<CFData>!](cfpropertylistcreatexmldata(_:_:).md)
  Creates an XML representation of the specified property list.
- [func CFPropertyListWriteToStream(CFPropertyList!, CFWriteStream!, CFPropertyListFormat, UnsafeMutablePointer<Unmanaged<CFString>?>!) -> CFIndex](cfpropertylistwritetostream(_:_:_:_:).md)
  Writes the bytes of a property list serialization out to a stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfpropertylistcreatedata(_:_:_:_:_:))*