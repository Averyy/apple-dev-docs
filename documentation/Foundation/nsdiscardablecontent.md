# NSDiscardableContent

**Framework**: Foundation  
**Kind**: protocol

You implement this protocol when a class’s objects have subcomponents that can be discarded when not being used, thereby giving an application a smaller memory footprint.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
protocol NSDiscardableContent
```

#### Overview

An `NSDiscardableContent` object’s life cycle is dependent upon a “counter” variable. An `NSDiscardableContent` object is a purgeable block of memory that keeps track of whether or not it is currently being used by some other object. When this memory is being read, or is still needed, its counter variable will be greater than or equal to 1. When it is not being used, and can be discarded, the counter variable will be equal to 0.

When the counter is equal to 0, the block of memory may be discarded if memory is tight at that point in time. In order to discard the content, call [`discardContentIfPossible()`](nsdiscardablecontent/discardcontentifpossible().md) on the object, which will free the associated memory if the counter variable equals 0.

By default, `NSDiscardableContent` objects are initialized with their counter equal to 1 to ensure that they are not immediately discarded by the memory-management system. From this point, you must keep track of the counter variable’s state. Calling the [`beginContentAccess()`](nsdiscardablecontent/begincontentaccess().md) method increments the counter variable by 1, thus ensuring that the object will not be discarded. When you no longer need the object, decrement its counter by calling [`endContentAccess()`](nsdiscardablecontent/endcontentaccess().md).

The Foundation framework includes the [`NSPurgeableData`](nspurgeabledata.md) class, which provides a default implementation of this protocol.

## Topics

### Accessing Content
- [func beginContentAccess() -> Bool](nsdiscardablecontent/begincontentaccess.md)
  Returns a Boolean value indicating whether the discardable contents are still available and have been successfully accessed.
- [func endContentAccess()](nsdiscardablecontent/endcontentaccess.md)
  Called if the discardable contents are no longer being accessed.
### Discarding Content
- [func discardContentIfPossible()](nsdiscardablecontent/discardcontentifpossible.md)
  Called to discard the contents of the receiver if the value of the accessed counter is 0.
- [func isContentDiscarded() -> Bool](nsdiscardablecontent/iscontentdiscarded.md)
  Returns a Boolean value indicating whether the content has been discarded.

## Relationships

### Conforming Types
- [NSPurgeableData](nspurgeabledata.md)

## See Also

- [var evictsObjectsWithDiscardedContent: Bool](nscache/evictsobjectswithdiscardedcontent.md)
  Whether the cache will automatically evict discardable-content objects whose content has been discarded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdiscardablecontent)*