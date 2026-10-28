# getObjects:range:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Copies references to objects contained in the array that fall within the specified range to `aBuffer`.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```objc
- (void) getObjects:(ObjectType[]) objects range:(NSRange) range;
```

## Discussion

The method copies into `aBuffer` references to objects in the array in the range specified by `aRange`; the size of the buffer must therefore be at least the length of the range multiplied by the size of an object reference, as shown in the following example (this is solely for illustration—you should typically not create a buffer simply to iterate over the contents of an array):

```objc
NSArray *mArray = // an array with at least six elements...;
id *objects;
 
NSRange range = NSMakeRange(2, 4);
objects = malloc(sizeof(id) * range.length);
 
[mArray getObjects:objects range:range];
 
for (i = 0; i < range.length; i++) {
    NSLog(@"objects: %@", objects[i]);
}
free(objects);
```

## Parameters

- `objects`: A C array of objects of size at least the length of the range specified by `aRange`.
- `range`: A range within the bounds of the array.

  If the location plus the length of the range is greater than the count of the array, this method raises an [`rangeException`](../nsexceptionname/rangeexception.md).

## See Also

### Related Documentation
- [convenience init(objects: UnsafePointer<AnyObject>, count: Int)](./init%28objects,count%29-7dct1.md)
  Creates and returns an array that includes a given number of objects from a given C array.
### Querying an Array
- [func contains(Any) -> Bool](./contains%28_%29.md)
  Returns a Boolean value that indicates whether a given object is present in the array.
- [var count: Int](./count.md)
  The number of objects in the array.
- [- getObjects:](./getobjects_.md)
  Copies all the objects contained in the array to `aBuffer`.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarray/getobjects:range:)*