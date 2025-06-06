# setResourceValues(_:)

**Framework**: Foundation  
**Kind**: method

Sets the URL’s resource properties for a given set of keys to a given set of values.

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
func setResourceValues(_ keyedValues: [URLResourceKey : Any]) throws
```

#### Discussion

This method synchronously writes the new resource value out to disk. If an error occurs after some resource properties have been successfully changed, the `userInfo` dictionary in the returned error object contains a `kCFURLKeysOfUnsetValuesKey` key whose value is an array of the resource values that were not successfully set.

Attempts to set a read-only resource property or to set a resource property that is not supported by the resource are ignored and are not considered errors.

The order in which the resource values are set is not defined. If you need to guarantee the order in which resource values are set, you should make multiple requests to this method or [`setResourceValue(_:forKey:)`](nsurl/setresourcevalue(_:forkey:).md).

> **Note**:  This method applies only to URLs for file system resources.

 This method applies only to URLs for file system resources.

> **Note**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

 In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.

You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `keyedValues`: A dictionary of resource values to be set.

## See Also

- [func resourceValues(forKeys: [URLResourceKey]) throws -> [URLResourceKey : Any]](nsurl/resourcevalues(forkeys:).md)
  Returns the resource values for the properties identified by specified array of keys.
- [func getResourceValue(AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey: URLResourceKey) throws](nsurl/getresourcevalue(_:forkey:).md)
  Returns the value of the resource property for the specified key.
- [func setResourceValue(Any?, forKey: URLResourceKey) throws](nsurl/setresourcevalue(_:forkey:).md)
  Sets the URL’s resource property for a given key to a given value.
- [func removeAllCachedResourceValues()](nsurl/removeallcachedresourcevalues.md)
  Removes all cached resource values and temporary resource values from the URL object.
- [func removeCachedResourceValue(forKey: URLResourceKey)](nsurl/removecachedresourcevalue(forkey:).md)
  Removes the cached resource value identified by a given key from the URL object.
- [func setTemporaryResourceValue((any Sendable)?, forKey: URLResourceKey)](nsurl/settemporaryresourcevalue(_:forkey:).md)
  Sets a temporary resource value on the URL object.
- [struct URLResourceKey](urlresourcekey.md)
  Keys that apply to file system URLs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurl/setresourcevalues(_:))*