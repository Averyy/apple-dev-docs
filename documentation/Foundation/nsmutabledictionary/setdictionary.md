# setDictionary(_:)

**Framework**: Foundation  
**Kind**: method

Sets the contents of the receiving dictionary to entries in a given dictionary.

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
func setDictionary(_ otherDictionary: [AnyHashable : Any])
```

#### Discussion

All entries are removed from the receiving dictionary (with [`removeAllObjects()`](nsmutabledictionary/removeallobjects().md)), then each entry from `otherDictionary` added into the receiving dictionary.

## Parameters

- `otherDictionary`: A dictionary containing the new entries.

## See Also

- [func setObject(Any, forKey: any NSCopying)](nsmutabledictionary/setobject(_:forkey:).md)
  Adds a given key-value pair to the dictionary.
- [func setValue(Any?, forKey: String)](nsmutabledictionary/setvalue(_:forkey:).md)
  Adds a given key-value pair to the dictionary.
- [func addEntries(from: [AnyHashable : Any])](nsmutabledictionary/addentries(from:).md)
  Adds to the receiving dictionary the entries from another dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutabledictionary/setdictionary(_:))*