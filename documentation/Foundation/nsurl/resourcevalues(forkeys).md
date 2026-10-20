# resourceValues(forKeys:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns the resource values for the properties identified by specified array of keys.

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
func resourceValues(forKeys keys: [URLResourceKey]) throws -> [URLResourceKey : Any]
```

```objc
- (NSDictionary<NSString *,id> *) resourceValuesForKeys:(NSArray<NSString *> *) keys error:(NSError **) error;
```

#### Return Value

A dictionary of resource values indexed by key.

#### Discussion

This method first checks if the URL object already caches the specified resource values. If so, it returns the cached resource values to the caller. If not, then this method synchronously obtains the resource values from the backing store, adds the resource values to the URL object’s cache, and returns the resource values to the caller.

The type of the returned resource value varies by resource property; for details, see the documentation for the key you want to access.

If the result dictionary does not contain a resource value for one or more of the requested resource keys, it means those resource properties are not available for the URL, and no errors occurred when determining those resource properties were not available.

If an error occurs, this method returns `nil` and populates the object pointer referenced by `error` with additional information.

> **Note**:  This method applies only to URLs that represent file system resources.

> **Handling Errors in Swift**:  In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `keys`: An array of property keys for the desired resource properties.

## See Also

### Accessing Resource Values
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
- [func setTemporaryResourceValue((any Sendable)?, forKey: URLResourceKey)](./settemporaryresourcevalue%28_,forkey%29.md)
  Sets a temporary resource value on the URL object.
- [struct URLResourceKey](../urlresourcekey.md)
  Keys that apply to file system URLs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurl/resourcevalues(forkeys:))*