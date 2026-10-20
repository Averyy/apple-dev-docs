# objects(at:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns an array containing the objects in the array at the indexes specified by a given index set.

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

#### Return Value

An array containing the objects in the array at the indexes specified by `indexes`.

#### Discussion

The returned objects are in the ascending order of their indexes in `indexes`, so that object in returned array with higher index in indexes will follow the object with smaller index in `indexes`.

Raises an [`rangeException`](../nsexceptionname/rangeexception.md) if any location in `indexes` exceeds the bounds of the array, `indexes` is `nil`.

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
- [func object(at: Int) -> Any](./object%28at%29.md)
  Returns the object located at the specified index.
- [subscript(Int) -> Any](./subscript%28_%29.md)
  Returns the object at the specified index.
- [func objectEnumerator() -> NSEnumerator](./objectenumerator%28%29.md)
  Returns an enumerator object that lets you access each object in the array.
- [func reverseObjectEnumerator() -> NSEnumerator](./reverseobjectenumerator%28%29.md)
  Returns an enumerator object that lets you access each object in the array, in reverse order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarray/objects(at:))*