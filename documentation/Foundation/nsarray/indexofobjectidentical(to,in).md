# indexOfObjectIdentical(to:in:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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
func indexOfObjectIdentical(to anObject: Any, in range: NSRange) -> Int
```

```objc
- (NSUInteger) indexOfObjectIdenticalTo:(ObjectType) anObject inRange:(NSRange) range;
```

#### Return Value

The lowest index within `range` whose corresponding array value is identical to `anObject`. If none of the objects within `range` is identical to `anObject`, returns `NSNotFound`.

#### Discussion

Objects are considered identical if their object addresses are the same.

## Parameters

- `anObject`: An object.
- `range`: The range of indexes in the array within which to search for `anObject`.

## See Also

### Related Documentation
- [func contains(Any) -> Bool](./contains%28_%29.md)
  Returns a Boolean value that indicates whether a given object is present in the array.
### Finding Objects in an Array
- [func index(of: Any) -> Int](./index%28of%29.md)
  Returns the lowest index whose corresponding array value is equal to a given object.
- [func index(of: Any, in: NSRange) -> Int](./index%28of,in%29.md)
  Returns the lowest index within a specified range whose corresponding array value is equal to a given object .
- [func indexOfObjectIdentical(to: Any) -> Int](./indexofobjectidentical%28to%29.md)
  Returns the lowest index whose corresponding array value is identical to a given object.
- [func indexOfObject(passingTest: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int](./indexofobject%28passingtest%29.md)
  Returns the index of the first object in the array that passes a test in a given block.
- [func indexOfObject(options: NSEnumerationOptions, passingTest: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int](./indexofobject%28options,passingtest%29.md)
  Returns the index of an object in the array that passes a test in a given block for a given set of enumeration options.
- [func indexOfObject(at: IndexSet, options: NSEnumerationOptions, passingTest: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int](./indexofobject%28at,options,passingtest%29.md)
  Returns the index, from a given set of indexes, of the first object in the array that passes a test in a given block for a given set of enumeration options.
- [func indexesOfObjects(passingTest: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> IndexSet](./indexesofobjects%28passingtest%29.md)
  Returns the indexes of objects in the array that pass a test in a given block.
- [func indexesOfObjects(options: NSEnumerationOptions, passingTest: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> IndexSet](./indexesofobjects%28options,passingtest%29.md)
  Returns the indexes of objects in the array that pass a test in a given block for a given set of enumeration options.
- [func indexesOfObjects(at: IndexSet, options: NSEnumerationOptions, passingTest: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> IndexSet](./indexesofobjects%28at,options,passingtest%29.md)
  Returns the indexes, from a given set of indexes, of objects in the array that pass a test in a given block for a given set of enumeration options.
- [func index(of: Any, inSortedRange: NSRange, options: NSBinarySearchingOptions, usingComparator: (Any, Any) -> ComparisonResult) -> Int](./index%28of,insortedrange,options,usingcomparator%29.md)
  Returns the index, within a specified range, of an object compared with elements in the array using a given `NSComparator` block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarray/indexofobjectidentical(to:in:))*