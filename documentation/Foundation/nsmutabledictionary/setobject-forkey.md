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

- `anObject`: The value for  . A strong reference to the object is maintained by the dictionary.
- `aKey`: The key for  . The key is copied (using  ; keys must conform to the   protocol). If   already exists in the dictionary,   takes its place.

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