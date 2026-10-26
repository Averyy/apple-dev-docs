# setObject:atIndexedSubscript:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Replaces the object at the index with the new object, possibly adding the object.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```objc
- (void) setObject:(ObjectType) obj atIndexedSubscript:(NSUInteger) idx;
```

#### Discussion

This method has the same behavior as the [`replaceObject(at:with:)`](./replaceobject%28at,with%29.md) method.

If `idx` is beyond the end of the array (that is, if `idx` is greater than the value returned by `count`), an [`rangeException`](../nsexceptionname/rangeexception.md) is raised.

You shouldn’t need to call this method directly. Instead, this method is called when setting an object by index using subscripting.

```objc
mutableArray[3] = @"someValue"; // equivalent to [mutableArray replaceObjectAtIndex:3 withObject:@"someValue"]
```

## Parameters

- `obj`: The object with which to replace the object at index `idx` in the array. This value must not be `nil`.

  > ❗ **Important**:  Raises an `NSInvalidArgumentException` if `anObject` is `nil`.
- `idx`: The index of the object to be replaced. This value must not exceed the bounds of the array.

  > ❗ **Important**:  Raises an `NSRangeException` if `idx` is beyond the end of the array.

## See Also

### Related Documentation
- [subscript(Int) -> Any](../nsarray/subscript%28_%29.md)
  Returns the object at the specified index.
- [func insert(Any, at: Int)](./insert%28_,at%29-5dbx5.md)
  Inserts a given object into the array’s contents at a given index.
- [func removeObject(at: Int)](./removeobject%28at%29.md)
  Removes the object at `index` .
- [func removeObjects(at: IndexSet)](./removeobjects%28at%29.md)
  Removes the objects at the specified indexes from the array.
### Replacing Objects
- [func replaceObject(at: Int, with: Any)](./replaceobject%28at,with%29.md)
  Replaces the object at `index` with `anObject`.
- [func replaceObjects(at: IndexSet, with: [Any])](./replaceobjects%28at,with%29.md)
  Replaces the objects in the receiving array at locations specified with the objects from a given array.
- [func replaceObjects(in: NSRange, withObjectsFrom: [Any], range: NSRange)](./replaceobjects%28in,withobjectsfrom,range%29.md)
  Replaces the objects in the receiving array specified by one given range with the objects in another array specified by another range.
- [func replaceObjects(in: NSRange, withObjectsFrom: [Any])](./replaceobjects%28in,withobjectsfrom%29.md)
  Replaces the objects in the receiving array specified by a given range with all of the objects from a given array.
- [func setArray([Any])](./setarray%28_%29.md)
  Sets the receiving array’s elements to those in another given array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutablearray/setobject:atindexedsubscript:)*