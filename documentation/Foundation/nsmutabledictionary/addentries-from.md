# addEntries(from:)

**Framework**: Foundation  
**Kind**: method

Adds to the receiving dictionary the entries from another dictionary.

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
func addEntries(from otherDictionary: [AnyHashable : Any])
```

#### Discussion

Each value object from `otherDictionary` is sent a [`retain`](https://developer.apple.com/documentation/ObjectiveC/NSObject-c.protocol/retain) message before being added to the receiving dictionary. In contrast, each key object is copied (using [`copy(with:)`](nscopying/copy(with:).md)—keys must conform to the `NSCopying` protocol), and the copy is added to the receiving dictionary.

If both dictionaries contain the same key, the receiving dictionary’s previous value object for that key is sent a `release` message, and the new value object takes its place.

## Parameters

- `otherDictionary`: The dictionary from which to add entries

## See Also

- [func setObject(Any, forKey: any NSCopying)](nsmutabledictionary/setobject(_:forkey:).md)
  Adds a given key-value pair to the dictionary.
- [func setValue(Any?, forKey: String)](nsmutabledictionary/setvalue(_:forkey:).md)
  Adds a given key-value pair to the dictionary.
- [func setDictionary([AnyHashable : Any])](nsmutabledictionary/setdictionary(_:).md)
  Sets the contents of the receiving dictionary to entries in a given dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutabledictionary/addentries(from:))*