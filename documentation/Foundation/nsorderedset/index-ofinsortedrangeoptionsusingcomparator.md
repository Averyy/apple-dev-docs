# index(of:inSortedRange:options:usingComparator:)

**Framework**: Foundation  
**Kind**: method

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

#### Return Value

If the [`insertionIndex`](nsbinarysearchingoptions/insertionindex.md) option is not specified:

- If the `object` is found and neither [`firstEqual`](nsbinarysearchingoptions/firstequal.md) nor [`lastEqual`](nsbinarysearchingoptions/lastequal.md) is specified, returns the matching object’s index.
- If the [`firstEqual`](nsbinarysearchingoptions/firstequal.md) or [`lastEqual`](nsbinarysearchingoptions/lastequal.md) option is also specified, returns the index of equal objects.
- If the object is not found, returns `NSNotFound`.

If the [`insertionIndex`](nsbinarysearchingoptions/insertionindex.md) option is specified, returns the index at which you should insert `obj` in order to maintain a sorted array:

- If the `object` is found and neither [`firstEqual`](nsbinarysearchingoptions/firstequal.md) nor [`lastEqual`](nsbinarysearchingoptions/lastequal.md) is specified, returns the matching object’s index.
- If the [`firstEqual`](nsbinarysearchingoptions/firstequal.md) or  [`lastEqual`](nsbinarysearchingoptions/lastequal.md) option is also specified, returns the index of the equal objects.
- If the object is not found, returns the index of the least greater object, or the index at the end of the array if the object is larger than all other elements.

#### Discussion

The elements in the ordered set  must have already been sorted using the comparator `cmp`. If the ordered set is not sorted, the result is undefined.

## Parameters

- `object`: If this value is  , throws an  .
- `range`: If r exceeds the bounds of the ordered set (if the location plus length of the range is greater than the count of the ordered set), throws an  .
- `opts`: Options for the search. For possible values, see  .
- `cmp`: If this value is  , throws an  .

## See Also

- [func contains(Any) -> Bool](nsorderedset/contains(_:).md)
  Returns a Boolean value that indicates whether a given object is present in the ordered set.
- [func enumerateObjects(at: IndexSet, options: NSEnumerationOptions, using: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Void)](nsorderedset/enumerateobjects(at:options:using:).md)
  Executes a given block using the objects in the ordered set at the specified indexes.
- [func enumerateObjects((Any, Int, UnsafeMutablePointer<ObjCBool>) -> Void)](nsorderedset/enumerateobjects(_:).md)
  Executes a given block using each object in the ordered set.
- [func enumerateObjects(options: NSEnumerationOptions, using: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Void)](nsorderedset/enumerateobjects(options:using:).md)
  Executes a given block using each object in the set, using the specified enumeration options.
- [var firstObject: Any?](nsorderedset/firstobject.md)
  The first object in the ordered set.
- [var lastObject: Any?](nsorderedset/lastobject.md)
  The last object in the ordered set.
- [func object(at: Int) -> Any](nsorderedset/object(at:).md)
  Returns the object at the specified index of the set.
- [func objects(at: IndexSet) -> [Any]](nsorderedset/objects(at:).md)
  Returns the objects in the ordered set at the specified indexes.
- [func index(of: Any) -> Int](nsorderedset/index(of:).md)
  Returns the index of the specified object.
- [func index(ofObjectAt: IndexSet, options: NSEnumerationOptions, passingTest: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int](nsorderedset/index(ofobjectat:options:passingtest:).md)
  Returns the index, from a given set of indexes, of the object in the ordered set that passes a test in a given block for a given set of enumeration options.
- [func index(ofObjectPassingTest: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int](nsorderedset/index(ofobjectpassingtest:).md)
  Returns the index of the object in the ordered set that passes a test in a given block.
- [func index(NSEnumerationOptions, ofObjectPassingTest: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int](nsorderedset/index(_:ofobjectpassingtest:).md)
  Returns the index of an object in the ordered set that passes a test in a given block for a given set of enumeration options.
- [func indexes(ofObjectsAt: IndexSet, options: NSEnumerationOptions, passingTest: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> IndexSet](nsorderedset/indexes(ofobjectsat:options:passingtest:).md)
  Returns the index, from a given set of indexes, of the object in the ordered set that passes a test in a given block for a given set of enumeration options.
- [func indexes(ofObjectsPassingTest: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> IndexSet](nsorderedset/indexes(ofobjectspassingtest:).md)
  Returns the index of the object in the ordered set that passes a test in a given block.
- [func indexes(options: NSEnumerationOptions, ofObjectsPassingTest: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> IndexSet](nsorderedset/indexes(options:ofobjectspassingtest:).md)
  Returns the index of an object in the ordered set that passes a test in a given block for a given set of enumeration options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsorderedset/index(of:insortedrange:options:usingcomparator:))*