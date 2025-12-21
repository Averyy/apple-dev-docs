# removeValue(at:fromPropertyWithKey:)

**Framework**: Objective-C Runtime  
**Kind**: method

Removes the object at the specified index from the collection specified by the passed key.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
func removeValue(at index: Int, fromPropertyWithKey key: String)
```

#### Discussion

The method `removeFrom<Key>AtIndex:` is invoked if it exists. If no corresponding scripting-KVC-compliant method (`-removeFrom<Key>AtIndex:`) is found, this method invokes `-mutableArrayValueForKey:` and mutates the result.

> **Note**:  Prior to OS X version 10.4, this method did not invoke `-mutableArrayValueForKey:`.

## See Also

- [func insertValue(Any, at: Int, inPropertyWithKey: String)](nsobject-swift.class/insertvalue(_:at:inpropertywithkey:).md)
  Inserts an object at the specified index in the collection specified by the passed key.
- [func replaceValue(at: Int, inPropertyWithKey: String, withValue: Any)](nsobject-swift.class/replacevalue(at:inpropertywithkey:withvalue:).md)
  Replaces the object at the specified index in the collection specified by the passed key.
- [func value(at: Int, inPropertyWithKey: String) -> Any?](nsobject-swift.class/value(at:inpropertywithkey:).md)
  Retrieves an indexed object from the collection specified by the passed key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/removevalue(at:frompropertywithkey:))*