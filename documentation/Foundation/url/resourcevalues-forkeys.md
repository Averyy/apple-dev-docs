# resourceValues(forKeys:)

**Framework**: Foundation  
**Kind**: method

Returns a collection of resource values identified by the given resource keys.

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
func resourceValues(forKeys keys: Set<URLResourceKey>) throws -> URLResourceValues
```

#### Return Value

A [`URLResourceValues`](urlresourcevalues.md) instance, containing the retrieved values.

#### Discussion

This method first checks if the URL instance already caches the specified resource values. If so, it returns the cached resource values to the caller. If not, then this method synchronously obtains the resource values from the backing store, adds them to the URL object’s cache, and returns a populated [`URLResourceValues`](urlresourcevalues.md) instance. This method only populates [`URLResourceValues`](urlresourcevalues.md) members corresponding to the contents of the `keys` parameter.

The type of the returned resource value varies by resource property; for details, see the documentation for the [`URLResourceKey`](urlresourcekey.md) you want to access.

If there’s no available value for a given key in `keys`, the returned [`URLResourceValues`](urlresourcevalues.md) contains `nil` for the corresponding item. If this method fails to determine a value’s availability or retrieve its value, the method throws an error.

When you call this method from the main thread, the URL removes cached resource values the next time the thread’s run loop runs, except those added as temporary properties. You can explicitly remove cached resource values with [`removeCachedResourceValue(forKey:)`](url/removecachedresourcevalue(forkey:).md) and [`removeAllCachedResourceValues()`](url/removeallcachedresourcevalues().md).

> **Note**:  This method is currently applicable only to URLs for file system resources.

 This method is currently applicable only to URLs for file system resources.

## Parameters

- `keys`: A set of URL resource keys indicating the values to retrieve.

## See Also

- [func setResourceValues(URLResourceValues) throws](url/setresourcevalues(_:).md)
  Sets the resource value identified by a given resource key.
- [func removeCachedResourceValue(forKey: URLResourceKey)](url/removecachedresourcevalue(forkey:).md)
  Removes the cached resource value identified by a given resource value key from the URL object.
- [func removeAllCachedResourceValues()](url/removeallcachedresourcevalues.md)
  Removes all cached resource values and all temporary resource values from the URL object.
- [func setTemporaryResourceValue(any Sendable, forKey: URLResourceKey)](url/settemporaryresourcevalue(_:forkey:).md)
  Sets a temporary resource value on the URL object.
- [struct URLResourceKey](urlresourcekey.md)
  Keys that apply to file system URLs.
- [struct URLResourceValues](urlresourcevalues.md)
  The properties that the file system resources support.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/resourcevalues(forkeys:))*