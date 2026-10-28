# setResourceValue(_:forKey:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Sets the URL’s resource property for a given key to a given value.

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
func setResourceValue(_ value: Any?, forKey key: URLResourceKey) throws
```

```objc
- (BOOL) setResourceValue:(id) value forKey:(NSURLResourceKey) key error:(NSError **) error;
```

## Mentions

- [Using the file system effectively](../using-the-file-system-effectively.md)

## Discussion

This method synchronously writes the new resource value out to disk. Attempts to set a read-only resource property or to set a resource property that is not supported by the resource are ignored and are not considered errors.

If an error occurs, this method returns [`false`](../../Swift/false.md) and populates the object pointer referenced by `error` with additional information.

> **Note**:  This method applies only to URLs for file system resources.

> **Handling Errors in Swift**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `value`: The value for the resource property defined by `key`.
- `key`: The name of one of the URL’s resource properties.

## See Also

### Accessing Resource Values
- [func resourceValues(forKeys: [URLResourceKey]) throws -> [URLResourceKey : Any]](./resourcevalues%28forkeys%29.md)
  Returns the resource values for the properties identified by specified array of keys.
- [func getResourceValue(AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey: URLResourceKey) throws](./getresourcevalue%28_,forkey%29.md)
  Returns the value of the resource property for the specified key.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurl/setresourcevalue(_:forkey:))*