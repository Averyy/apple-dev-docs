# setTemporaryResourceValue(_:forKey:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Sets a temporary resource value on the URL object.

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
func setTemporaryResourceValue(_ value: (any Sendable)?, forKey key: URLResourceKey)
```

```objc
- (void) setTemporaryResourceValue:(id) value forKey:(NSURLResourceKey) key;
```

## Discussion

Your app can use a temporary resource value to temporarily store a value for an app-defined resource value key in memory without modifying the actual resource that the URL represents. Once set, you can copy the temporary resource value from the URL object just as you would copy system-defined keys—by calling [`getResourceValue(_:forKey:)`](./getresourcevalue%28_,forkey%29.md) or [`resourceValues(forKeys:)`](./resourcevalues%28forkeys%29.md).

Your app can remove a temporary resource value from the URL object by calling [`removeCachedResourceValue(forKey:)`](./removecachedresourcevalue%28forkey%29.md) or [`removeAllCachedResourceValues()`](./removeallcachedresourcevalues%28%29.md) (to remove all temporary values).

This method is applicable only to URLs for file system resources.

## Parameters

- `value`: The value to store.
- `key`: The key where the value should be stored. This key must be unique and must not conflict with any system-defined keys. Reverse-domain-name notation is recommended.

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
- [func removeCachedResourceValue(forKey: URLResourceKey)](./removecachedresourcevalue%28forkey%29.md)
  Removes the cached resource value identified by a given key from the URL object.
- [struct URLResourceKey](../urlresourcekey.md)
  Keys that apply to file system URLs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurl/settemporaryresourcevalue(_:forkey:))*