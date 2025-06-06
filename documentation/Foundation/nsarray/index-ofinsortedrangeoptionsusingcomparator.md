# index(of:inSortedRange:options:usingComparator:)

**Framework**: Foundation  
**Kind**: method

Returns the index, within a specified range, of an object compared with elements in the array using a given `NSComparator` block.

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
func index(of obj: Any, inSortedRange r: NSRange, options opts: NSBinarySearchingOptions = [], usingComparator cmp: (Any, Any) -> ComparisonResult) -> Int
```

#### Return Value

If the [`insertionIndex`](nsbinarysearchingoptions/insertionindex.md) option is not specified:

- If the `obj` is found and neither [`firstEqual`](nsbinarysearchingoptions/firstequal.md) nor [`lastEqual`](nsbinarysearchingoptions/lastequal.md) is specified, returns an arbitrary matching object’s index.
- If the [`firstEqual`](nsbinarysearchingoptions/firstequal.md) option is also specified, returns the lowest index of equal objects.
- If the [`lastEqual`](nsbinarysearchingoptions/lastequal.md) option is also specified, returns the highest index of equal objects.
- If the object is not found, returns `NSNotFound`.

If the [`insertionIndex`](nsbinarysearchingoptions/insertionindex.md) option is specified, returns the index at which you should insert `obj` in order to maintain a sorted array:

- If the `obj` is found and neither [`firstEqual`](nsbinarysearchingoptions/firstequal.md) nor [`lastEqual`](nsbinarysearchingoptions/lastequal.md) is specified, returns any equal or one larger index than any matching object’s index.
- If the [`firstEqual`](nsbinarysearchingoptions/firstequal.md) option is also specified, returns the lowest index of equal objects.
- If the [`lastEqual`](nsbinarysearchingoptions/lastequal.md) option is also specified, returns the highest index of equal objects.
- If the object is not found, returns the index of the least greater object, or the index at the end of the array if the object is larger than all other elements.

#### Discussion

The elements in the array must have already been sorted using the comparator `cmp`.  If the array is not sorted, the result is undefined.

## Parameters

- `obj`: If this value is  , throws an  .
- `r`: If   exceeds the bounds of the array (if the location plus length of the range is greater than the count of the array), throws an  .
- `opts`: If you specify both   and  , throws an  .
- `cmp`: If this value is  , throws an  .

## See Also

- [func index(of: Any) -> Int](nsarray/index(of:).md)
  Returns the lowest index whose corresponding array value is equal to a given object.
- [func index(of: Any, in: NSRange) -> Int](nsarray/index(of:in:).md)
  Returns the lowest index within a specified range whose corresponding array value is equal to a given object .
- [func indexOfObjectIdentical(to: Any) -> Int](nsarray/indexofobjectidentical(to:).md)
  Returns the lowest index whose corresponding array value is identical to a given object.
- [func indexOfObjectIdentical(to: Any, in: NSRange) -> Int](nsarray/indexofobjectidentical(to:in:).md)
  Returns the lowest index within a specified range whose corresponding array value is equal to a given object .
- [func indexOfObject(passingTest: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int](nsarray/indexofobject(passingtest:).md)
  Returns the index of the first object in the array that passes a test in a given block.
- [func indexOfObject(options: NSEnumerationOptions, passingTest: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int](nsarray/indexofobject(options:passingtest:).md)
  Returns the index of an object in the array that passes a test in a given block for a given set of enumeration options.
- [func indexOfObject(at: IndexSet, options: NSEnumerationOptions, passingTest: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int](nsarray/indexofobject(at:options:passingtest:).md)
  Returns the index, from a given set of indexes, of the first object in the array that passes a test in a given block for a given set of enumeration options.
- [func indexesOfObjects(passingTest: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> IndexSet](nsarray/indexesofobjects(passingtest:).md)
  Returns the indexes of objects in the array that pass a test in a given block.
- [func indexesOfObjects(options: NSEnumerationOptions, passingTest: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> IndexSet](nsarray/indexesofobjects(options:passingtest:).md)
  Returns the indexes of objects in the array that pass a test in a given block for a given set of enumeration options.
- [func indexesOfObjects(at: IndexSet, options: NSEnumerationOptions, passingTest: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> IndexSet](nsarray/indexesofobjects(at:options:passingtest:).md)
  Returns the indexes, from a given set of indexes, of objects in the array that pass a test in a given block for a given set of enumeration options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarray/index(of:insortedrange:options:usingcomparator:))*