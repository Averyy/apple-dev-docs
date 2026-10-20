# setObject(_:forKey:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Sets the value of the specified key in the cache.

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
func setObject(_ obj: ObjectType, forKey key: KeyType)
```

```objc
- (void) setObject:(ObjectType) obj forKey:(KeyType) key;
```

#### Discussion

Unlike an `NSMutableDictionary` object, a cache does not copy the key objects that are put into it.

## Parameters

- `obj`: The object to be stored in the cache.
- `key`: The key with which to associate the value.

## See Also

### Adding and Removing Cached Values
- [func setObject(ObjectType, forKey: KeyType, cost: Int)](./setobject%28_,forkey,cost%29.md)
  Sets the value of the specified key in the cache, and associates the key-value pair with the specified cost.
- [func removeObject(forKey: KeyType)](./removeobject%28forkey%29.md)
  Removes the value of the specified key in the cache.
- [func removeAllObjects()](./removeallobjects%28%29.md)
  Empties the cache.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscache/setobject(_:forkey:))*