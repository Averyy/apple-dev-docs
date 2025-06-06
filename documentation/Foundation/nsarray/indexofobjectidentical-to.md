# indexOfObjectIdentical(to:)

**Framework**: Foundation  
**Kind**: method

Returns the lowest index whose corresponding array value is identical to a given object.

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
func indexOfObjectIdentical(to anObject: Any) -> Int
```

#### Return Value

The lowest index whose corresponding array value is identical to `anObject`. If none of the objects in the array is identical to `anObject`, returns `NSNotFound`.

#### Discussion

Objects are considered identical if their object addresses are the same.

## Parameters

- `anObject`: An object.

## See Also

- [func contains(Any) -> Bool](nsarray/contains(_:).md)
  Returns a Boolean value that indicates whether a given object is present in the array.
- [func index(of: Any) -> Int](nsarray/index(of:).md)
  Returns the lowest index whose corresponding array value is equal to a given object.
- [func index(of: Any, in: NSRange) -> Int](nsarray/index(of:in:).md)
  Returns the lowest index within a specified range whose corresponding array value is equal to a given object .
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
- [func index(of: Any, inSortedRange: NSRange, options: NSBinarySearchingOptions, usingComparator: (Any, Any) -> ComparisonResult) -> Int](nsarray/index(of:insortedrange:options:usingcomparator:).md)
  Returns the index, within a specified range, of an object compared with elements in the array using a given `NSComparator` block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarray/indexofobjectidentical(to:))*