# CFURLCopyResourcePropertyForKey(_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns the value of a given resource property of a given URL.

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
func CFURLCopyResourcePropertyForKey(_ url: CFURL!, _ key: CFString!, _ propertyValueTypeRefPtr: UnsafeMutableRawPointer!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool
```

```c
extern Boolean CFURLCopyResourcePropertyForKey(CFURLRef url, CFStringRef key, void *propertyValueTypeRefPtr, CFErrorRef*error);
```

#### Return Value

`true` if `propertyValueTypeRefPtr` is successfully populated; otherwise, `false`.

#### Discussion

This function first checks if the URL object already caches the resource value. If so, it returns the cached resource value to the caller. If not, then this function synchronously obtains the resource value from the backing store, adds the resource value to the URL object’s cache, and returns the resource value to the caller.

The type of the returned resource value varies by resource property; for details, see the documentation for the key you want to access.

If this function returns [`true`](../Swift/true.md) and the propertyValueTypeRefPtr is populated with `nil`, it means that the resource property is not available for the specified resource, and that no errors occurred when determining that the resource property was unavailable.

If this function returns [`false`](../Swift/false.md), an error occurred. the object pointer referenced by `error` is populated with additional information.

> **Note**:  This method applies only to URLs that represent file system resources.

## Parameters

- `url`: The URL.
- `key`: The property value key for the requested value.
- `propertyValueTypeRefPtr`: The output pointer that is populated with the result.
- `error`: The error that occurred if the property’s value could not be obtained. This parameter is optional. If you are not interested in receiving error information, you can pass `NULL`.

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
- [func CFURLCreateResourcePropertiesForKeysFromBookmarkData(CFAllocator!, CFArray!, CFData!) -> Unmanaged<CFDictionary>!](./cfurlcreateresourcepropertiesforkeysfrombookmarkdata%28_,_,_%29.md)
  Returns the resource values for properties identified by a specified array of keys contained in specified bookmark data.
- [func CFURLCreateResourcePropertyForKeyFromBookmarkData(CFAllocator!, CFString!, CFData!) -> Unmanaged<CFTypeRef>!](./cfurlcreateresourcepropertyforkeyfrombookmarkdata%28_,_,_%29.md)
  Returns the value of a resource property from specified bookmark data.
- [func CFURLSetResourcePropertiesForKeys(CFURL!, CFDictionary!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./cfurlsetresourcepropertiesforkeys%28_,_,_%29.md)
  Sets the URL’s resource properties for a given set of keys to a given set of values.
- [func CFURLSetResourcePropertyForKey(CFURL!, CFString!, CFTypeRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./cfurlsetresourcepropertyforkey%28_,_,_,_%29.md)
  Sets the URL’s resource property for a given key to a given value.
- [func CFURLSetTemporaryResourcePropertyForKey(CFURL!, CFString!, CFTypeRef!)](./cfurlsettemporaryresourcepropertyforkey%28_,_,_%29.md)
  Sets a temporary resource value on the URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfurlcopyresourcepropertyforkey(_:_:_:_:))*