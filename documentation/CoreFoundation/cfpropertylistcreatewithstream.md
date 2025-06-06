# CFPropertyListCreateWithStream(_:_:_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Create and return a property list with a CFReadStream input.

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
func CFPropertyListCreateWithStream(_ allocator: CFAllocator!, _ stream: CFReadStream!, _ streamLength: CFIndex, _ options: CFOptionFlags, _ format: UnsafeMutablePointer<CFPropertyListFormat>!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFPropertyList>!
```

#### Return Value

A new property list created from the data in `stream`. If an error occurs while parsing the data, returns `NULL`. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `allocator`: The allocator to use to allocate memory for the new property list object. Pass   or kCFAllocatorDefault to use the current default allocator.
- `stream`: A CFReadStream that contains a serialized representation of a property list.
- `streamLength`: The number of bytes to read from the stream. Pass   to read until the end of the stream is detected.
- `options`: A   constant to specify the mutability of the returned property list—see   for possible values.
- `format`: If this parameter is non- , on return it will be set to the format of the data. See   for possible values.
- `error`: If this parameter is non- , if an error occurs, on return this will contain a CFError error describing the problem. Ownership follows the  .

## See Also

- [func CFPropertyListCreateWithData(CFAllocator!, CFData!, CFOptionFlags, UnsafeMutablePointer<CFPropertyListFormat>!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFPropertyList>!](cfpropertylistcreatewithdata(_:_:_:_:_:).md)
  Creates a property list from a given CFData object.
- [func CFPropertyListCreateDeepCopy(CFAllocator!, CFPropertyList!, CFOptionFlags) -> CFPropertyList!](cfpropertylistcreatedeepcopy(_:_:_:).md)
  Recursively creates a copy of a given property list.
- [func CFPropertyListCreateFromXMLData(CFAllocator!, CFData!, CFOptionFlags, UnsafeMutablePointer<Unmanaged<CFString>?>!) -> Unmanaged<CFPropertyList>!](cfpropertylistcreatefromxmldata(_:_:_:_:).md)
  Creates a property list using the specified XML or binary property list data.
- [func CFPropertyListCreateFromStream(CFAllocator!, CFReadStream!, CFIndex, CFOptionFlags, UnsafeMutablePointer<CFPropertyListFormat>!, UnsafeMutablePointer<Unmanaged<CFString>?>!) -> Unmanaged<CFPropertyList>!](cfpropertylistcreatefromstream(_:_:_:_:_:_:).md)
  Creates a property list using data from a stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfpropertylistcreatewithstream(_:_:_:_:_:_:))*