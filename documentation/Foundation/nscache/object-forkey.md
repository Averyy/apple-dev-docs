# object(forKey:)

**Framework**: Foundation  
**Kind**: method

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

#### Return Value

The value associated with `key`, or `nil` if no value is associated with `key`.

## Parameters

- `key`: An object identifying the value.

## See Also

- [func removeObject(forKey: KeyType)](nscache/removeobject(forkey:).md)
  Removes the value of the specified key in the cache.
- [func setObject(ObjectType, forKey: KeyType, cost: Int)](nscache/setobject(_:forkey:cost:).md)
  Sets the value of the specified key in the cache, and associates the key-value pair with the specified cost.
- [func setObject(ObjectType, forKey: KeyType)](nscache/setobject(_:forkey:).md)
  Sets the value of the specified key in the cache.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscache/object(forkey:))*