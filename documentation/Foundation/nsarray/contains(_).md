# contains(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (BOOL) containsObject:(ObjectType) anObject;
```

## Return Value

[`true`](../../Swift/true.md) if `anObject` is present in the array, otherwise [`false`](../../Swift/false.md).

## Discussion

Starting at index `0`, each element of the array is checked for equality with `anObject` until a match is found or the end of the array is reached.  Objects are considered equal if [`isEqual(_:)`](../../ObjectiveC/nsobjectprotocol/isequal%28_%29.md) returns [`true`](../../Swift/true.md).

To determine if the array contains a particular instance of an object, you can test for identity rather than equality by calling the [`indexOfObjectIdentical(to:)`](./indexofobjectidentical%28to%29.md) method and comparing the return value to [`NSNotFound`](../nsnotfound-9t5v2.md).

## Parameters

- `anObject`: An object to look for in the array.

## See Also

### Related Documentation
- [func indexOfObjectIdentical(to: Any) -> Int](./indexofobjectidentical%28to%29.md)
  Returns the lowest index whose corresponding array value is identical to a given object.
- [func index(of: Any) -> Int](./index%28of%29.md)
  Returns the lowest index whose corresponding array value is equal to a given object.
### Querying an Array
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
- [func reverseObjectEnumerator() -> NSEnumerator](./reverseobjectenumerator%28%29.md)
  Returns an enumerator object that lets you access each object in the array, in reverse order.
- [- getObjects:](./getobjects_.md)
  Copies all the objects contained in the array to `aBuffer`.
- [- getObjects:range:](./getobjects_range_.md)
  Copies references to objects contained in the array that fall within the specified range to `aBuffer`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarray/contains(_:))*