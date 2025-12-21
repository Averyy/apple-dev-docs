# getResourceValue(_:forKey:)

**Framework**: Foundation  
**Kind**: method

Returns the value of the resource property for the specified key.

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
func getResourceValue(_ value: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey key: URLResourceKey) throws
```

#### Discussion

This method first checks if the URL object already caches the resource value. If so, it returns the cached resource value to the caller. If not, then this method synchronously obtains the resource value from the backing store, adds the resource value to the URL object’s cache, and returns the resource value to the caller.

The type of the returned resource value varies by resource property; for details, see the documentation for the key you want to access.

If this method returns [`true`](https://developer.apple.com/documentation/Swift/true) and the value is populated with `nil`, it means that the resource property is not available for the specified resource, and that no errors occurred when determining that the resource property was unavailable.

If this method returns [`false`](https://developer.apple.com/documentation/Swift/false), an error occurred. The object pointer referenced by `error` is populated with additional information.

> **Note**:  This method applies only to URLs that represent file system resources.

> **Note**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `value`: The location where the value for the resource property identified by   should be stored.
- `key`: The name of one of the URL’s resource properties.

## See Also

- [func resourceValues(forKeys: [URLResourceKey]) throws -> [URLResourceKey : Any]](nsurl/resourcevalues(forkeys:).md)
  Returns the resource values for the properties identified by specified array of keys.
- [func setResourceValue(Any?, forKey: URLResourceKey) throws](nsurl/setresourcevalue(_:forkey:).md)
  Sets the URL’s resource property for a given key to a given value.
- [func setResourceValues([URLResourceKey : Any]) throws](nsurl/setresourcevalues(_:).md)
  Sets the URL’s resource properties for a given set of keys to a given set of values.
- [func removeAllCachedResourceValues()](nsurl/removeallcachedresourcevalues.md)
  Removes all cached resource values and temporary resource values from the URL object.
- [func removeCachedResourceValue(forKey: URLResourceKey)](nsurl/removecachedresourcevalue(forkey:).md)
  Removes the cached resource value identified by a given key from the URL object.
- [func setTemporaryResourceValue((any Sendable)?, forKey: URLResourceKey)](nsurl/settemporaryresourcevalue(_:forkey:).md)
  Sets a temporary resource value on the URL object.
- [struct URLResourceKey](urlresourcekey.md)
  Keys that apply to file system URLs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurl/getresourcevalue(_:forkey:))*