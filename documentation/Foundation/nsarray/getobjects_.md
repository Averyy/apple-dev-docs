# getObjects:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Copies all the objects contained in the array to `aBuffer`.

**Availability**:
- iOS 2.0+ - Deprecated in 11.0
- iPadOS 2.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.13
- tvOS 9.0+ - Deprecated in 11.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 4.0

> **Deprecated**: Use [`getObjects:range:`](./getobjects_range_.md) instead.

## Declaration

```objc
- (void) getObjects:(ObjectType[]) objects;
```

## Discussion

The method copies into `aBuffer` all the objects in the array; the size of the buffer must therefore be at least the count of the array multiplied by the size of an object reference, as shown in the following example (note that this is just an example, you should typically not create a buffer simply to iterate over the contents of an array):

```objc
NSArray *mArray = // ...;
id *objects;
 
NSUInteger count = [mArray count];
objects = malloc(sizeof(id) * count);
 
[mArray getObjects:objects];
 
for (i = 0; i < count; i++) {
    NSLog(@"object at index %d: %@", i, objects[i]);
}
free(objects);
```

### Special Considerations

This deprecated method is unsafe because it could potentially cause buffer overruns.

## Parameters

- `objects`: A C array of objects of size at least the count of the array.

## See Also

### Related Documentation
- [convenience init(objects: UnsafePointer<AnyObject>, count: Int)](./init%28objects,count%29-7dct1.md)
  Creates and returns an array that includes a given number of objects from a given C array.
### Querying an Array
- [func contains(Any) -> Bool](./contains%28_%29.md)
  Returns a Boolean value that indicates whether a given object is present in the array.
- [var count: Int](./count.md)
  The number of objects in the array.
- [- getObjects:range:](./getobjects_range_.md)
  Copies references to objects contained in the array that fall within the specified range to `aBuffer`.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarray/getobjects:)*