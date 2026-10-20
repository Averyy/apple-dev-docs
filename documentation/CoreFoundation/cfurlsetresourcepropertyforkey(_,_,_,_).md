# CFURLSetResourcePropertyForKey(_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Sets the URL’s resource property for a given key to a given value.

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
func CFURLSetResourcePropertyForKey(_ url: CFURL!, _ key: CFString!, _ propertyValue: CFTypeRef!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool
```

```c
extern Boolean CFURLSetResourcePropertyForKey(CFURLRef url, CFStringRef key, CFTypeRef propertyValue, CFErrorRef*error);
```

#### Return Value

`true`  if the resource property named `key` is successfully set to `value`; otherwise, `false`.

#### Discussion

This function synchronously writes the new resource value out to disk. Attempts to set a read-only resource property or to set a resource property that is not supported by the resource are ignored and are not considered errors.

If an error occurs, this method returns `false` and populates the object pointer referenced by `error` with additional information.

> **Note**:  This method applies only to URLs for file system resources.

## Parameters

- `url`: The URL.
- `key`: The name of one of the URL’s resource properties.
- `propertyValue`: The value for the resource property defined by `key`.
- `error`: The error that occurred if the resource value could not be set.

## See Also

### Related Documentation
- [class CFURL](./cfurl.md)
### Getting and Setting File System Resource Properties
- [func CFURLClearResourcePropertyCache(CFURL!)](./cfurlclearresourcepropertycache%28_%29.md)
  Removes all cached resource values and temporary resource values from the URL object.
- [func CFURLClearResourcePropertyCacheForKey(CFURL!, CFString!)](./cfurlclearresourcepropertycacheforkey%28_,_%29.md)
  Removes the cached resource value identified by a given key from the URL object.
- [func CFURLCopyResourcePropertiesForKeys(CFURL!, CFArray!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFDictionary>!](./cfurlcopyresourcepropertiesforkeys%28_,_,_%29.md)
  Returns the resource values for the properties identified by specified array of keys.
- [func CFURLCopyResourcePropertyForKey(CFURL!, CFString!, UnsafeMutableRawPointer!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./cfurlcopyresourcepropertyforkey%28_,_,_,_%29.md)
  Returns the value of a given resource property of a given URL.
- [func CFURLCreateResourcePropertiesForKeysFromBookmarkData(CFAllocator!, CFArray!, CFData!) -> Unmanaged<CFDictionary>!](./cfurlcreateresourcepropertiesforkeysfrombookmarkdata%28_,_,_%29.md)
  Returns the resource values for properties identified by a specified array of keys contained in specified bookmark data.
- [func CFURLCreateResourcePropertyForKeyFromBookmarkData(CFAllocator!, CFString!, CFData!) -> Unmanaged<CFTypeRef>!](./cfurlcreateresourcepropertyforkeyfrombookmarkdata%28_,_,_%29.md)
  Returns the value of a resource property from specified bookmark data.
- [func CFURLSetResourcePropertiesForKeys(CFURL!, CFDictionary!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./cfurlsetresourcepropertiesforkeys%28_,_,_%29.md)
  Sets the URL’s resource properties for a given set of keys to a given set of values.
- [func CFURLSetTemporaryResourcePropertyForKey(CFURL!, CFString!, CFTypeRef!)](./cfurlsettemporaryresourcepropertyforkey%28_,_,_%29.md)
  Sets a temporary resource value on the URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfurlsetresourcepropertyforkey(_:_:_:_:))*