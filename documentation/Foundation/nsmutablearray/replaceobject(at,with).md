# replaceObject(at:with:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Replaces the object at `index` with `anObject`.

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
func replaceObject(at index: Int, with anObject: Any)
```

```objc
- (void) replaceObjectAtIndex:(NSUInteger) index withObject:(ObjectType) anObject;
```

## Parameters

- `index`: The index of the object to be replaced. This value must not exceed the bounds of the array.

  > ❗ **Important**:  Raises an `NSRangeException` if `index` is beyond the end of the array.
- `anObject`: The object with which to replace the object at index `index` in the array. This value must not be `nil`.

  > ❗ **Important**:  Raises an `NSInvalidArgumentException` if `anObject` is `nil`.

## See Also

### Related Documentation
- [func removeObjects(at: IndexSet)](./removeobjects%28at%29.md)
  Removes the objects at the specified indexes from the array.
- [func removeObject(at: Int)](./removeobject%28at%29.md)
  Removes the object at `index` .
- [func insert(Any, at: Int)](./insert%28_,at%29-5dbx5.md)
  Inserts a given object into the array’s contents at a given index.
- [- setObject:atIndexedSubscript:](./setobject_atindexedsubscript_.md)
  Replaces the object at the index with the new object, possibly adding the object.
### Replacing Objects
- [func replaceObjects(at: IndexSet, with: [Any])](./replaceobjects%28at,with%29.md)
  Replaces the objects in the receiving array at locations specified with the objects from a given array.
- [func replaceObjects(in: NSRange, withObjectsFrom: [Any], range: NSRange)](./replaceobjects%28in,withobjectsfrom,range%29.md)
  Replaces the objects in the receiving array specified by one given range with the objects in another array specified by another range.
- [func replaceObjects(in: NSRange, withObjectsFrom: [Any])](./replaceobjects%28in,withobjectsfrom%29.md)
  Replaces the objects in the receiving array specified by a given range with all of the objects from a given array.
- [func setArray([Any])](./setarray%28_%29.md)
  Sets the receiving array’s elements to those in another given array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutablearray/replaceobject(at:with:))*