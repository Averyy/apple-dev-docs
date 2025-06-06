# insertValue(_:at:inPropertyWithKey:)

**Framework**: Objectivec  
**Kind**: method

Inserts an object at the specified index in the collection specified by the passed key.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)
```

#### Discussion

The method `insertIn<Key>:atIndex:` is invoked if it exists. If no corresponding scripting-KVC-compliant method (`insertIn<Key>:atIndex:` ) is found, this method invokes `mutableArrayValueForKey:` and mutates the result.

> **Note**:  Prior to OS X version 10.4, this method did not invoke `-mutableArrayValueForKey:`.

## See Also

- [func removeValue(at: Int, fromPropertyWithKey: String)](nsobject-swift.class/removevalue(at:frompropertywithkey:).md)
  Removes the object at the specified index from the collection specified by the passed key.
- [func replaceValue(at: Int, inPropertyWithKey: String, withValue: Any)](nsobject-swift.class/replacevalue(at:inpropertywithkey:withvalue:).md)
  Replaces the object at the specified index in the collection specified by the passed key.
- [func value(at: Int, inPropertyWithKey: String) -> Any?](nsobject-swift.class/value(at:inpropertywithkey:).md)
  Retrieves an indexed object from the collection specified by the passed key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/insertvalue(_:at:inpropertywithkey:))*