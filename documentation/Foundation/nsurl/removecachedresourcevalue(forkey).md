# removeCachedResourceValue(forKey:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) removeCachedResourceValueForKey:(NSURLResourceKey) key;
```

#### Discussion

Removing a cached resource value may remove other cached resource values because some resource values are cached as a set of values, and because some resource values depend on other resource values. (Temporary resource values have no dependencies.)

This method is currently applicable only to URLs for file system resources.

> **Note**:  The caching behavior of the `NSURL` and `CFURL` APIs differ. For `NSURL`, all cached values (not temporary values) are automatically removed after each pass through the run loop. You only need to call the [`removeCachedResourceValue(forKey:)`](./removecachedresourcevalue%28forkey%29.md) method when you want to clear the cache within a single execution of the run loop. The `CFURL` functions, on the other hand, do not automatically clear cached resource values. The client has complete control over the cache lifetimes, and you must use [`CFURLClearResourcePropertyCacheForKey(_:_:)`](../../CoreFoundation/cfurlclearresourcepropertycacheforkey%28_,_%29.md) or [`CFURLClearResourcePropertyCache(_:)`](../../CoreFoundation/cfurlclearresourcepropertycache%28_%29.md) to clear cached resource values.

## Parameters

- `key`: The resource value key whose cached values you want to remove.

## See Also

### Accessing Resource Values
- [func resourceValues(forKeys: [URLResourceKey]) throws -> [URLResourceKey : Any]](./resourcevalues%28forkeys%29.md)
  Returns the resource values for the properties identified by specified array of keys.
- [func getResourceValue(AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey: URLResourceKey) throws](./getresourcevalue%28_,forkey%29.md)
  Returns the value of the resource property for the specified key.
- [func setResourceValue(Any?, forKey: URLResourceKey) throws](./setresourcevalue%28_,forkey%29.md)
  Sets the URL’s resource property for a given key to a given value.
- [func setResourceValues([URLResourceKey : Any]) throws](./setresourcevalues%28_%29.md)
  Sets the URL’s resource properties for a given set of keys to a given set of values.
- [func removeAllCachedResourceValues()](./removeallcachedresourcevalues%28%29.md)
  Removes all cached resource values and temporary resource values from the URL object.
- [func setTemporaryResourceValue((any Sendable)?, forKey: URLResourceKey)](./settemporaryresourcevalue%28_,forkey%29.md)
  Sets a temporary resource value on the URL object.
- [struct URLResourceKey](../urlresourcekey.md)
  Keys that apply to file system URLs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurl/removecachedresourcevalue(forkey:))*