# value(at:inPropertyWithKey:)

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Retrieves an indexed object from the collection specified by the passed key.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
func value(at index: Int, inPropertyWithKey key: String) -> Any?
```

```objc
- (id) valueAtIndex:(NSUInteger) index inPropertyWithKey:(NSString *) key;
```

#### Discussion

This actually works with a single-value key as well if `index` is 0. The method `valueIn<Key>AtIndex:` is used if it exists.

## See Also

### Indexed access
- [func insertValue(Any, at: Int, inPropertyWithKey: String)](./insertvalue%28_,at,inpropertywithkey%29.md)
  Inserts an object at the specified index in the collection specified by the passed key.
- [func removeValue(at: Int, fromPropertyWithKey: String)](./removevalue%28at,frompropertywithkey%29.md)
  Removes the object at the specified index from the collection specified by the passed key.
- [func replaceValue(at: Int, inPropertyWithKey: String, withValue: Any)](./replacevalue%28at,inpropertywithkey,withvalue%29.md)
  Replaces the object at the specified index in the collection specified by the passed key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/value(at:inpropertywithkey:))*