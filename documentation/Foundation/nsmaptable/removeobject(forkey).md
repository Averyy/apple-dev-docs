# removeObject(forKey:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Removes a given key and its associated value from the map table.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func removeObject(forKey aKey: KeyType?)
```

```objc
- (void) removeObjectForKey:(KeyType) aKey;
```

#### Discussion

Does nothing if `aKey` does not exist.

## Parameters

- `aKey`: The key to remove.

## See Also

### Manipulating Content
- [func setObject(ObjectType?, forKey: KeyType?)](./setobject%28_,forkey%29.md)
  Adds a given key-value pair to the map table.
- [func removeAllObjects()](./removeallobjects%28%29.md)
  Empties the map table of its entries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmaptable/removeobject(forkey:))*