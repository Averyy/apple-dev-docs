# setObject(_:forKey:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Adds a given key-value pair to the dictionary.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func setObject(_ anObject: Any, forKey aKey: any NSCopying)
```

```objc
- (void) setObject:(ObjectType) anObject forKey:(id<NSCopying>) aKey;
```

## Parameters

- `anObject`: The value for `aKey`. A strong reference to the object is maintained by the dictionary.

  > ❗ **Important**:  Raises an [`invalidArgumentException`](../nsexceptionname/invalidargumentexception.md) if `anObject` is `nil`. If you need to represent a `nil` value in the dictionary, use [`NSNull`](../nsnull.md).
- `aKey`: The key for `value`. The key is copied (using [`copy(with:)`](../nscopying/copy%28with%29.md); keys must conform to the `NSCopying` protocol). If `aKey` already exists in the dictionary, `anObject` takes its place.

  > ❗ **Important**:  Raises an [`invalidArgumentException`](../nsexceptionname/invalidargumentexception.md) if `aKey` is `nil`.

## See Also

### Related Documentation
- [func removeObject(forKey: Any)](./removeobject%28forkey%29.md)
  Removes a given key and its associated value from the dictionary.
### Adding Entries to a Mutable Dictionary
- [func setValue(Any?, forKey: String)](./setvalue%28_,forkey%29.md)
  Adds a given key-value pair to the dictionary.
- [func addEntries(from: [AnyHashable : Any])](./addentries%28from%29.md)
  Adds to the receiving dictionary the entries from another dictionary.
- [func setDictionary([AnyHashable : Any])](./setdictionary%28_%29.md)
  Sets the contents of the receiving dictionary to entries in a given dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutabledictionary/setobject(_:forkey:))*