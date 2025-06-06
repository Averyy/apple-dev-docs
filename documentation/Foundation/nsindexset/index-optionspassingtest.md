# index(options:passingTest:)

**Framework**: Foundation  
**Kind**: method

Returns the index of the first object that passes the predicate Block test using the specified enumeration options.

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
func index(options opts: NSEnumerationOptions = [], passingTest predicate: (Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int
```

#### Return Value

The index of the first object that passes the predicate test.

## Parameters

- `opts`: A bitmask that specifies the options for the enumeration (whether it should be performed concurrently and whether it should be performed in reverse order). See   for the supported values.
- `predicate`: The Block returns a Boolean value that indicates whether   passed the test.

## See Also

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
- [func indexes(options: NSEnumerationOptions, passingTest: (Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> IndexSet](nsindexset/indexes(options:passingtest:).md)
  Returns an `NSIndexSet` containing the receiving index set’s objects that pass the Block test using the specified enumeration options.
- [func index(in: NSRange, options: NSEnumerationOptions, passingTest: (Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int](nsindexset/index(in:options:passingtest:).md)
  Returns the index of the first object in the specified range that passes the predicate Block test.
- [func indexes(in: NSRange, options: NSEnumerationOptions, passingTest: (Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> IndexSet](nsindexset/indexes(in:options:passingtest:).md)
  Returns an `NSIndexSet` containing the receiving index set’s objects in the specified range that pass the Block test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsindexset/index(options:passingtest:))*