# NSIndexSet

**Framework**: Foundation  
**Kind**: class

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

## Mentions

- [init](1807255-init.md)

#### Overview

In Swift, this type bridges to [`IndexSet`](indexset.md); use [`NSIndexSet`](nsindexset.md) when you need reference semantics or other Foundation-specific behavior.

The `NSIndexSet` class represents an immutable collection of unique unsigned integers, known as  because of the way they are used. This collection is referred to as an . Indexes must be in the range `0 .. NSNotFound - 1`.

You use index sets in your code to store indexes into some other data structure. For example, given an `NSArray` object, you could use an index set to identify a subset of objects in that array.

You should not use index sets to store an arbitrary collection of integer values because index sets store indexes as sorted ranges. This makes them more efficient than storing a collection of individual integers. It also means that each index value can only appear once in the index set.

The designated initializers of the `NSIndexSet` class are: [`init(index:)`](nsindexset/init(index:).md), [`init(indexesIn:)`](nsindexset/init(indexesin:).md), and [`init(indexSet:)`](nsindexset/init(indexset:).md).

You must not subclass the `NSIndexSet` class.

The mutable subclass of `NSIndexSet` is [`NSMutableIndexSet`](nsmutableindexset.md).

> ❗ **Important**:  The Swift overlay to the Foundation framework provides the [`IndexSet`](indexset.md) structure, which bridges to the [`NSIndexSet`](nsindexset.md) class and its mutable subclass, [`NSMutableIndexSet`](nsmutableindexset.md). For more information about value types, see [`Working with Cocoa Frameworks`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Swift/Conceptual/BuildingCocoaApps/WorkingWithCocoaDataTypes.html#//apple_ref/doc/uid/TP40014216-CH6) in [`Using Swift with Cocoa and Objective-C (Swift 4.1)`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Swift/Conceptual/BuildingCocoaApps/index.html#//apple_ref/doc/uid/TP40014216).

 The Swift overlay to the Foundation framework provides the [`IndexSet`](indexset.md) structure, which bridges to the [`NSIndexSet`](nsindexset.md) class and its mutable subclass, [`NSMutableIndexSet`](nsmutableindexset.md). For more information about value types, see [`Working with Cocoa Frameworks`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Swift/Conceptual/BuildingCocoaApps/WorkingWithCocoaDataTypes.html#//apple_ref/doc/uid/TP40014216-CH6) in [`Using Swift with Cocoa and Objective-C (Swift 4.1)`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Swift/Conceptual/BuildingCocoaApps/index.html#//apple_ref/doc/uid/TP40014216).

## Topics

### Creating Index Sets
- [convenience init(index: Int)](nsindexset/init(index:).md)
  Initializes an allocated [`NSIndexSet`](nsindexset.md) object with an index.
- [init(indexesIn: NSRange)](nsindexset/init(indexesin:).md)
  Initializes an allocated [`NSIndexSet`](nsindexset.md) object with an index range.
- [init(indexSet: IndexSet)](nsindexset/init(indexset:).md)
  Initializes an allocated [`NSIndexSet`](nsindexset.md) object with an index set.
### Querying Index Sets
- [func contains(Int) -> Bool](nsindexset/contains(_:)-bb19.md)
  Indicates whether the index set contains a specific index.
- [func contains(IndexSet) -> Bool](nsindexset/contains(_:)-5j2kh.md)
  Indicates whether the receiving index set contains a superset of the indexes in another index set.
- [func contains(in: NSRange) -> Bool](nsindexset/contains(in:).md)
  Indicates whether the index set contains the indexes represented by an index range.
- [func intersects(in: NSRange) -> Bool](nsindexset/intersects(in:).md)
  Indicates whether the index set contains any of the indexes in a range.
- [var count: Int](nsindexset/count.md)
  The number of indexes in the index set.
- [func countOfIndexes(in: NSRange) -> Int](nsindexset/countofindexes(in:).md)
  Returns the number of indexes in the index set that are members of a given range.
- [func index(passingTest: (Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int](nsindexset/index(passingtest:).md)
  Returns the index of the first object that passes the predicate Block test.
- [func indexes(passingTest: (Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> IndexSet](nsindexset/indexes(passingtest:).md)
  Returns an `NSIndexSet` containing the receiving index set’s objects that pass the Block test.
- [func index(options: NSEnumerationOptions, passingTest: (Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int](nsindexset/index(options:passingtest:).md)
  Returns the index of the first object that passes the predicate Block test using the specified enumeration options.
- [func indexes(options: NSEnumerationOptions, passingTest: (Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> IndexSet](nsindexset/indexes(options:passingtest:).md)
  Returns an `NSIndexSet` containing the receiving index set’s objects that pass the Block test using the specified enumeration options.
- [func index(in: NSRange, options: NSEnumerationOptions, passingTest: (Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int](nsindexset/index(in:options:passingtest:).md)
  Returns the index of the first object in the specified range that passes the predicate Block test.
- [func indexes(in: NSRange, options: NSEnumerationOptions, passingTest: (Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> IndexSet](nsindexset/indexes(in:options:passingtest:).md)
  Returns an `NSIndexSet` containing the receiving index set’s objects in the specified range that pass the Block test.
### Enumerating Index Set Content
- [func enumerateRanges(in: NSRange, options: NSEnumerationOptions, using: (NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)](nsindexset/enumerateranges(in:options:using:).md)
  Enumerates over the ranges in the range of objects using the block
- [func enumerateRanges((NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)](nsindexset/enumerateranges(_:).md)
  Executes a given block using each object in the index set, in the specified ranges.
- [func enumerateRanges(options: NSEnumerationOptions, using: (NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)](nsindexset/enumerateranges(options:using:).md)
  Executes a given block using each object in the index set, in the specified ranges.
### Comparing Index Sets
- [func isEqual(to: IndexSet) -> Bool](nsindexset/isequal(to:).md)
  Indicates whether the indexes in the receiving index set are the same indexes contained in another index set.
### Getting Indexes
- [var firstIndex: Int](nsindexset/firstindex.md)
  The first index in the index set.
- [var lastIndex: Int](nsindexset/lastindex.md)
  The last index in the index set.
- [func indexLessThanIndex(Int) -> Int](nsindexset/indexlessthanindex(_:).md)
  Returns either the closest index in the index set that is less than a specific index or the not-found indicator.
- [func indexLessThanOrEqual(to: Int) -> Int](nsindexset/indexlessthanorequal(to:).md)
  Returns either the closest index in the index set that is less than or equal to a specific index or the not-found indicator.
- [func indexGreaterThanOrEqual(to: Int) -> Int](nsindexset/indexgreaterthanorequal(to:).md)
  Returns either the closest index in the index set that is greater than or equal to a specific index or the not-found indicator.
- [func indexGreaterThanIndex(Int) -> Int](nsindexset/indexgreaterthanindex(_:).md)
  Returns either the closest index in the index set that is greater than a specific index or the not-found indicator.
- [func getIndexes(UnsafeMutablePointer<Int>, maxCount: Int, inIndexRange: NSRangePointer?) -> Int](nsindexset/getindexes(_:maxcount:inindexrange:).md)
  The index set fills an index buffer with the indexes contained both in the index set and in an index range, returning the number of indexes copied.
### Enumerating Indexes
- [func enumerate((Int, UnsafeMutablePointer<ObjCBool>) -> Void)](nsindexset/enumerate(_:).md)
  Executes a given Block using each object in the index set.
- [func enumerate(options: NSEnumerationOptions, using: (Int, UnsafeMutablePointer<ObjCBool>) -> Void)](nsindexset/enumerate(options:using:).md)
  Executes a given Block over the index set’s indexes, using the specified enumeration options.
- [func enumerate(in: NSRange, options: NSEnumerationOptions, using: (Int, UnsafeMutablePointer<ObjCBool>) -> Void)](nsindexset/enumerate(in:options:using:).md)
  Executes a given Block using the indexes in the specified range, using the specified enumeration options.
- [func makeIterator() -> NSIndexSetIterator](nsindexset/makeiterator.md)
  Returns an  over the elements of this .
- [struct NSIndexSetIterator](nsindexsetiterator.md)
  An iterator suitable for enumerating the elements of an index set.
### Default Implementations
- [Sequence Implementations](nsindexset/sequence-implementations.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [NSMutableIndexSet](nsmutableindexset.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsindexset)*