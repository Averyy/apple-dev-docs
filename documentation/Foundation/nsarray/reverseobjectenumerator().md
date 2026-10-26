# reverseObjectEnumerator()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (NSEnumerator<id> *) reverseObjectEnumerator;
```

#### Return Value

An enumerator object that lets you access each object in the array, in order, from the element at the highest index down to the element at index `0`.

#### Discussion

When you use this method with mutable subclasses of `NSArray`, you must not modify the array during enumeration.

It is more efficient to use the fast enumeration protocol (see [`NSFastEnumeration`](../nsfastenumeration.md)). Fast enumeration is available in macOS 10.5 and later and iOS 2.0 and later.

## See Also

### Related Documentation
- [func nextObject() -> Any?](../nsenumerator/nextobject%28%29.md)
  Returns the next object from the collection being enumerated.
### Querying an Array
- [func contains(Any) -> Bool](./contains%28_%29.md)
  Returns a Boolean value that indicates whether a given object is present in the array.
- [var count: Int](./count.md)
  The number of objects in the array.
- [var firstObject: Any?](./firstobject.md)
  The first object in the array.
- [var lastObject: Any?](./lastobject.md)
  The last object in the array.
- [func object(at: Int) -> Any](./object%28at%29.md)
  Returns the object located at the specified index.
- [subscript(Int) -> Any](./subscript%28_%29.md)
  Returns the object at the specified index.
- [func objects(at: IndexSet) -> [Any]](./objects%28at%29.md)
  Returns an array containing the objects in the array at the indexes specified by a given index set.
- [func objectEnumerator() -> NSEnumerator](./objectenumerator%28%29.md)
  Returns an enumerator object that lets you access each object in the array.
- [- getObjects:](./getobjects_.md)
  Copies all the objects contained in the array to `aBuffer`.
- [- getObjects:range:](./getobjects_range_.md)
  Copies references to objects contained in the array that fall within the specified range to `aBuffer`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarray/reverseobjectenumerator())*