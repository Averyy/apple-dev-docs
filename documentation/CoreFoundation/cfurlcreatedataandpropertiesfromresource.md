# CFURLCreateDataAndPropertiesFromResource(_:_:_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Loads the data and properties referred to by a given URL.

**Availability**:
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CFURLCreateDataAndPropertiesFromResource(_ alloc: CFAllocator!, _ url: CFURL!, _ resourceData: UnsafeMutablePointer<Unmanaged<CFData>?>!, _ properties: UnsafeMutablePointer<Unmanaged<CFDictionary>?>!, _ desiredProperties: CFArray!, _ errorCode: UnsafeMutablePointer<Int32>!) -> Bool
```

#### Return Value

`true` if successful, `false` otherwise.

#### Discussion

If you are interested in loading only the resource data or the resource’s properties, pass `NULL` for the one you don’t want. If `properties` is non-`NULL` and `desiredProperties` is `NULL` then all properties are fetched. Note that as much work as possible is done even if `false` is returned. For instance, if one property is not available, the others are fetched anyway. This function is intended for convenience, not performance.

## Parameters

- `alloc`: The allocator to use to allocate memory for the new `CFData` and `CFDictionary` objects returned in `resourceData` and `properties`. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.
- `url`: The URL referring to the data and/or properties you wish to load.
- `resourceData`: On return, contains a `CFData` object containing the data referred to by `url`. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).
- `properties`: On return, a pointer to a `CFDictionary` object containing the resource properties referred to by `url`. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).
- `desiredProperties`: A list of the properties you wish to obtain and return in `properties`. See [`File URL Properties`](file-url-properties.md) and [`HTTP URL Properties`](http-url-properties.md) for the list of available properties.
- `errorCode`: `0` if successful, otherwise an error code indicating the nature of the problem. See [`CFURLError`](cfurlerror.md) for a list of possible error codes.

## See Also

- [func CFURLCreatePropertyFromResource(CFAllocator!, CFURL!, CFString!, UnsafeMutablePointer<Int32>!) -> CFTypeRef!](cfurlcreatepropertyfromresource(_:_:_:_:).md)
  Returns a given property specified by a given URL and property string.
- [func CFURLDestroyResource(CFURL!, UnsafeMutablePointer<Int32>!) -> Bool](cfurldestroyresource(_:_:).md)
  Destroys a resource indicated by a given URL.
- [func CFURLWriteDataAndPropertiesToResource(CFURL!, CFData!, CFDictionary!, UnsafeMutablePointer<Int32>!) -> Bool](cfurlwritedataandpropertiestoresource(_:_:_:_:).md)
  Writes the given data and properties to a given URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfurlcreatedataandpropertiesfromresource(_:_:_:_:_:_:))*