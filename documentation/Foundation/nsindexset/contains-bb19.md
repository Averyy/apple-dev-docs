# contains(_:)

**Framework**: Foundation  
**Kind**: method

Indicates whether the index set contains a specific index.

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
func contains(_ value: Int) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) when the index set contains `index`, [`false`](https://developer.apple.com/documentation/Swift/false) otherwise.

## Parameters

- `value`: Index being inquired about.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsindexset/contains(_:)-bb19)*