# objects(at:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns the objects in the ordered set at the specified indexes.

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
func objects(at indexes: IndexSet) -> [Any]
```

```objc
- (NSArray<id> *) objectsAtIndexes:(NSIndexSet *) indexes;
```

## Return Value

The returned objects are in the ascending order of their indexes in indexes, so that object in returned ordered set with higher index in indexes will follow the object with smaller index in indexes.

## Discussion

Raises an [`rangeException`](../nsexceptionname/rangeexception.md) if any location in indexes exceeds the bounds of the array, of if `indexes` is `nil`.

## Parameters

- `indexes`: The indexes.

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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsorderedset/objects(at:))*