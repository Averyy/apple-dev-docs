# index(options:passingTest:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (NSUInteger) indexWithOptions:(NSEnumerationOptions) opts passingTest:(BOOL (^)(NSUInteger idx, BOOL *stop)) predicate;
```

#### Return Value

The index of the first object that passes the predicate test.

## Parameters

- `opts`: A bitmask that specifies the options for the enumeration (whether it should be performed concurrently and whether it should be performed in reverse order). See [`NSEnumerationOptions`](../nsenumerationoptions.md) for the supported values.
- `predicate`: The Block to apply to elements in the set.

  The Block takes two arguments:

  - **idx**: The index of the object.
  - **stop**: A reference to a Boolean value. The block can set the value to [`true`](../../Swift/true.md) to stop further processing of the set. The `stop` argument is an out-only argument. You should only ever set this Boolean to YES within the Block.

  The Block returns a Boolean value that indicates whether `obj` passed the test.

## See Also

### Querying Index Sets
- [func contains(Int) -> Bool](./contains%28_%29-bb19.md)
  Indicates whether the index set contains a specific index.
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
- [func indexes(options: NSEnumerationOptions, passingTest: (Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> IndexSet](./indexes%28options,passingtest%29.md)
  Returns an `NSIndexSet` containing the receiving index set’s objects that pass the Block test using the specified enumeration options.
- [func index(in: NSRange, options: NSEnumerationOptions, passingTest: (Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int](./index%28in,options,passingtest%29.md)
  Returns the index of the first object in the specified range that passes the predicate Block test.
- [func indexes(in: NSRange, options: NSEnumerationOptions, passingTest: (Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> IndexSet](./indexes%28in,options,passingtest%29.md)
  Returns an `NSIndexSet` containing the receiving index set’s objects in the specified range that pass the Block test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsindexset/index(options:passingtest:))*