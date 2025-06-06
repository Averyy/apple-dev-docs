# CFPropertyListCreateDeepCopy(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Recursively creates a copy of a given property list.

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
func CFPropertyListCreateDeepCopy(_ allocator: CFAllocator!, _ propertyList: CFPropertyList!, _ mutabilityOption: CFOptionFlags) -> CFPropertyList!
```

#### Return Value

A new property list that is a copy of `propertyList`. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

#### Discussion

Recursively creates a copy of the given property list so nested arrays and dictionaries are copied as well as the top-most container.

## Parameters

- `allocator`: The allocator to use to allocate memory for the new property list. Pass   or kCFAllocatorDefault to use the current default allocator.
- `propertyList`: The property list to copy. This may be any of the standard property list objects, for example a CFArray or a CFDictionary object.
- `mutabilityOption`: A constant that specifies the degree of mutability of the returned property list. See   for descriptions of possible values.

## See Also

- [func CFPropertyListCreateWithData(CFAllocator!, CFData!, CFOptionFlags, UnsafeMutablePointer<CFPropertyListFormat>!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFPropertyList>!](cfpropertylistcreatewithdata(_:_:_:_:_:).md)
  Creates a property list from a given CFData object.
- [func CFPropertyListCreateWithStream(CFAllocator!, CFReadStream!, CFIndex, CFOptionFlags, UnsafeMutablePointer<CFPropertyListFormat>!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFPropertyList>!](cfpropertylistcreatewithstream(_:_:_:_:_:_:).md)
  Create and return a property list with a CFReadStream input.
- [func CFPropertyListCreateFromXMLData(CFAllocator!, CFData!, CFOptionFlags, UnsafeMutablePointer<Unmanaged<CFString>?>!) -> Unmanaged<CFPropertyList>!](cfpropertylistcreatefromxmldata(_:_:_:_:).md)
  Creates a property list using the specified XML or binary property list data.
- [func CFPropertyListCreateFromStream(CFAllocator!, CFReadStream!, CFIndex, CFOptionFlags, UnsafeMutablePointer<CFPropertyListFormat>!, UnsafeMutablePointer<Unmanaged<CFString>?>!) -> Unmanaged<CFPropertyList>!](cfpropertylistcreatefromstream(_:_:_:_:_:_:).md)
  Creates a property list using data from a stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfpropertylistcreatedeepcopy(_:_:_:))*