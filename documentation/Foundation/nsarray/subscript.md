# subscript(_:)

**Framework**: Foundation  
**Kind**: subscript

Returns the object at the specified index.

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
subscript(idx: Int) -> Any { get set }
```

#### Return Value

The object located at `idx`.

#### Discussion

This method has the same behavior as the [`object(at:)`](nsarray/object(at:).md) method.

If `idx` is beyond the end of the array (that is, if `idx` is greater than or equal to the value returned by `count`), an [`rangeException`](nsexceptionname/rangeexception.md) is raised.

You shouldn’t need to call this method directly. Instead, this method is called when accessing an object by index using subscripting.

```objc
id value = array[3]; // equivalent to [array objectAtIndex:3]
```

## Parameters

- `idx`: An index within the bounds of the array.

## See Also

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
- [func objects(at: IndexSet) -> [Any]](nsarray/objects(at:).md)
  Returns an array containing the objects in the array at the indexes specified by a given index set.
- [func objectEnumerator() -> NSEnumerator](nsarray/objectenumerator.md)
  Returns an enumerator object that lets you access each object in the array.
- [func reverseObjectEnumerator() -> NSEnumerator](nsarray/reverseobjectenumerator.md)
  Returns an enumerator object that lets you access each object in the array, in reverse order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarray/subscript(_:))*