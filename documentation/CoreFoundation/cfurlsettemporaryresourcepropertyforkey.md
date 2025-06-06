# CFURLSetTemporaryResourcePropertyForKey(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Sets a temporary resource value on the URL.

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
func CFURLSetTemporaryResourcePropertyForKey(_ url: CFURL!, _ key: CFString!, _ propertyValue: CFTypeRef!)
```

#### Discussion

Your app can use a temporary resource value to temporarily store a value for an app-defined resource value key in memory without modifying the actual resource that the URL represents. Once set, you can copy the temporary resource value from the URL object just as you would copy system-defined keys—by calling [`CFURLCopyResourcePropertyForKey(_:_:_:_:)`](cfurlcopyresourcepropertyforkey(_:_:_:_:).md) or [`CFURLCopyResourcePropertiesForKeys(_:_:_:)`](cfurlcopyresourcepropertiesforkeys(_:_:_:).md).

Your app can remove a temporary resource value from the URL object by calling [`CFURLClearResourcePropertyCacheForKey(_:_:)`](cfurlclearresourcepropertycacheforkey(_:_:).md) or [`CFURLClearResourcePropertyCache(_:)`](cfurlclearresourcepropertycache(_:).md) (to remove all temporary values).

This method is applicable only to URLs for file system resources.

## Parameters

- `url`: The URL.
- `key`: The key where the value should be stored. This key must be unique and must not conflict with any system-defined keys. Reverse-domain-name notation is recommended.
- `propertyValue`: The value to store.

## See Also

- [func CFURLClearResourcePropertyCache(CFURL!)](cfurlclearresourcepropertycache(_:).md)
  Removes all cached resource values and temporary resource values from the URL object.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfurlsettemporaryresourcepropertyforkey(_:_:_:))*