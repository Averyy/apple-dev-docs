# contains(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (BOOL) containsIndex:(NSUInteger) value;
```

#### Return Value

[`true`](../../Swift/true.md) when the index set contains `index`, [`false`](../../Swift/false.md) otherwise.

## Parameters

- `value`: Index being inquired about.

## See Also

### Querying Index Sets
- [func contains(IndexSet) -> Bool](./contains%28_%29-5j2kh.md)
  Indicates whether the receiving index set contains a superset of the indexes in another index set.
- [func contains(in: NSRange) -> Bool](./contains%28in%29.md)
  Indicates whether the index set contains the indexes represented by an index range.
- [func intersects(in: NSRange) -> Bool](./intersects%28in%29.md)
  Indicates whether the index set contains any of the indexes in a range.
- [var count: Int](./count.md)
  The number of indexes in the index set.
- [func countOfIndexes(in: NSRange) -> Int](./countofindexes%28in%29.md)
  Returns the number of indexes in the index set that are members of a given range.
- [func index(passingTest: (Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int](./index%28passingtest%29.md)
  Returns the index of the first object that passes the predicate Block test.
- [func indexes(passingTest: (Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> IndexSet](./indexes%28passingtest%29.md)
  Returns an `NSIndexSet` containing the receiving index set’s objects that pass the Block test.
- [func index(options: NSEnumerationOptions, passingTest: (Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int](./index%28options,passingtest%29.md)
  Returns the index of the first object that passes the predicate Block test using the specified enumeration options.
- [func indexes(options: NSEnumerationOptions, passingTest: (Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> IndexSet](./indexes%28options,passingtest%29.md)
  Returns an `NSIndexSet` containing the receiving index set’s objects that pass the Block test using the specified enumeration options.
- [func index(in: NSRange, options: NSEnumerationOptions, passingTest: (Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int](./index%28in,options,passingtest%29.md)
  Returns the index of the first object in the specified range that passes the predicate Block test.
- [func indexes(in: NSRange, options: NSEnumerationOptions, passingTest: (Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> IndexSet](./indexes%28in,options,passingtest%29.md)
  Returns an `NSIndexSet` containing the receiving index set’s objects in the specified range that pass the Block test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsindexset/contains(_:)-bb19)*