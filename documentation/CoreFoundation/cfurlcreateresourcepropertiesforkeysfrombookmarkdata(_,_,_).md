# CFURLCreateResourcePropertiesForKeysFromBookmarkData(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns the resource values for properties identified by a specified array of keys contained in specified bookmark data.

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
func CFURLCreateResourcePropertiesForKeysFromBookmarkData(_ allocator: CFAllocator!, _ resourcePropertiesToReturn: CFArray!, _ bookmark: CFData!) -> Unmanaged<CFDictionary>!
```

```c
extern CFDictionaryRefCFURLCreateResourcePropertiesForKeysFromBookmarkData(CFAllocatorRef allocator, CFArrayRef resourcePropertiesToReturn, CFDataRef bookmark);
```

## Return Value

A dictionary of the requested resource values contained in `bookmarkData`.

## Discussion

This function does not attempt to resolve the bookmark data or perform I/O.

## Parameters

- `allocator`: The allocator to use to allocate memory for the new `CFURL` object. Pass `NULL` or [`kCFAllocatorDefault`](./kcfallocatordefault.md) to use the current default allocator.
- `resourcePropertiesToReturn`: An array of names of URL resource properties. See [Common File System Resource Keys](./common-file-system-resource-keys.md) for a list of possible keys.
- `bookmark`: The bookmark data the resource values are derived from.

## See Also

### Getting and Setting File System Resource Properties
- [func CFURLClearResourcePropertyCache(CFURL!)](./cfurlclearresourcepropertycache%28_%29.md)
  Removes all cached resource values and temporary resource values from the URL object.
- [func CFURLClearResourcePropertyCacheForKey(CFURL!, CFString!)](./cfurlclearresourcepropertycacheforkey%28_,_%29.md)
  Removes the cached resource value identified by a given key from the URL object.
- [func CFURLCopyResourcePropertiesForKeys(CFURL!, CFArray!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFDictionary>!](./cfurlcopyresourcepropertiesforkeys%28_,_,_%29.md)
  Returns the resource values for the properties identified by specified array of keys.
- [func CFURLCopyResourcePropertyForKey(CFURL!, CFString!, UnsafeMutableRawPointer!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./cfurlcopyresourcepropertyforkey%28_,_,_,_%29.md)
  Returns the value of a given resource property of a given URL.
- [func CFURLCreateResourcePropertyForKeyFromBookmarkData(CFAllocator!, CFString!, CFData!) -> Unmanaged<CFTypeRef>!](./cfurlcreateresourcepropertyforkeyfrombookmarkdata%28_,_,_%29.md)
  Returns the value of a resource property from specified bookmark data.
- [func CFURLSetResourcePropertiesForKeys(CFURL!, CFDictionary!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./cfurlsetresourcepropertiesforkeys%28_,_,_%29.md)
  Sets the URL’s resource properties for a given set of keys to a given set of values.
- [func CFURLSetResourcePropertyForKey(CFURL!, CFString!, CFTypeRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./cfurlsetresourcepropertyforkey%28_,_,_,_%29.md)
  Sets the URL’s resource property for a given key to a given value.
- [func CFURLSetTemporaryResourcePropertyForKey(CFURL!, CFString!, CFTypeRef!)](./cfurlsettemporaryresourcepropertyforkey%28_,_,_%29.md)
  Sets a temporary resource value on the URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfurlcreateresourcepropertiesforkeysfrombookmarkdata(_:_:_:))*