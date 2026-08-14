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

The [`NSMutableIndexSet`](nsmutableindexset.md) class represents a mutable collection of unique unsigned integers, known as *indexes* because of the way they are used. This collection is referred to as a *mutable index set*. The inclusive range of valid indexes is `0...(NSNotFound - 1)`; trying to use indexes outside this range is invalid.

The values in a mutable index set are always sorted, so the order in which values are added is irrelevant.

Do not subclass the [`NSMutableIndexSet`](nsmutableindexset.md) class.

> ❗ **Important**:  The Swift overlay to the Foundation framework provides the [`IndexSet`](indexset.md) structure, which bridges to the [`NSMutableIndexSet`](nsmutableindexset.md) class and its immutable superclass, [`NSIndexSet`](nsindexset.md). For more information about value types, see [`Working with Foundation Types`](https://developer.apple.com/documentation/swift/working-with-foundation-types).

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
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](nscoding.md)
- [NSCopying](nscopying.md)
- [NSMutableCopying](nsmutablecopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](nssecurecoding.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [Sequence](../swift/sequence.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutableindexset)*