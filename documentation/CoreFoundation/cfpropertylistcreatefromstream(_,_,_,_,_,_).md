# CFPropertyListCreateFromStream(_:_:_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Creates a property list using data from a stream.

**Availability**:
- iOS 2.0+ - Deprecated in 8.0
- iPadOS 2.0+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.2+ - Deprecated in 10.10
- tvOS 9.0+ - Deprecated in 9.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: Use CFPropertyListCreateWithStream instead.

## Declaration

```swift
func CFPropertyListCreateFromStream(_ allocator: CFAllocator!, _ stream: CFReadStream!, _ streamLength: CFIndex, _ mutabilityOption: CFOptionFlags, _ format: UnsafeMutablePointer<CFPropertyListFormat>!, _ errorString: UnsafeMutablePointer<Unmanaged<CFString>?>!) -> Unmanaged<CFPropertyList>!
```

```c
extern CFPropertyListRefCFPropertyListCreateFromStream(CFAllocatorRef allocator, CFReadStreamRef stream, CFIndex streamLength, CFOptionFlags mutabilityOption, CFPropertyListFormat *format, CFStringRef*errorString);
```

#### Return Value

A new property list initialized with the data contained in `stream`. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

#### Discussion

This function simply reads bytes from `stream` starting at the current location to the end, which is expected to be the end of the property list, or up to the number of bytes specified by `streamLength` if it is not `0`.

##### Special Considerations

> ⚠️ **Warning**:  This function is obsolete and will be deprecated soon. Use [`CFPropertyListCreateWithStream(_:_:_:_:_:_:)`](./cfpropertylistcreatewithstream%28_,_,_,_,_,_%29.md) instead.

## Parameters

- `allocator`: The allocator to use to allocate memory for the new property list. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.
- `stream`: The stream whose data contains the content. The stream must be opened and configured—this function simply reads bytes from the stream. The stream may contain any supported property list type (see [`CFPropertyListFormat`](./cfpropertylistformat.md)).
- `streamLength`: The number of bytes to read. If `0`, this function will read to the end of the stream.
- `mutabilityOption`: A constant that specifies the degree of mutability for the returned property list. See [Property List Mutability Options](./property_list_mutability_options.md) for descriptions of possible values.
- `format`: A constant that specifies the format of the property list. See [`CFPropertyListFormat`](./cfpropertylistformat.md) for possible values.
- `errorString`: On return, `NULL` if the conversion is successful, otherwise a string that describes the nature of the error. Error messages are not localized, but may be in the future, so they are not suitable for comparison.

  Pass `NULL` if you do not wish to receive an error string. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

### Creating a Property List
- [func CFPropertyListCreateWithData(CFAllocator!, CFData!, CFOptionFlags, UnsafeMutablePointer<CFPropertyListFormat>!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFPropertyList>!](./cfpropertylistcreatewithdata%28_,_,_,_,_%29.md)
  Creates a property list from a given CFData object.
- [func CFPropertyListCreateWithStream(CFAllocator!, CFReadStream!, CFIndex, CFOptionFlags, UnsafeMutablePointer<CFPropertyListFormat>!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFPropertyList>!](./cfpropertylistcreatewithstream%28_,_,_,_,_,_%29.md)
  Create and return a property list with a CFReadStream input.
- [func CFPropertyListCreateDeepCopy(CFAllocator!, CFPropertyList!, CFOptionFlags) -> CFPropertyList!](./cfpropertylistcreatedeepcopy%28_,_,_%29.md)
  Recursively creates a copy of a given property list.
- [func CFPropertyListCreateFromXMLData(CFAllocator!, CFData!, CFOptionFlags, UnsafeMutablePointer<Unmanaged<CFString>?>!) -> Unmanaged<CFPropertyList>!](./cfpropertylistcreatefromxmldata%28_,_,_,_%29.md)
  Creates a property list using the specified XML or binary property list data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfpropertylistcreatefromstream(_:_:_:_:_:_:))*