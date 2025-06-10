# contains(_:)

**Framework**: Foundation  
**Kind**: method

Returns a Boolean value that indicates whether a given object is present in the array.

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
func contains(_ anObject: Any) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if `anObject` is present in the array, otherwise [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

Starting at index `0`, each element of the array is checked for equality with `anObject` until a match is found or the end of the array is reached.  Objects are considered equal if [`isEqual(_:)`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol/isEqual(_:)) returns [`true`](https://developer.apple.com/documentation/swift/true).

To determine if the array contains a particular instance of an object, you can test for identity rather than equality by calling the [`indexOfObjectIdentical(to:)`](nsarray/indexofobjectidentical(to:).md) method and comparing the return value to [`NSNotFound`](nsnotfound-9t5v2.md).

## Parameters

- `anObject`: An object to look for in the array.

## See Also

- [func indexOfObjectIdentical(to: Any) -> Int](nsarray/indexofobjectidentical(to:).md)
  Returns the lowest index whose corresponding array value is identical to a given object.
- [func index(of: Any) -> Int](nsarray/index(of:).md)
  Returns the lowest index whose corresponding array value is equal to a given object.
- [var count: Int](nsarray/count.md)
  The number of objects in the array.
- [var firstObject: Any?](nsarray/firstobject.md)
  The first object in the array.
- [var lastObject: Any?](nsarray/lastobject.md)
  The last object in the array.
- [func object(at: Int) -> Any](nsarray/object(at:).md)
  Returns the object located at the specified index.
- [subscript(Int) -> Any](nsarray/subscript(_:).md)
  Returns the object at the specified index.
- [func objects(at: IndexSet) -> [Any]](nsarray/objects(at:).md)
  Returns an array containing the objects in the array at the indexes specified by a given index set.
- [func objectEnumerator() -> NSEnumerator](nsarray/objectenumerator.md)
  Returns an enumerator object that lets you access each object in the array.
- [func reverseObjectEnumerator() -> NSEnumerator](nsarray/reverseobjectenumerator.md)
  Returns an enumerator object that lets you access each object in the array, in reverse order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarray/contains(_:))*