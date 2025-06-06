# NSMutableIndexSet

**Framework**: Foundation  
**Kind**: class

A mutable collection of unique integer values that represent indexes in another collection.

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
class NSMutableIndexSet
```

#### Overview

In Swift, this type bridges to [`IndexSet`](indexset.md); use [`NSMutableIndexSet`](nsmutableindexset.md) when you need reference semantics or other Foundation-specific behavior.

The [`NSMutableIndexSet`](nsmutableindexset.md) class represents a mutable collection of unique unsigned integers, known as  because of the way they are used. This collection is referred to as a . The inclusive range of valid indexes is `0...(NSNotFound - 1)`; trying to use indexes outside this range is invalid.

The values in a mutable index set are always sorted, so the order in which values are added is irrelevant.

Do not subclass the [`NSMutableIndexSet`](nsmutableindexset.md) class.

> ❗ **Important**:  The Swift overlay to the Foundation framework provides the [`IndexSet`](indexset.md) structure, which bridges to the [`NSMutableIndexSet`](nsmutableindexset.md) class and its immutable superclass, [`NSIndexSet`](nsindexset.md). For more information about value types, see [`Working with Cocoa Frameworks`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Swift/Conceptual/BuildingCocoaApps/WorkingWithCocoaDataTypes.html#//apple_ref/doc/uid/TP40014216-CH6) in [`Using Swift with Cocoa and Objective-C (Swift 4.1)`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Swift/Conceptual/BuildingCocoaApps/index.html#//apple_ref/doc/uid/TP40014216).

 The Swift overlay to the Foundation framework provides the [`IndexSet`](indexset.md) structure, which bridges to the [`NSMutableIndexSet`](nsmutableindexset.md) class and its immutable superclass, [`NSIndexSet`](nsindexset.md). For more information about value types, see [`Working with Cocoa Frameworks`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Swift/Conceptual/BuildingCocoaApps/WorkingWithCocoaDataTypes.html#//apple_ref/doc/uid/TP40014216-CH6) in [`Using Swift with Cocoa and Objective-C (Swift 4.1)`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Swift/Conceptual/BuildingCocoaApps/index.html#//apple_ref/doc/uid/TP40014216).

## Topics

### Adding Indexes
- [func add(Int)](nsmutableindexset/add(_:)-6dtkj.md)
  Adds an index  to the receiver.
- [func add(IndexSet)](nsmutableindexset/add(_:)-6zmti.md)
  Adds the indexes in an index set to the receiver.
- [func add(in: NSRange)](nsmutableindexset/add(in:).md)
  Adds the indexes in an index range to the receiver.
### Removing Indexes
- [func remove(Int)](nsmutableindexset/remove(_:)-5li0r.md)
  Removes an index from the receiver.
- [func remove(IndexSet)](nsmutableindexset/remove(_:)-196u2.md)
  Removes the indexes in an index set from the receiver.
- [func removeAllIndexes()](nsmutableindexset/removeallindexes.md)
  Removes the receiver’s indexes.
- [func remove(in: NSRange)](nsmutableindexset/remove(in:).md)
  Removes the indexes in an index range from the receiver.
### Shifting Index Groups
- [func shiftIndexesStarting(at: Int, by: Int)](nsmutableindexset/shiftindexesstarting(at:by:).md)
  Shifts a group of indexes to the left or the right within the receiver.

## Relationships

### Inherits From
- [NSIndexSet](nsindexset.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](nscoding.md)
- [NSCopying](nscopying.md)
- [NSMutableCopying](nsmutablecopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](nssecurecoding.md)
- [Sequence](../Swift/Sequence.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutableindexset)*