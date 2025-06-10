# CFPropertyListCreateFromStream(_:_:_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Creates a property list using data from a stream.

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
func CFPropertyListCreateFromStream(_ allocator: CFAllocator!, _ stream: CFReadStream!, _ streamLength: CFIndex, _ mutabilityOption: CFOptionFlags, _ format: UnsafeMutablePointer<CFPropertyListFormat>!, _ errorString: UnsafeMutablePointer<Unmanaged<CFString>?>!) -> Unmanaged<CFPropertyList>!
```

#### Return Value

A new property list initialized with the data contained in `stream`. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

#### Discussion

This function simply reads bytes from `stream` starting at the current location to the end, which is expected to be the end of the property list, or up to the number of bytes specified by `streamLength` if it is not `0`.

##### Special Considerations

> ⚠️ **Warning**:  This function is obsolete and will be deprecated soon. Use [`CFPropertyListCreateWithStream(_:_:_:_:_:_:)`](cfpropertylistcreatewithstream(_:_:_:_:_:_:).md) instead.

## Parameters

- `allocator`: The allocator to use to allocate memory for the new property list. Pass   or kCFAllocatorDefault to use the current default allocator.
- `stream`: The stream whose data contains the content. The stream must be opened and configured—this function simply reads bytes from the stream. The stream may contain any supported property list type (see  ).
- `streamLength`: The number of bytes to read. If  , this function will read to the end of the stream.
- `mutabilityOption`: A constant that specifies the degree of mutability for the returned property list. See   for descriptions of possible values.
- `format`: A constant that specifies the format of the property list. See   for possible values.
- `errorString`: Pass   if you do not wish to receive an error string. Ownership follows the  .

## See Also

- [func CFPropertyListCreateWithData(CFAllocator!, CFData!, CFOptionFlags, UnsafeMutablePointer<CFPropertyListFormat>!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFPropertyList>!](cfpropertylistcreatewithdata(_:_:_:_:_:).md)
  Creates a property list from a given CFData object.
- [func CFPropertyListCreateWithStream(CFAllocator!, CFReadStream!, CFIndex, CFOptionFlags, UnsafeMutablePointer<CFPropertyListFormat>!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFPropertyList>!](cfpropertylistcreatewithstream(_:_:_:_:_:_:).md)
  Create and return a property list with a CFReadStream input.
- [func CFPropertyListCreateDeepCopy(CFAllocator!, CFPropertyList!, CFOptionFlags) -> CFPropertyList!](cfpropertylistcreatedeepcopy(_:_:_:).md)
  Recursively creates a copy of a given property list.
- [func CFPropertyListCreateFromXMLData(CFAllocator!, CFData!, CFOptionFlags, UnsafeMutablePointer<Unmanaged<CFString>?>!) -> Unmanaged<CFPropertyList>!](cfpropertylistcreatefromxmldata(_:_:_:_:).md)
  Creates a property list using the specified XML or binary property list data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfpropertylistcreatefromstream(_:_:_:_:_:_:))*