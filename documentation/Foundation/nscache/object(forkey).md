# object(forKey:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns the value associated with a given key.

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
func object(forKey key: KeyType) -> ObjectType?
```

```objc
- (ObjectType) objectForKey:(KeyType) key;
```

## Return Value

The value associated with `key`, or `nil` if no value is associated with `key`.

## Parameters

- `key`: An object identifying the value.

## See Also

### Related Documentation
- [func removeObject(forKey: KeyType)](./removeobject%28forkey%29.md)
  Removes the value of the specified key in the cache.
- [func setObject(ObjectType, forKey: KeyType, cost: Int)](./setobject%28_,forkey,cost%29.md)
  Sets the value of the specified key in the cache, and associates the key-value pair with the specified cost.
- [func setObject(ObjectType, forKey: KeyType)](./setobject%28_,forkey%29.md)
  Sets the value of the specified key in the cache.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscache/object(forkey:))*