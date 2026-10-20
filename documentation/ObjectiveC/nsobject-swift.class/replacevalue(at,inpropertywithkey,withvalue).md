# replaceValue(at:inPropertyWithKey:withValue:)

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Replaces the object at the specified index in the collection specified by the passed key.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)
```

```objc
- (void) replaceValueAtIndex:(NSUInteger) index inPropertyWithKey:(NSString *) key withValue:(id) value;
```

#### Discussion

The method `replaceIn<Key>:atIndex:` is invoked if it exists. If no corresponding scripting-KVC-compliant method (`-replaceIn<Key>atIndex:`) is found, this method invokes `-mutableArrayValueForKey:` and mutates the result.

> **Note**:  Prior to OS X version 10.4, this method did not invoke `-mutableArrayValueForKey:`.

## See Also

### Indexed access
- [func insertValue(Any, at: Int, inPropertyWithKey: String)](./insertvalue%28_,at,inpropertywithkey%29.md)
  Inserts an object at the specified index in the collection specified by the passed key.
- [func removeValue(at: Int, fromPropertyWithKey: String)](./removevalue%28at,frompropertywithkey%29.md)
  Removes the object at the specified index from the collection specified by the passed key.
- [func value(at: Int, inPropertyWithKey: String) -> Any?](./value%28at,inpropertywithkey%29.md)
  Retrieves an indexed object from the collection specified by the passed key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/replacevalue(at:inpropertywithkey:withvalue:))*