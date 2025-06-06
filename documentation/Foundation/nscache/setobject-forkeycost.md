# setObject(_:forKey:cost:)

**Framework**: Foundation  
**Kind**: method

Sets the value of the specified key in the cache, and associates the key-value pair with the specified cost.

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
func setObject(_ obj: ObjectType, forKey key: KeyType, cost g: Int)
```

#### Discussion

The `cost` value is used to compute a sum encompassing the costs of all the objects in the cache. When memory is limited or when the total cost of the cache eclipses the maximum allowed total cost, the cache could begin an eviction process to remove some of its elements. However, this eviction process is not in a guaranteed order. As a consequence, if you try to manipulate the cost values to achieve some specific behavior, the consequences could be detrimental to your program. Typically, the obvious cost is the size of the value in bytes. If that information is not readily available, you should not go through the trouble of trying to compute it, as doing so will drive up the cost of using the cache. Pass in `0` for the cost value if you otherwise have nothing useful to pass, or simply use the `setObject:forKey:` method, which does not require a `cost` value to be passed in.

Unlike an `NSMutableDictionary` object, a cache does not copy the key objects that are put into it.

## Parameters

- `obj`: The object to store in the cache.
- `key`: The key with which to associate the value.
- `g`: The cost with which to associate the key-value pair.

## See Also

- [var totalCostLimit: Int](nscache/totalcostlimit.md)
  The maximum total cost that the cache can hold before it starts evicting objects.
- [func setObject(ObjectType, forKey: KeyType)](nscache/setobject(_:forkey:).md)
  Sets the value of the specified key in the cache.
- [func removeObject(forKey: KeyType)](nscache/removeobject(forkey:).md)
  Removes the value of the specified key in the cache.
- [func removeAllObjects()](nscache/removeallobjects.md)
  Empties the cache.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscache/setobject(_:forkey:cost:))*