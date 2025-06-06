# NSCache

**Framework**: Foundation  
**Kind**: class

A mutable collection you use to temporarily store transient key-value pairs that are subject to eviction when resources are low.

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
class NSCache<KeyType, ObjectType> where KeyType : AnyObject, ObjectType : AnyObject
```

#### Overview

Cache objects differ from other mutable collections in a few ways:

- The [`NSCache`](nscache.md) class incorporates various auto-eviction policies, which ensure that a cache doesn’t use too much of the system’s memory. If memory is needed by other applications, these policies remove some items from the cache, minimizing its memory footprint.
- You can add, remove, and query items in the cache from different threads without having to lock the cache yourself.
- Unlike an [`NSMutableDictionary`](nsmutabledictionary.md) object, a cache does not copy the key objects that are put into it.

You typically use [`NSCache`](nscache.md) objects to temporarily store objects with transient data that are expensive to create. Reusing these objects can provide performance benefits, because their values do not have to be recalculated. However, the objects are not critical to the application and can be discarded if memory is tight. If discarded, their values will have to be recomputed again when needed.

Objects that have subcomponents that can be discarded when not being used can adopt the [`NSDiscardableContent`](nsdiscardablecontent.md) protocol to improve cache eviction behavior. By default, [`NSDiscardableContent`](nsdiscardablecontent.md) objects in a cache are automatically removed if their content is discarded, although this automatic removal policy can be changed. If an [`NSDiscardableContent`](nsdiscardablecontent.md) object is put into the cache, the cache calls [`discardContentIfPossible()`](nsdiscardablecontent/discardcontentifpossible().md) on it upon its removal.

## Topics

### Managing the Name
- [var name: String](nscache/name.md)
  The name of the cache.
### Managing Cache Size
- [var countLimit: Int](nscache/countlimit.md)
  The maximum number of objects the cache should hold.
- [var totalCostLimit: Int](nscache/totalcostlimit.md)
  The maximum total cost that the cache can hold before it starts evicting objects.
### Managing Discardable Content
- [var evictsObjectsWithDiscardedContent: Bool](nscache/evictsobjectswithdiscardedcontent.md)
  Whether the cache will automatically evict discardable-content objects whose content has been discarded.
- [protocol NSDiscardableContent](nsdiscardablecontent.md)
  You implement this protocol when a class’s objects have subcomponents that can be discarded when not being used, thereby giving an application a smaller memory footprint.
### Managing the Delegate
- [var delegate: (any NSCacheDelegate)?](nscache/delegate.md)
  The cache’s delegate.
- [protocol NSCacheDelegate](nscachedelegate.md)
  The delegate of an [`NSCache`](nscache.md) object implements this protocol to perform specialized actions when an object is about to be evicted or removed from the cache.
### Getting a Cached Value
- [func object(forKey: KeyType) -> ObjectType?](nscache/object(forkey:).md)
  Returns the value associated with a given key.
### Adding and Removing Cached Values
- [func setObject(ObjectType, forKey: KeyType)](nscache/setobject(_:forkey:).md)
  Sets the value of the specified key in the cache.
- [func setObject(ObjectType, forKey: KeyType, cost: Int)](nscache/setobject(_:forkey:cost:).md)
  Sets the value of the specified key in the cache, and associates the key-value pair with the specified cost.
- [func removeObject(forKey: KeyType)](nscache/removeobject(forkey:).md)
  Removes the value of the specified key in the cache.
- [func removeAllObjects()](nscache/removeallobjects.md)
  Empties the cache.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSPurgeableData](nspurgeabledata.md)
  A mutable data object containing bytes that can be discarded when they’re no longer needed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscache)*