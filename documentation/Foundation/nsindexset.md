# NSIndexSet

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

An immutable collection of unique integer values that represent indexes in another collection.

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
class NSIndexSet
```

```objc
@interface NSIndexSet : NSObject
```

#### Overview

In Swift, this type bridges to [`IndexSet`](./indexset.md); use [`NSIndexSet`](./nsindexset.md) when you need reference semantics or other Foundation-specific behavior.

The `NSIndexSet` class represents an immutable collection of unique unsigned integers, known as **indexes** because of the way they are used. This collection is referred to as an **index set**. Indexes must be in the range `0 .. NSNotFound - 1`.

You use index sets in your code to store indexes into some other data structure. For example, given an `NSArray` object, you could use an index set to identify a subset of objects in that array.

You should not use index sets to store an arbitrary collection of integer values because index sets store indexes as sorted ranges. This makes them more efficient than storing a collection of individual integers. It also means that each index value can only appear once in the index set.

The designated initializers of the `NSIndexSet` class are: [`init(index:)`](./nsindexset/init%28index%29.md), [`init(indexesIn:)`](./nsindexset/init%28indexesin%29.md), and [`init(indexSet:)`](./nsindexset/init%28indexset%29.md).

You must not subclass the `NSIndexSet` class.

The mutable subclass of `NSIndexSet` is [`NSMutableIndexSet`](./nsmutableindexset.md).

> ❗ **Important**:  The Swift overlay to the Foundation framework provides the [`IndexSet`](./indexset.md) structure, which bridges to the [`NSIndexSet`](./nsindexset.md) class and its mutable subclass, [`NSMutableIndexSet`](./nsmutableindexset.md). For more information about value types, see [Working with Foundation Types](../Swift/working-with-foundation-types.md).

## Topics

### Creating Index Sets
- [convenience init(index: Int)](./nsindexset/init%28index%29.md)
  Initializes an allocated [`NSIndexSet`](./nsindexset.md) object with an index.
- [init(indexesIn: NSRange)](./nsindexset/init%28indexesin%29.md)
  Initializes an allocated [`NSIndexSet`](./nsindexset.md) object with an index range.
- [init(indexSet: IndexSet)](./nsindexset/init%28indexset%29.md)
  Initializes an allocated [`NSIndexSet`](./nsindexset.md) object with an index set.
### Querying Index Sets
- [func contains(Int) -> Bool](./nsindexset/contains%28_%29-bb19.md)
  Indicates whether the index set contains a specific index.
- [func contains(IndexSet) -> Bool](./nsindexset/contains%28_%29-5j2kh.md)
  Indicates whether the receiving index set contains a superset of the indexes in another index set.
- [func contains(in: NSRange) -> Bool](./nsindexset/contains%28in%29.md)
  Indicates whether the index set contains the indexes represented by an index range.
- [func intersects(in: NSRange) -> Bool](./nsindexset/intersects%28in%29.md)
  Indicates whether the index set contains any of the indexes in a range.
- [var count: Int](./nsindexset/count.md)
  The number of indexes in the index set.
- [func countOfIndexes(in: NSRange) -> Int](./nsindexset/countofindexes%28in%29.md)
  Returns the number of indexes in the index set that are members of a given range.
- [func index(passingTest: (Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int](./nsindexset/index%28passingtest%29.md)
  Returns the index of the first object that passes the predicate Block test.
- [func indexes(passingTest: (Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> IndexSet](./nsindexset/indexes%28passingtest%29.md)
  Returns an `NSIndexSet` containing the receiving index set’s objects that pass the Block test.
- [func index(options: NSEnumerationOptions, passingTest: (Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int](./nsindexset/index%28options,passingtest%29.md)
  Returns the index of the first object that passes the predicate Block test using the specified enumeration options.
- [func indexes(options: NSEnumerationOptions, passingTest: (Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> IndexSet](./nsindexset/indexes%28options,passingtest%29.md)
  Returns an `NSIndexSet` containing the receiving index set’s objects that pass the Block test using the specified enumeration options.
- [func index(in: NSRange, options: NSEnumerationOptions, passingTest: (Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int](./nsindexset/index%28in,options,passingtest%29.md)
  Returns the index of the first object in the specified range that passes the predicate Block test.
- [func indexes(in: NSRange, options: NSEnumerationOptions, passingTest: (Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> IndexSet](./nsindexset/indexes%28in,options,passingtest%29.md)
  Returns an `NSIndexSet` containing the receiving index set’s objects in the specified range that pass the Block test.
### Enumerating Index Set Content
- [func enumerateRanges(in: NSRange, options: NSEnumerationOptions, using: (NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)](./nsindexset/enumerateranges%28in,options,using%29.md)
  Enumerates over the ranges in the range of objects using the block
- [func enumerateRanges((NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)](./nsindexset/enumerateranges%28_%29.md)
  Executes a given block using each object in the index set, in the specified ranges.
- [func enumerateRanges(options: NSEnumerationOptions, using: (NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)](./nsindexset/enumerateranges%28options,using%29.md)
  Executes a given block using each object in the index set, in the specified ranges.
### Comparing Index Sets
- [func isEqual(to: IndexSet) -> Bool](./nsindexset/isequal%28to%29.md)
  Indicates whether the indexes in the receiving index set are the same indexes contained in another index set.
### Getting Indexes
- [var firstIndex: Int](./nsindexset/firstindex.md)
  The first index in the index set.
- [var lastIndex: Int](./nsindexset/lastindex.md)
  The last index in the index set.
- [func indexLessThanIndex(Int) -> Int](./nsindexset/indexlessthanindex%28_%29.md)
  Returns either the closest index in the index set that is less than a specific index or the not-found indicator.
- [func indexLessThanOrEqual(to: Int) -> Int](./nsindexset/indexlessthanorequal%28to%29.md)
  Returns either the closest index in the index set that is less than or equal to a specific index or the not-found indicator.
- [func indexGreaterThanOrEqual(to: Int) -> Int](./nsindexset/indexgreaterthanorequal%28to%29.md)
  Returns either the closest index in the index set that is greater than or equal to a specific index or the not-found indicator.
- [func indexGreaterThanIndex(Int) -> Int](./nsindexset/indexgreaterthanindex%28_%29.md)
  Returns either the closest index in the index set that is greater than a specific index or the not-found indicator.
- [func getIndexes(UnsafeMutablePointer<Int>, maxCount: Int, inIndexRange: NSRangePointer?) -> Int](./nsindexset/getindexes%28_,maxcount,inindexrange%29.md)
  The index set fills an index buffer with the indexes contained both in the index set and in an index range, returning the number of indexes copied.
### Enumerating Indexes
- [func enumerate((Int, UnsafeMutablePointer<ObjCBool>) -> Void)](./nsindexset/enumerate%28_%29.md)
  Executes a given Block using each object in the index set.
- [func enumerate(options: NSEnumerationOptions, using: (Int, UnsafeMutablePointer<ObjCBool>) -> Void)](./nsindexset/enumerate%28options,using%29.md)
  Executes a given Block over the index set’s indexes, using the specified enumeration options.
- [func enumerate(in: NSRange, options: NSEnumerationOptions, using: (Int, UnsafeMutablePointer<ObjCBool>) -> Void)](./nsindexset/enumerate%28in,options,using%29.md)
  Executes a given Block using the indexes in the specified range, using the specified enumeration options.
- [func makeIterator() -> NSIndexSetIterator](./nsindexset/makeiterator%28%29.md)
  Returns an *iterator* over the elements of this *sequence*.
- [struct NSIndexSetIterator](./nsindexsetiterator.md)
  An iterator suitable for enumerating the elements of an index set.
### Initializers
- [init?(coder: NSCoder)](./nsindexset/init%28coder%29.md)
- [init(indexesInRange: NSRange)](./nsindexset/init%28indexesinrange%29-67dvw.md)
- [convenience init(indexesInRange: NSRange)](./nsindexset/init%28indexesinrange%29-n2eh.md)
### Default Implementations
- [Sequence Implementations](./nsindexset/sequence-implementations.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [NSMutableIndexSet](./nsmutableindexset.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](./nscoding.md)
- [NSCopying](./nscopying.md)
- [NSMutableCopying](./nsmutablecopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](./nssecurecoding.md)
- [Sequence](../Swift/sequence.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsindexset)*