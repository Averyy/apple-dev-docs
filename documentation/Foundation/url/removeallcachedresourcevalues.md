# removeAllCachedResourceValues()

**Framework**: Foundation  
**Kind**: method

Removes all cached resource values and all temporary resource values from the URL object.

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
mutating func removeAllCachedResourceValues()
```

#### Discussion

This method is currently applicable only to URLs for file system resources.

## See Also

- [func resourceValues(forKeys: Set<URLResourceKey>) throws -> URLResourceValues](url/resourcevalues(forkeys:).md)
  Returns a collection of resource values identified by the given resource keys.
- [func setResourceValues(URLResourceValues) throws](url/setresourcevalues(_:).md)
  Sets the resource value identified by a given resource key.
- [func removeCachedResourceValue(forKey: URLResourceKey)](url/removecachedresourcevalue(forkey:).md)
  Removes the cached resource value identified by a given resource value key from the URL object.
- [func setTemporaryResourceValue(any Sendable, forKey: URLResourceKey)](url/settemporaryresourcevalue(_:forkey:).md)
  Sets a temporary resource value on the URL object.
- [struct URLResourceKey](urlresourcekey.md)
  Keys that apply to file system URLs.
- [struct URLResourceValues](urlresourcevalues.md)
  The properties that the file system resources support.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/removeallcachedresourcevalues())*