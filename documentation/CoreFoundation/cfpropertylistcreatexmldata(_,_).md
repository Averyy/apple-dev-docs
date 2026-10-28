# CFPropertyListCreateXMLData(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Creates an XML representation of the specified property list.

**Availability**:
- iOS 2.0+ - Deprecated in 8.0
- iPadOS 2.0+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.10
- tvOS 9.0+ - Deprecated in 9.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: Use CFPropertyListCreateData instead.

## Declaration

```swift
func CFPropertyListCreateXMLData(_ allocator: CFAllocator!, _ propertyList: CFPropertyList!) -> Unmanaged<CFData>!
```

```c
extern CFDataRefCFPropertyListCreateXMLData(CFAllocatorRef allocator, CFPropertyListRef propertyList);
```

## Return Value

A CFData object containing the XML data. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

> ⚠️ **Warning**:  This function is obsolete and will be deprecated soon. Use [`CFPropertyListCreateData(_:_:_:_:_:)`](./cfpropertylistcreatedata%28_,_,_,_,_%29.md) instead.

## Parameters

- `allocator`: The allocator to use to allocate memory for the new data object. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.
- `propertyList`: The property list to convert. This may be any of the standard property list objects, for example a CFArray or a CFDictionary object.

## See Also

### Exporting a Property List
- [func CFPropertyListCreateData(CFAllocator!, CFPropertyList!, CFPropertyListFormat, CFOptionFlags, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFData>!](./cfpropertylistcreatedata%28_,_,_,_,_%29.md)
  Returns a CFData object containing a serialized representation of a given property list in a specified format.
- [func CFPropertyListWrite(CFPropertyList!, CFWriteStream!, CFPropertyListFormat, CFOptionFlags, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> CFIndex](./cfpropertylistwrite%28_,_,_,_,_%29.md)
  Write the bytes of a serialized property list out to a stream.
- [func CFPropertyListWriteToStream(CFPropertyList!, CFWriteStream!, CFPropertyListFormat, UnsafeMutablePointer<Unmanaged<CFString>?>!) -> CFIndex](./cfpropertylistwritetostream%28_,_,_,_%29.md)
  Writes the bytes of a property list serialization out to a stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfpropertylistcreatexmldata(_:_:))*