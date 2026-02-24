# setObject(_:forKey:)

**Framework**: Foundation  
**Kind**: method

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

## Parameters

- `anObject`: The value for `aKey`. A strong reference to the object is maintained by the dictionary. > ❗ **Important**:  Raises an [`invalidArgumentException`](nsexceptionname/invalidargumentexception.md) if `anObject` is `nil`. If you need to represent a `nil` value in the dictionary, use [`NSNull`](nsnull.md).
- `aKey`: The key for `value`. The key is copied (using [`copy(with:)`](nscopying/copy(with:).md); keys must conform to the `NSCopying` protocol). If `aKey` already exists in the dictionary, `anObject` takes its place. > ❗ **Important**:  Raises an [`invalidArgumentException`](nsexceptionname/invalidargumentexception.md) if `aKey` is `nil`.

## See Also

- [func removeObject(forKey: Any)](nsmutabledictionary/removeobject(forkey:).md)
  Removes a given key and its associated value from the dictionary.
- [func setValue(Any?, forKey: String)](nsmutabledictionary/setvalue(_:forkey:).md)
  Adds a given key-value pair to the dictionary.
- [func addEntries(from: [AnyHashable : Any])](nsmutabledictionary/addentries(from:).md)
  Adds to the receiving dictionary the entries from another dictionary.
- [func setDictionary([AnyHashable : Any])](nsmutabledictionary/setdictionary(_:).md)
  Sets the contents of the receiving dictionary to entries in a given dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutabledictionary/setobject(_:forkey:))*