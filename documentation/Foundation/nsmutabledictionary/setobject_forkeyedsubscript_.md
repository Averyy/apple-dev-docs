# setObject:forKeyedSubscript:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Adds a given key-value pair to the dictionary.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```objc
- (void) setObject:(ObjectType) obj forKeyedSubscript:(id<NSCopying>) key;
```

#### Discussion

This method has the same behavior as the [`setObject(_:forKey:)`](./setobject%28_,forkey%29.md) method.

You shouldn’t need to call this method directly. Instead, this method is called when setting an object for a key using subscripting.

```objc
id value = @"someValue";
mutableDictionary[@"someKey"] = value;
```

## Parameters

- `obj`: The value for `key`. A strong reference to the object is maintained by the dictionary.

  Passing `nil` will cause any object corresponding to `key` to be removed from the dictionary.
- `key`: The key for `obj`. The key is copied (using [`copy(with:)`](../nscopying/copy%28with%29.md); keys must conform to the `NSCopying` protocol). If `key` already exists in the dictionary, `anObject` takes its place.

  > ❗ **Important**:  Raises an [`invalidArgumentException`](../nsexceptionname/invalidargumentexception.md) if `key` is `nil`.

## See Also

### Related Documentation
- [func removeObject(forKey: Any)](./removeobject%28forkey%29.md)
  Removes a given key and its associated value from the dictionary.
- [subscript(any NSCopying) -> Any?](../nsdictionary/subscript%28_%29-52n56.md)
  Returns the value associated with a given key.
### Adding Entries to a Mutable Dictionary
- [func setObject(Any, forKey: any NSCopying)](./setobject%28_,forkey%29.md)
  Adds a given key-value pair to the dictionary.
- [func setValue(Any?, forKey: String)](./setvalue%28_,forkey%29.md)
  Adds a given key-value pair to the dictionary.
- [func addEntries(from: [AnyHashable : Any])](./addentries%28from%29.md)
  Adds to the receiving dictionary the entries from another dictionary.
- [func setDictionary([AnyHashable : Any])](./setdictionary%28_%29.md)
  Sets the contents of the receiving dictionary to entries in a given dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutabledictionary/setobject:forkeyedsubscript:)*