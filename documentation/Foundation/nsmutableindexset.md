# NSMutableIndexSet

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

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

```objc
@interface NSMutableIndexSet : NSIndexSet
```

## Overview

In Swift, this type bridges to [`IndexSet`](./indexset.md); use [`NSMutableIndexSet`](./nsmutableindexset.md) when you need reference semantics or other Foundation-specific behavior.

The [`NSMutableIndexSet`](./nsmutableindexset.md) class represents a mutable collection of unique unsigned integers, known as *indexes* because of the way they are used. This collection is referred to as a *mutable index set*. The inclusive range of valid indexes is `0...(NSNotFound - 1)`; trying to use indexes outside this range is invalid.

The values in a mutable index set are always sorted, so the order in which values are added is irrelevant.

Do not subclass the [`NSMutableIndexSet`](./nsmutableindexset.md) class.

> ❗ **Important**:  The Swift overlay to the Foundation framework provides the [`IndexSet`](./indexset.md) structure, which bridges to the [`NSMutableIndexSet`](./nsmutableindexset.md) class and its immutable superclass, [`NSIndexSet`](./nsindexset.md). For more information about value types, see [Working with Foundation Types](../Swift/working-with-foundation-types.md).

## Topics

### Adding Indexes
- [func add(Int)](./nsmutableindexset/add%28_%29-6dtkj.md)
  Adds an index  to the receiver.
- [func add(IndexSet)](./nsmutableindexset/add%28_%29-6zmti.md)
  Adds the indexes in an index set to the receiver.
- [func add(in: NSRange)](./nsmutableindexset/add%28in%29.md)
  Adds the indexes in an index range to the receiver.
### Removing Indexes
- [func remove(Int)](./nsmutableindexset/remove%28_%29-5li0r.md)
  Removes an index from the receiver.
- [func remove(IndexSet)](./nsmutableindexset/remove%28_%29-196u2.md)
  Removes the indexes in an index set from the receiver.
- [func removeAllIndexes()](./nsmutableindexset/removeallindexes%28%29.md)
  Removes the receiver’s indexes.
- [func remove(in: NSRange)](./nsmutableindexset/remove%28in%29.md)
  Removes the indexes in an index range from the receiver.
### Shifting Index Groups
- [func shiftIndexesStarting(at: Int, by: Int)](./nsmutableindexset/shiftindexesstarting%28at,by%29.md)
  Shifts a group of indexes to the left or the right within the receiver.

## Relationships

### Inherits From
- [NSIndexSet](./nsindexset.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](./nscoding.md)
- [NSCopying](./nscopying.md)
- [NSMutableCopying](./nsmutablecopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](./nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [Sequence](../Swift/sequence.md)

## See Also

### Indexes
- [NSIndexPath](./nsindexpath.md)
  A list of indexes that together represent the path to a specific location in a tree of nested arrays.
- [NSIndexSet](./nsindexset.md)
  An immutable collection of unique integer values that represent indexes in another collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutableindexset)*