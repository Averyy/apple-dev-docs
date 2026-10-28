# removeCachedResourceValue(forKey:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Removes the cached resource value identified by a given resource value key from the URL object.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
mutating func removeCachedResourceValue(forKey key: URLResourceKey)
```

## Discussion

Removing a cached resource value may remove other cached resource values because some resource values are cached as a set of values, and because some resource values depend on other resource values (temporary resource values have no dependencies). This method is currently applicable only to URLs for file system resources.

## See Also

### Accessing resource values
- [func resourceValues(forKeys: Set<URLResourceKey>) throws -> URLResourceValues](./resourcevalues%28forkeys%29.md)
  Returns a collection of resource values identified by the given resource keys.
- [func setResourceValues(URLResourceValues) throws](./setresourcevalues%28_%29.md)
  Sets the resource value identified by a given resource key.
- [func removeAllCachedResourceValues()](./removeallcachedresourcevalues%28%29.md)
  Removes all cached resource values and all temporary resource values from the URL object.
- [func setTemporaryResourceValue(any Sendable, forKey: URLResourceKey)](./settemporaryresourcevalue%28_,forkey%29.md)
  Sets a temporary resource value on the URL object.
- [struct URLResourceKey](../urlresourcekey.md)
  Keys that apply to file system URLs.
- [struct URLResourceValues](../urlresourcevalues.md)
  The properties that the file system resources support.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/removecachedresourcevalue(forkey:))*