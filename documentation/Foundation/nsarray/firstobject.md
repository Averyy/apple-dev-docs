# firstObject

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The first object in the array.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var firstObject: Any? { get }
```

```objc
@property (nonatomic, readonly, nullable) ObjectType firstObject;
```

## Discussion

If the array is empty, returns `nil`.

## See Also

### Querying an Array
- [func contains(Any) -> Bool](./contains%28_%29.md)
  Returns a Boolean value that indicates whether a given object is present in the array.
- [var count: Int](./count.md)
  The number of objects in the array.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarray/firstobject)*