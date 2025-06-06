# indexes(ofObjectsAt:options:passingTest:)

**Framework**: Foundation  
**Kind**: method

Returns the index, from a given set of indexes, of the object in the ordered set that passes a test in a given block for a given set of enumeration options.

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
func indexes(ofObjectsAt s: IndexSet, options opts: NSEnumerationOptions = [], passingTest predicate: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> IndexSet
```

#### Return Value

The index of the corresponding value in the ordered set that passes the test specified by predicate. If no objects in the ordered set pass the test, returns NSNotFound.

#### Discussion

By default, the enumeration starts with the first object and continues serially through the ordered set to the last object. You can specify [`concurrent`](nsenumerationoptions/concurrent.md) and/or [`reverse`](nsenumerationoptions/reverse.md) as enumeration options to modify this behavior.

> ❗ **Important**:  If the block parameter or `s` is `nil` this method will raise an exception.

 If the block parameter or `s` is `nil` this method will raise an exception.

## Parameters

- `s`: The indexes of the objects over which to enumerate.
- `opts`: A bitmask that specifies the options for the enumeration (whether it should be performed concurrently and whether it should be performed in reverse order).
- `predicate`: The block returns a Boolean value that indicates whether   passed the test.

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
- [func index(of: Any, inSortedRange: NSRange, options: NSBinarySearchingOptions, usingComparator: (Any, Any) -> ComparisonResult) -> Int](nsorderedset/index(of:insortedrange:options:usingcomparator:).md)
  Returns the index, within a specified range, of an object compared with elements in the ordered set using a given NSComparator block.
- [func index(ofObjectAt: IndexSet, options: NSEnumerationOptions, passingTest: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int](nsorderedset/index(ofobjectat:options:passingtest:).md)
  Returns the index, from a given set of indexes, of the object in the ordered set that passes a test in a given block for a given set of enumeration options.
- [func index(ofObjectPassingTest: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int](nsorderedset/index(ofobjectpassingtest:).md)
  Returns the index of the object in the ordered set that passes a test in a given block.
- [func index(NSEnumerationOptions, ofObjectPassingTest: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int](nsorderedset/index(_:ofobjectpassingtest:).md)
  Returns the index of an object in the ordered set that passes a test in a given block for a given set of enumeration options.
- [func indexes(ofObjectsPassingTest: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> IndexSet](nsorderedset/indexes(ofobjectspassingtest:).md)
  Returns the index of the object in the ordered set that passes a test in a given block.
- [func indexes(options: NSEnumerationOptions, ofObjectsPassingTest: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> IndexSet](nsorderedset/indexes(options:ofobjectspassingtest:).md)
  Returns the index of an object in the ordered set that passes a test in a given block for a given set of enumeration options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsorderedset/indexes(ofobjectsat:options:passingtest:))*