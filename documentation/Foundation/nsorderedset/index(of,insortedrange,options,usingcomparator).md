# index(of:inSortedRange:options:usingComparator:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns the index, within a specified range, of an object compared with elements in the ordered set using a given NSComparator block.

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
func index(of object: Any, inSortedRange range: NSRange, options opts: NSBinarySearchingOptions = [], usingComparator cmp: (Any, Any) -> ComparisonResult) -> Int
```

```objc
- (NSUInteger) indexOfObject:(ObjectType) object inSortedRange:(NSRange) range options:(NSBinarySearchingOptions) opts usingComparator:(NSComparator) cmp;
```

#### Return Value

If the [`insertionIndex`](../nsbinarysearchingoptions/insertionindex.md) option is not specified:

- If the `object` is found and neither [`firstEqual`](../nsbinarysearchingoptions/firstequal.md) nor [`lastEqual`](../nsbinarysearchingoptions/lastequal.md) is specified, returns the matching object’s index.
- If the [`firstEqual`](../nsbinarysearchingoptions/firstequal.md) or [`lastEqual`](../nsbinarysearchingoptions/lastequal.md) option is also specified, returns the index of equal objects.
- If the object is not found, returns `NSNotFound`.

If the [`insertionIndex`](../nsbinarysearchingoptions/insertionindex.md) option is specified, returns the index at which you should insert `obj` in order to maintain a sorted array:

- If the `object` is found and neither [`firstEqual`](../nsbinarysearchingoptions/firstequal.md) nor [`lastEqual`](../nsbinarysearchingoptions/lastequal.md) is specified, returns the matching object’s index.
- If the [`firstEqual`](../nsbinarysearchingoptions/firstequal.md) or  [`lastEqual`](../nsbinarysearchingoptions/lastequal.md) option is also specified, returns the index of the equal objects.
- If the object is not found, returns the index of the least greater object, or the index at the end of the array if the object is larger than all other elements.

#### Discussion

The elements in the ordered set  must have already been sorted using the comparator `cmp`. If the ordered set is not sorted, the result is undefined.

## Parameters

- `object`: An object for which to search in the ordered set.

  If this value is `nil`, throws an [`invalidArgumentException`](../nsexceptionname/invalidargumentexception.md).
- `range`: The range within the array to search for `object`.

  If r exceeds the bounds of the ordered set (if the location plus length of the range is greater than the count of the ordered set), throws an [`rangeException`](../nsexceptionname/rangeexception.md).
- `opts`: Options for the search. For possible values, see [`NSBinarySearchingOptions`](../nsbinarysearchingoptions.md).
- `cmp`: A comparator block used to compare the object obj with elements in the ordered set.

  If this value is `NULL`, throws an [`invalidArgumentException`](../nsexceptionname/invalidargumentexception.md).

## See Also

### Accessing Set Members
- [func contains(Any) -> Bool](./contains%28_%29.md)
  Returns a Boolean value that indicates whether a given object is present in the ordered set.
- [func enumerateObjects(at: IndexSet, options: NSEnumerationOptions, using: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Void)](./enumerateobjects%28at,options,using%29.md)
  Executes a given block using the objects in the ordered set at the specified indexes.
- [func enumerateObjects((Any, Int, UnsafeMutablePointer<ObjCBool>) -> Void)](./enumerateobjects%28_%29.md)
  Executes a given block using each object in the ordered set.
- [func enumerateObjects(options: NSEnumerationOptions, using: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Void)](./enumerateobjects%28options,using%29.md)
  Executes a given block using each object in the set, using the specified enumeration options.
- [var firstObject: Any?](./firstobject.md)
  The first object in the ordered set.
- [var lastObject: Any?](./lastobject.md)
  The last object in the ordered set.
- [func object(at: Int) -> Any](./object%28at%29.md)
  Returns the object at the specified index of the set.
- [subscript(Int) -> Any](./subscript%28_%29.md)
  Returns the object at the specified index of the set.
- [func objects(at: IndexSet) -> [Any]](./objects%28at%29.md)
  Returns the objects in the ordered set at the specified indexes.
- [func index(of: Any) -> Int](./index%28of%29.md)
  Returns the index of the specified object.
- [func index(ofObjectAt: IndexSet, options: NSEnumerationOptions, passingTest: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int](./index%28ofobjectat,options,passingtest%29.md)
  Returns the index, from a given set of indexes, of the object in the ordered set that passes a test in a given block for a given set of enumeration options.
- [func index(ofObjectPassingTest: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int](./index%28ofobjectpassingtest%29.md)
  Returns the index of the object in the ordered set that passes a test in a given block.
- [func index(NSEnumerationOptions, ofObjectPassingTest: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int](./index%28_,ofobjectpassingtest%29.md)
  Returns the index of an object in the ordered set that passes a test in a given block for a given set of enumeration options.
- [func indexes(ofObjectsAt: IndexSet, options: NSEnumerationOptions, passingTest: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> IndexSet](./indexes%28ofobjectsat,options,passingtest%29.md)
  Returns the index, from a given set of indexes, of the object in the ordered set that passes a test in a given block for a given set of enumeration options.
- [func indexes(ofObjectsPassingTest: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> IndexSet](./indexes%28ofobjectspassingtest%29.md)
  Returns the index of the object in the ordered set that passes a test in a given block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsorderedset/index(of:insortedrange:options:usingcomparator:))*