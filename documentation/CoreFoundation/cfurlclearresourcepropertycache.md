# CFURLClearResourcePropertyCache(_:)

**Framework**: Core Foundation  
**Kind**: func

Removes all cached resource values and temporary resource values from the URL object.

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
func CFURLClearResourcePropertyCache(_ url: CFURL!)
```

#### Discussion

This method is applicable only to URLs that represent file system resources.

> **Note**:  The caching behavior of the `NSURL` and `CFURL` APIs differ. For `NSURL`, all cached values (not temporary values) are automatically removed after each pass through the run loop. You only need to call the [`CFURL`](cfurl.md) method when you want to clear the cache within a single execution of the run loop. The `CFURL` functions, on the other hand, do not automatically clear cached resource values. The client has complete control over the cache lifetimes, and you must use [`CFURLClearResourcePropertyCacheForKey(_:_:)`](cfurlclearresourcepropertycacheforkey(_:_:).md) or [`CFURLClearResourcePropertyCache(_:)`](cfurlclearresourcepropertycache(_:).md) to clear cached resource values.

## Parameters

- `url`: The URL.

## See Also

- [func CFURLClearResourcePropertyCacheForKey(CFURL!, CFString!)](cfurlclearresourcepropertycacheforkey(_:_:).md)
  Removes the cached resource value identified by a given key from the URL object.
- [func CFURLCopyResourcePropertiesForKeys(CFURL!, CFArray!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFDictionary>!](cfurlcopyresourcepropertiesforkeys(_:_:_:).md)
  Returns the resource values for the properties identified by specified array of keys.
- [func CFURLCopyResourcePropertyForKey(CFURL!, CFString!, UnsafeMutableRawPointer!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](cfurlcopyresourcepropertyforkey(_:_:_:_:).md)
  Returns the value of a given resource property of a given URL.
- [func CFURLCreateResourcePropertiesForKeysFromBookmarkData(CFAllocator!, CFArray!, CFData!) -> Unmanaged<CFDictionary>!](cfurlcreateresourcepropertiesforkeysfrombookmarkdata(_:_:_:).md)
  Returns the resource values for properties identified by a specified array of keys contained in specified bookmark data.
- [func CFURLCreateResourcePropertyForKeyFromBookmarkData(CFAllocator!, CFString!, CFData!) -> Unmanaged<CFTypeRef>!](cfurlcreateresourcepropertyforkeyfrombookmarkdata(_:_:_:).md)
  Returns the value of a resource property from specified bookmark data.
- [func CFURLSetResourcePropertiesForKeys(CFURL!, CFDictionary!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](cfurlsetresourcepropertiesforkeys(_:_:_:).md)
  Sets the URL’s resource properties for a given set of keys to a given set of values.
- [func CFURLSetResourcePropertyForKey(CFURL!, CFString!, CFTypeRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](cfurlsetresourcepropertyforkey(_:_:_:_:).md)
  Sets the URL’s resource property for a given key to a given value.
- [func CFURLSetTemporaryResourcePropertyForKey(CFURL!, CFString!, CFTypeRef!)](cfurlsettemporaryresourcepropertyforkey(_:_:_:).md)
  Sets a temporary resource value on the URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfurlclearresourcepropertycache(_:))*