# objectEnumerator()

**Framework**: Foundation  
**Kind**: method

Returns an enumerator object that lets you access each object in the ordered set.

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
func objectEnumerator() -> NSEnumerator
```

#### Return Value

An enumerator object that lets you access each object in the ordered set, in order, from the element at the lowest index upwards.

#### Discussion

When you use this method with mutable subclasses of `NSOrderedSet`, you must not modify the ordered set during enumeration.

It is more efficient to use the fast enumeration protocol (see [`NSFastEnumeration`](nsfastenumeration.md)). Fast enumeration is available in macOS 10.5 and later and iOS 2.0 and later.

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
- [subscript(Int) -> Any](nsorderedset/subscript(_:).md)
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
- [func indexes(ofObjectsAt: IndexSet, options: NSEnumerationOptions, passingTest: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> IndexSet](nsorderedset/indexes(ofobjectsat:options:passingtest:).md)
  Returns the index, from a given set of indexes, of the object in the ordered set that passes a test in a given block for a given set of enumeration options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsorderedset/objectenumerator())*