# object(at:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns the object located at the specified index.

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
func object(at index: Int) -> Any
```

```objc
- (ObjectType) objectAtIndex:(NSUInteger) index;
```

#### Return Value

The object located at `index`.

#### Discussion

If `index` is beyond the end of the array (that is, if `index` is greater than or equal to the value returned by `count`), an [`rangeException`](../nsexceptionname/rangeexception.md) is raised.

## Parameters

- `index`: An index within the bounds of the array.

## See Also

### Querying an Array
- [func contains(Any) -> Bool](./contains%28_%29.md)
  Returns a Boolean value that indicates whether a given object is present in the array.
- [var count: Int](./count.md)
  The number of objects in the array.
- [var firstObject: Any?](./firstobject.md)
  The first object in the array.
- [var lastObject: Any?](./lastobject.md)
  The last object in the array.
- [subscript(Int) -> Any](./subscript%28_%29.md)
  Returns the object at the specified index.
- [func objects(at: IndexSet) -> [Any]](./objects%28at%29.md)
  Returns an array containing the objects in the array at the indexes specified by a given index set.
- [func objectEnumerator() -> NSEnumerator](./objectenumerator%28%29.md)
  Returns an enumerator object that lets you access each object in the array.
- [func reverseObjectEnumerator() -> NSEnumerator](./reverseobjectenumerator%28%29.md)
  Returns an enumerator object that lets you access each object in the array, in reverse order.
- [- getObjects:](./getobjects_.md)
  Copies all the objects contained in the array to `aBuffer`.
- [- getObjects:range:](./getobjects_range_.md)
  Copies references to objects contained in the array that fall within the specified range to `aBuffer`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarray/object(at:))*