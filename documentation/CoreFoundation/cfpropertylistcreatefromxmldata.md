# CFPropertyListCreateFromXMLData(_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Creates a property list using the specified XML or binary property list data.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CFPropertyListCreateFromXMLData(_ allocator: CFAllocator!, _ xmlData: CFData!, _ mutabilityOption: CFOptionFlags, _ errorString: UnsafeMutablePointer<Unmanaged<CFString>?>!) -> Unmanaged<CFPropertyList>!
```

#### Return Value

A new property list if the conversion is successful, otherwise `NULL`. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

#### Discussion

> ⚠️ **Warning**:  This function is obsolete and will be deprecated soon. Use [`CFPropertyListCreateWithData(_:_:_:_:_:)`](cfpropertylistcreatewithdata(_:_:_:_:_:).md) instead.

## Parameters

- `allocator`: The allocator to use to allocate memory for the new property list. Pass   or kCFAllocatorDefault to use the current default allocator.
- `xmlData`: The raw bytes to convert into a property list. The bytes may be the content of an XML file or of a binary property list (see  ).
- `mutabilityOption`: A constant that specifies the degree of mutability for the returned property list. See   for descriptions of possible values.
- `errorString`: Pass   if you do not wish to receive an error string. Ownership follows the  .

## See Also

- [func CFPropertyListCreateWithData(CFAllocator!, CFData!, CFOptionFlags, UnsafeMutablePointer<CFPropertyListFormat>!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFPropertyList>!](cfpropertylistcreatewithdata(_:_:_:_:_:).md)
  Creates a property list from a given CFData object.
- [func CFPropertyListCreateWithStream(CFAllocator!, CFReadStream!, CFIndex, CFOptionFlags, UnsafeMutablePointer<CFPropertyListFormat>!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFPropertyList>!](cfpropertylistcreatewithstream(_:_:_:_:_:_:).md)
  Create and return a property list with a CFReadStream input.
- [func CFPropertyListCreateDeepCopy(CFAllocator!, CFPropertyList!, CFOptionFlags) -> CFPropertyList!](cfpropertylistcreatedeepcopy(_:_:_:).md)
  Recursively creates a copy of a given property list.
- [func CFPropertyListCreateFromStream(CFAllocator!, CFReadStream!, CFIndex, CFOptionFlags, UnsafeMutablePointer<CFPropertyListFormat>!, UnsafeMutablePointer<Unmanaged<CFString>?>!) -> Unmanaged<CFPropertyList>!](cfpropertylistcreatefromstream(_:_:_:_:_:_:).md)
  Creates a property list using data from a stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfpropertylistcreatefromxmldata(_:_:_:_:))*