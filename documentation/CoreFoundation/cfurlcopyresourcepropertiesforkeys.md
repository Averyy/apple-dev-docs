# CFURLCopyResourcePropertiesForKeys(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Returns the resource values for the properties identified by specified array of keys.

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
func CFURLCopyResourcePropertiesForKeys(_ url: CFURL!, _ keys: CFArray!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFDictionary>!
```

#### Return Value

A dictionary of resource values indexed by key, or `NULL` if an error occurs.

#### Discussion

This function first checks if the URL object already caches the specified resource values. If so, it returns the cached resource values to the caller. If not, then this function synchronously obtains the resource values from the backing store, adds the resource values to the URL object’s cache, and returns the resource values to the caller.

The type of the returned resource value varies by resource property; for details, see the documentation for the key you want to access.

If the result dictionary does not contain a resource value for one or more of the requested resource keys, it means those resource properties are not available for the specified URL, and no errors occurred when determining those resource properties were not available.

If an error occurs, this function returns `NULL` and populates the object pointer referenced by `error` with additional information.

> **Note**:  This method applies only to URLs that represent file system resources.

 This method applies only to URLs that represent file system resources.

## Parameters

- `url`: The URL.
- `keys`: An array of property keys for the desired resource properties.
- `error`: The error that occurred if one or more resource values could not be retrieved.  This parameter is optional. If you are not interested in receiving error information, you can pass  .

## See Also

- [class CFURL](cfurl.md)
- [func CFURLClearResourcePropertyCache(CFURL!)](cfurlclearresourcepropertycache(_:).md)
  Removes all cached resource values and temporary resource values from the URL object.
- [func CFURLClearResourcePropertyCacheForKey(CFURL!, CFString!)](cfurlclearresourcepropertycacheforkey(_:_:).md)
  Removes the cached resource value identified by a given key from the URL object.
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

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfurlcopyresourcepropertiesforkeys(_:_:_:))*