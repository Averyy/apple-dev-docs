# removeObject(forKey:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Removes the value of the specified key in the cache.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func removeObject(forKey key: KeyType)
```

```objc
- (void) removeObjectForKey:(KeyType) key;
```

## Parameters

- `key`: The key identifying the value to be removed.

## See Also

### Adding and Removing Cached Values
- [func setObject(ObjectType, forKey: KeyType)](./setobject%28_,forkey%29.md)
  Sets the value of the specified key in the cache.
- [func setObject(ObjectType, forKey: KeyType, cost: Int)](./setobject%28_,forkey,cost%29.md)
  Sets the value of the specified key in the cache, and associates the key-value pair with the specified cost.
- [func removeAllObjects()](./removeallobjects%28%29.md)
  Empties the cache.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscache/removeobject(forkey:))*