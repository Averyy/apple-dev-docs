# CFPropertyListCreateFromXMLData(_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Creates a property list using the specified XML or binary property list data.

**Availability**:
- iOS 2.0+ - Deprecated in 8.0
- iPadOS 2.0+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.10
- tvOS 9.0+ - Deprecated in 9.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: Use CFPropertyListCreateWithData instead.

## Declaration

```swift
func CFPropertyListCreateFromXMLData(_ allocator: CFAllocator!, _ xmlData: CFData!, _ mutabilityOption: CFOptionFlags, _ errorString: UnsafeMutablePointer<Unmanaged<CFString>?>!) -> Unmanaged<CFPropertyList>!
```

```c
extern CFPropertyListRefCFPropertyListCreateFromXMLData(CFAllocatorRef allocator, CFDataRef xmlData, CFOptionFlags mutabilityOption, CFStringRef*errorString);
```

## Return Value

A new property list if the conversion is successful, otherwise `NULL`. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

> ⚠️ **Warning**:  This function is obsolete and will be deprecated soon. Use [`CFPropertyListCreateWithData(_:_:_:_:_:)`](./cfpropertylistcreatewithdata%28_,_,_,_,_%29.md) instead.

## Parameters

- `allocator`: The allocator to use to allocate memory for the new property list. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.
- `xmlData`: The raw bytes to convert into a property list. The bytes may be the content of an XML file or of a binary property list (see [`CFPropertyListFormat`](./cfpropertylistformat.md)).
- `mutabilityOption`: A constant that specifies the degree of mutability for the returned property list. See [Property List Mutability Options](./property_list_mutability_options.md) for descriptions of possible values.
- `errorString`: On return, `NULL` if the conversion is successful, otherwise a string that describes the nature of the error. Error messages are not localized, but may be in the future, so they are not currently suitable for comparison.

  Pass `NULL` if you do not wish to receive an error string. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

### Creating a Property List
- [func CFPropertyListCreateWithData(CFAllocator!, CFData!, CFOptionFlags, UnsafeMutablePointer<CFPropertyListFormat>!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFPropertyList>!](./cfpropertylistcreatewithdata%28_,_,_,_,_%29.md)
  Creates a property list from a given CFData object.
- [func CFPropertyListCreateWithStream(CFAllocator!, CFReadStream!, CFIndex, CFOptionFlags, UnsafeMutablePointer<CFPropertyListFormat>!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFPropertyList>!](./cfpropertylistcreatewithstream%28_,_,_,_,_,_%29.md)
  Create and return a property list with a CFReadStream input.
- [func CFPropertyListCreateDeepCopy(CFAllocator!, CFPropertyList!, CFOptionFlags) -> CFPropertyList!](./cfpropertylistcreatedeepcopy%28_,_,_%29.md)
  Recursively creates a copy of a given property list.
- [func CFPropertyListCreateFromStream(CFAllocator!, CFReadStream!, CFIndex, CFOptionFlags, UnsafeMutablePointer<CFPropertyListFormat>!, UnsafeMutablePointer<Unmanaged<CFString>?>!) -> Unmanaged<CFPropertyList>!](./cfpropertylistcreatefromstream%28_,_,_,_,_,_%29.md)
  Creates a property list using data from a stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfpropertylistcreatefromxmldata(_:_:_:_:))*