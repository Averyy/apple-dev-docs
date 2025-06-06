# CFURLCreatePropertyFromResource(_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Returns a given property specified by a given URL and property string.

**Availability**:
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CFURLCreatePropertyFromResource(_ alloc: CFAllocator!, _ url: CFURL!, _ property: CFString!, _ errorCode: UnsafeMutablePointer<Int32>!) -> CFTypeRef!
```

#### Return Value

If successful, the requested property as a `CFType` object, `NULL` otherwise. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

#### Discussion

This is a convenience function for retrieving individual property values which calls through to [`CFURLCreateDataAndPropertiesFromResource(_:_:_:_:_:_:)`](cfurlcreatedataandpropertiesfromresource(_:_:_:_:_:_:).md).

## Parameters

- `alloc`: The allocator to use to to allocate memory for the new   object for the requested property. Pass   or kCFAllocatorDefault to use the current default allocator.
- `url`: The   object referring to the resource whose properties are loaded.
- `property`: The name of the property you wish to load. Pass one of the provided string constants indicating the property. See   and   for the list of available properties.
- `errorCode`: On return,   if successful, otherwise an error code indicating the nature of the problem. See   for a list of possible error codes.

## See Also

- [func CFURLCreateDataAndPropertiesFromResource(CFAllocator!, CFURL!, UnsafeMutablePointer<Unmanaged<CFData>?>!, UnsafeMutablePointer<Unmanaged<CFDictionary>?>!, CFArray!, UnsafeMutablePointer<Int32>!) -> Bool](cfurlcreatedataandpropertiesfromresource(_:_:_:_:_:_:).md)
  Loads the data and properties referred to by a given URL.
- [func CFURLDestroyResource(CFURL!, UnsafeMutablePointer<Int32>!) -> Bool](cfurldestroyresource(_:_:).md)
  Destroys a resource indicated by a given URL.
- [func CFURLWriteDataAndPropertiesToResource(CFURL!, CFData!, CFDictionary!, UnsafeMutablePointer<Int32>!) -> Bool](cfurlwritedataandpropertiestoresource(_:_:_:_:).md)
  Writes the given data and properties to a given URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfurlcreatepropertyfromresource(_:_:_:_:))*