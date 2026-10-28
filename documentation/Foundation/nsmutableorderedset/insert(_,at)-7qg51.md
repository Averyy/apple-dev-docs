# insert(_:at:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Inserts the given object at the specified index of the mutable ordered set, if it is not already a member.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func insert(_ object: Any, at idx: Int)
```

```objc
- (void) insertObject:(ObjectType) object atIndex:(NSUInteger) idx;
```

## Discussion

If the object is already a member, this method has no effect. If the specified index is already occupied, the objects at that index and beyond are shifted by adding `1` to their indexes to make room for the inserted object.

## Parameters

- `object`: The object to insert into the set’s content.
- `idx`: The index in the mutable ordered set at which to insert `object`. This value must not be greater than the count of elements in the array.

  > ❗ **Important**:  Important: Raises an [`rangeException`](../nsexceptionname/rangeexception.md) if `idx` is greater than the number of elements in the mutable ordered set.

## See Also

### Adding, Removing, and Reordering Entries
- [func add(Any)](./add%28_%29.md)
  Appends a given object to the end of the mutable ordered set, if it is not already a member.
- [func add(UnsafePointer<AnyObject>?, count: Int)](./add%28_,count%29.md)
  Appends the given number of objects from a given C array to the end of the mutable ordered set.
- [func addObjects(from: [Any])](./addobjects%28from%29.md)
  Appends to the end of the mutable ordered set each object contained in a given array that is not already a member.
- [func insert([Any], at: IndexSet)](./insert%28_,at%29-3ncnm.md)
  Inserts the objects in the array at the specified indexes.
- [func remove(Any)](./remove%28_%29.md)
  Removes a given object from the mutable ordered set.
- [func removeObject(at: Int)](./removeobject%28at%29.md)
  Removes a the object at the specified index from the mutable ordered set.
- [func removeObjects(at: IndexSet)](./removeobjects%28at%29.md)
  Removes the objects at the specified indexes from the mutable ordered set.
- [func removeObjects(in: [Any])](./removeobjects%28in%29-8h2kh.md)
  Removes the objects in the array from the mutable ordered set.
- [func removeObjects(in: NSRange)](./removeobjects%28in%29-9jkis.md)
  Removes from the mutable ordered set each of the objects within a given range.
- [func removeAllObjects()](./removeallobjects%28%29.md)
  Removes all the objects from the mutable ordered set.
- [func replaceObject(at: Int, with: Any)](./replaceobject%28at,with%29.md)
  Replaces the object at the specified index with the new object.
- [func replaceObjects(at: IndexSet, with: [Any])](./replaceobjects%28at,with%29.md)
  Replaces the objects at the specified indexes with the new objects.
- [func replaceObjects(in: NSRange, with: UnsafePointer<AnyObject>?, count: Int)](./replaceobjects%28in,with,count%29.md)
  Replaces the objects in the receiving mutable ordered set at the range with the specified number of objects from a given C array.
- [func setObject(Any, at: Int)](./setobject%28_,at%29.md)
  Appends or replaces the object at the specified index.
- [func moveObjects(at: IndexSet, to: Int)](./moveobjects%28at,to%29.md)
  Moves the objects at the specified indexes to the new location.
- [- setObject:atIndexedSubscript:](./setobject_atindexedsubscript_.md)
  Replaces the given object at the specified index of the mutable ordered set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutableorderedset/insert(_:at:)-7qg51)*