# value(at:inPropertyWithKey:)

**Framework**: Objective-C Runtime  
**Kind**: method

Retrieves an indexed object from the collection specified by the passed key.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
func value(at index: Int, inPropertyWithKey key: String) -> Any?
```

#### Discussion

This actually works with a single-value key as well if `index` is 0. The method `valueIn<Key>AtIndex:` is used if it exists.

## See Also

- [func insertValue(Any, at: Int, inPropertyWithKey: String)](nsobject-swift.class/insertvalue(_:at:inpropertywithkey:).md)
  Inserts an object at the specified index in the collection specified by the passed key.
- [func removeValue(at: Int, fromPropertyWithKey: String)](nsobject-swift.class/removevalue(at:frompropertywithkey:).md)
  Removes the object at the specified index from the collection specified by the passed key.
- [func replaceValue(at: Int, inPropertyWithKey: String, withValue: Any)](nsobject-swift.class/replacevalue(at:inpropertywithkey:withvalue:).md)
  Replaces the object at the specified index in the collection specified by the passed key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/value(at:inpropertywithkey:))*