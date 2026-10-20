# totalCostLimit

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The maximum total cost that the cache can hold before it starts evicting objects.

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
var totalCostLimit: Int { get set }
```

```objc
@property NSUInteger totalCostLimit;
```

#### Discussion

If `0`, there is no total cost limit. The default value is `0`.

When you add an object to the cache, you may pass in a specified cost for the object, such as the size in bytes of the object. If adding this object to the cache causes the cache’s total cost to rise above `totalCostLimit`, the cache may automatically evict objects until its total cost falls below `totalCostLimit`. The order in which the cache evicts objects is not guaranteed.

This is not a strict limit, and if the cache goes over the limit, an object in the cache could be evicted instantly, at a later point in time, or possibly never, all depending on the implementation details of the cache.

## See Also

### Related Documentation
- [func setObject(ObjectType, forKey: KeyType, cost: Int)](./setobject%28_,forkey,cost%29.md)
  Sets the value of the specified key in the cache, and associates the key-value pair with the specified cost.
### Managing Cache Size
- [var countLimit: Int](./countlimit.md)
  The maximum number of objects the cache should hold.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscache/totalcostlimit)*