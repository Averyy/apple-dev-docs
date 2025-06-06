# index(of:in:)

**Framework**: Foundation  
**Kind**: method

Returns the lowest index within a specified range whose corresponding array value is equal to a given object .

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
func index(of anObject: Any, in range: NSRange) -> Int
```

#### Return Value

The lowest index within `range` whose corresponding array value is equal to `anObject`. If none of the objects within `range` is equal to `anObject`, returns `NSNotFound`.

#### Discussion

Starting at `range.location`, each element of the array is passed as an argument to an [`isEqual(_:)`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol/isEqual(_:)) message sent to `anObject` until a match is found or the end of the `range` is reached. Objects are considered equal if [`isEqual(_:)`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol/isEqual(_:)) returns [`true`](https://developer.apple.com/documentation/swift/true).

This method raises an [`rangeException`](nsexceptionname/rangeexception.md) exception if the `range` parameter represents a range that doesn’t exist in the array.

## Parameters

- `anObject`: An object.
- `range`: The range of indexes in the array within which to search for  .

## See Also

- [func contains(Any) -> Bool](nsarray/contains(_:).md)
  Returns a Boolean value that indicates whether a given object is present in the array.
- [func index(of: Any) -> Int](nsarray/index(of:).md)
  Returns the lowest index whose corresponding array value is equal to a given object.
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
- [func index(of: Any, inSortedRange: NSRange, options: NSBinarySearchingOptions, usingComparator: (Any, Any) -> ComparisonResult) -> Int](nsarray/index(of:insortedrange:options:usingcomparator:).md)
  Returns the index, within a specified range, of an object compared with elements in the array using a given `NSComparator` block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarray/index(of:in:))*