# removeCachedResourceValue(forKey:)

**Framework**: Foundation  
**Kind**: method

Removes the cached resource value identified by a given key from the URL object.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func removeCachedResourceValue(forKey key: URLResourceKey)
```

#### Discussion

Removing a cached resource value may remove other cached resource values because some resource values are cached as a set of values, and because some resource values depend on other resource values. (Temporary resource values have no dependencies.)

This method is currently applicable only to URLs for file system resources.

> **Note**:  The caching behavior of the `NSURL` and `CFURL` APIs differ. For `NSURL`, all cached values (not temporary values) are automatically removed after each pass through the run loop. You only need to call the [`removeCachedResourceValue(forKey:)`](nsurl/removecachedresourcevalue(forkey:).md) method when you want to clear the cache within a single execution of the run loop. The `CFURL` functions, on the other hand, do not automatically clear cached resource values. The client has complete control over the cache lifetimes, and you must use [`CFURLClearResourcePropertyCacheForKey(_:_:)`](https://developer.apple.com/documentation/CoreFoundation/CFURLClearResourcePropertyCacheForKey(_:_:)) or [`CFURLClearResourcePropertyCache(_:)`](https://developer.apple.com/documentation/CoreFoundation/CFURLClearResourcePropertyCache(_:)) to clear cached resource values.

 The caching behavior of the `NSURL` and `CFURL` APIs differ. For `NSURL`, all cached values (not temporary values) are automatically removed after each pass through the run loop. You only need to call the [`removeCachedResourceValue(forKey:)`](nsurl/removecachedresourcevalue(forkey:).md) method when you want to clear the cache within a single execution of the run loop. The `CFURL` functions, on the other hand, do not automatically clear cached resource values. The client has complete control over the cache lifetimes, and you must use [`CFURLClearResourcePropertyCacheForKey(_:_:)`](https://developer.apple.com/documentation/CoreFoundation/CFURLClearResourcePropertyCacheForKey(_:_:)) or [`CFURLClearResourcePropertyCache(_:)`](https://developer.apple.com/documentation/CoreFoundation/CFURLClearResourcePropertyCache(_:)) to clear cached resource values.

## Parameters

- `key`: The resource value key whose cached values you want to remove.

## See Also

- [func resourceValues(forKeys: [URLResourceKey]) throws -> [URLResourceKey : Any]](nsurl/resourcevalues(forkeys:).md)
  Returns the resource values for the properties identified by specified array of keys.
- [func getResourceValue(AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey: URLResourceKey) throws](nsurl/getresourcevalue(_:forkey:).md)
  Returns the value of the resource property for the specified key.
- [func setResourceValue(Any?, forKey: URLResourceKey) throws](nsurl/setresourcevalue(_:forkey:).md)
  Sets the URL’s resource property for a given key to a given value.
- [func setResourceValues([URLResourceKey : Any]) throws](nsurl/setresourcevalues(_:).md)
  Sets the URL’s resource properties for a given set of keys to a given set of values.
- [func removeAllCachedResourceValues()](nsurl/removeallcachedresourcevalues.md)
  Removes all cached resource values and temporary resource values from the URL object.
- [func setTemporaryResourceValue((any Sendable)?, forKey: URLResourceKey)](nsurl/settemporaryresourcevalue(_:forkey:).md)
  Sets a temporary resource value on the URL object.
- [struct URLResourceKey](urlresourcekey.md)
  Keys that apply to file system URLs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurl/removecachedresourcevalue(forkey:))*