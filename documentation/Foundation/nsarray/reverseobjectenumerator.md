# reverseObjectEnumerator()

**Framework**: Foundation  
**Kind**: method

Returns an enumerator object that lets you access each object in the array, in reverse order.

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
func reverseObjectEnumerator() -> NSEnumerator
```

#### Return Value

An enumerator object that lets you access each object in the array, in order, from the element at the highest index down to the element at index `0`.

#### Discussion

When you use this method with mutable subclasses of `NSArray`, you must not modify the array during enumeration.

It is more efficient to use the fast enumeration protocol (see [`NSFastEnumeration`](nsfastenumeration.md)). Fast enumeration is available in macOS 10.5 and later and iOS 2.0 and later.

## See Also

- [func nextObject() -> Any?](nsenumerator/nextobject.md)
  Returns the next object from the collection being enumerated.
- [func contains(Any) -> Bool](nsarray/contains(_:).md)
  Returns a Boolean value that indicates whether a given object is present in the array.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarray/reverseobjectenumerator())*