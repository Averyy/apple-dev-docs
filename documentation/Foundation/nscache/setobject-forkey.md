# setObject(_:forKey:)

**Framework**: Foundation  
**Kind**: method

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

#### Discussion

Unlike an `NSMutableDictionary` object, a cache does not copy the key objects that are put into it.

## Parameters

- `obj`: The object to be stored in the cache.
- `key`: The key with which to associate the value.

## See Also

- [func setObject(ObjectType, forKey: KeyType, cost: Int)](nscache/setobject(_:forkey:cost:).md)
  Sets the value of the specified key in the cache, and associates the key-value pair with the specified cost.
- [func removeObject(forKey: KeyType)](nscache/removeobject(forkey:).md)
  Removes the value of the specified key in the cache.
- [func removeAllObjects()](nscache/removeallobjects.md)
  Empties the cache.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscache/setobject(_:forkey:))*