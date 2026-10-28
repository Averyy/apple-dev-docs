# subscript(_:)

**Framework**: Foundation  
**Kind**: subscript  
**Role**: Instance Subscript

Returns the object at the specified index of the set.

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
subscript(idx: Int) -> Any { get }
```

```swift
subscript(idx: Int) -> Any { get set }
```

```objc
- (ObjectType) objectAtIndexedSubscript:(NSUInteger) idx;
```

## Return Value

If `idx` is beyond the end of the ordered set (that is, if index is greater than or equal to the value returned by count), an [`rangeException`](../nsexceptionname/rangeexception.md) is raised.

## Discussion

This method is the same as [`object(at:)`](./object%28at%29.md).

## Parameters

- `idx`: The object located at index.

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
- [func objects(at: IndexSet) -> [Any]](./objects%28at%29.md)
  Returns the objects in the ordered set at the specified indexes.
- [func index(of: Any) -> Int](./index%28of%29.md)
  Returns the index of the specified object.
- [func index(of: Any, inSortedRange: NSRange, options: NSBinarySearchingOptions, usingComparator: (Any, Any) -> ComparisonResult) -> Int](./index%28of,insortedrange,options,usingcomparator%29.md)
  Returns the index, within a specified range, of an object compared with elements in the ordered set using a given NSComparator block.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsorderedset/subscript(_:))*