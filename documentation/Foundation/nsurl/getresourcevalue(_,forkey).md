# getResourceValue(_:forKey:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (BOOL) getResourceValue:(id*) value forKey:(NSURLResourceKey) key error:(NSError **) error;
```

## Discussion

This method first checks if the URL object already caches the resource value. If so, it returns the cached resource value to the caller. If not, then this method synchronously obtains the resource value from the backing store, adds the resource value to the URL object’s cache, and returns the resource value to the caller.

The type of the returned resource value varies by resource property; for details, see the documentation for the key you want to access.

If this method returns [`true`](../../Swift/true.md) and the value is populated with `nil`, it means that the resource property is not available for the specified resource, and that no errors occurred when determining that the resource property was unavailable.

If this method returns [`false`](../../Swift/false.md), an error occurred. The object pointer referenced by `error` is populated with additional information.

> **Note**:  This method applies only to URLs that represent file system resources.

> **Handling Errors in Swift**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `value`: The location where the value for the resource property identified by `key` should be stored.
- `key`: The name of one of the URL’s resource properties.

## See Also

### Accessing Resource Values
- [func resourceValues(forKeys: [URLResourceKey]) throws -> [URLResourceKey : Any]](./resourcevalues%28forkeys%29.md)
  Returns the resource values for the properties identified by specified array of keys.
- [func setResourceValue(Any?, forKey: URLResourceKey) throws](./setresourcevalue%28_,forkey%29.md)
  Sets the URL’s resource property for a given key to a given value.
- [func setResourceValues([URLResourceKey : Any]) throws](./setresourcevalues%28_%29.md)
  Sets the URL’s resource properties for a given set of keys to a given set of values.
- [func removeAllCachedResourceValues()](./removeallcachedresourcevalues%28%29.md)
  Removes all cached resource values and temporary resource values from the URL object.
- [func removeCachedResourceValue(forKey: URLResourceKey)](./removecachedresourcevalue%28forkey%29.md)
  Removes the cached resource value identified by a given key from the URL object.
- [func setTemporaryResourceValue((any Sendable)?, forKey: URLResourceKey)](./settemporaryresourcevalue%28_,forkey%29.md)
  Sets a temporary resource value on the URL object.
- [struct URLResourceKey](../urlresourcekey.md)
  Keys that apply to file system URLs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurl/getresourcevalue(_:forkey:))*