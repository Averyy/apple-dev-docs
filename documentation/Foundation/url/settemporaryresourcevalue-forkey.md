# setTemporaryResourceValue(_:forKey:)

**Framework**: Foundation  
**Kind**: method

Sets a temporary resource value on the URL object.

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
@preconcurrency
mutating func setTemporaryResourceValue(_ value: any Sendable, forKey key: URLResourceKey)
```

#### Discussion

Temporary resource values are for client use. Temporary resource values exist only in memory and are never written to the resource’s backing store. Once set, a temporary resource value can be copied from the URL object with `func resourceValues(forKeys:)`. The values are stored in the loosely-typed `allValues` dictionary property.

To remove a temporary resource value from the URL object, use `func removeCachedResourceValue(forKey:)`. Care should be taken to ensure the key that identifies a temporary resource value is unique and does not conflict with system defined keys (using reverse domain name notation in your temporary resource value keys is recommended). This method is currently applicable only to URLs for file system resources.

## See Also

- [func resourceValues(forKeys: Set<URLResourceKey>) throws -> URLResourceValues](url/resourcevalues(forkeys:).md)
  Returns a collection of resource values identified by the given resource keys.
- [func setResourceValues(URLResourceValues) throws](url/setresourcevalues(_:).md)
  Sets the resource value identified by a given resource key.
- [func removeCachedResourceValue(forKey: URLResourceKey)](url/removecachedresourcevalue(forkey:).md)
  Removes the cached resource value identified by a given resource value key from the URL object.
- [func removeAllCachedResourceValues()](url/removeallcachedresourcevalues.md)
  Removes all cached resource values and all temporary resource values from the URL object.
- [struct URLResourceKey](urlresourcekey.md)
  Keys that apply to file system URLs.
- [struct URLResourceValues](urlresourcevalues.md)
  The properties that the file system resources support.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/settemporaryresourcevalue(_:forkey:))*