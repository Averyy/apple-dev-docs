# replaceObjects(in:with:count:)

**Framework**: Foundation  
**Kind**: method

Replaces the objects in the receiving mutable ordered set at the range with the specified number of objects from a given C array.

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
func replaceObjects(in range: NSRange, with objects: UnsafePointer<AnyObject>?, count: Int)
```

#### Discussion

Elements are added to the new array in the same order they appear in objects, up to but not including index count.

## Parameters

- `range`: The range of the objects to replace.
- `objects`: A C array of objects.
- `count`: The number of values from the objects C array to insert in place of the objects in  . This number will be the count of the new array—it must not be negative or greater than the number of elements in objects.

## See Also

- [func add(Any)](nsmutableorderedset/add(_:).md)
  Appends a given object to the end of the mutable ordered set, if it is not already a member.
- [func add(UnsafePointer<AnyObject>?, count: Int)](nsmutableorderedset/add(_:count:).md)
  Appends the given number of objects from a given C array to the end of the mutable ordered set.
- [func addObjects(from: [Any])](nsmutableorderedset/addobjects(from:).md)
  Appends to the end of the mutable ordered set each object contained in a given array that is not already a member.
- [func insert(Any, at: Int)](nsmutableorderedset/insert(_:at:)-7qg51.md)
  Inserts the given object at the specified index of the mutable ordered set, if it is not already a member.
- [func insert([Any], at: IndexSet)](nsmutableorderedset/insert(_:at:)-3ncnm.md)
  Inserts the objects in the array at the specified indexes.
- [func remove(Any)](nsmutableorderedset/remove(_:).md)
  Removes a given object from the mutable ordered set.
- [func removeObject(at: Int)](nsmutableorderedset/removeobject(at:).md)
  Removes a the object at the specified index from the mutable ordered set.
- [func removeObjects(at: IndexSet)](nsmutableorderedset/removeobjects(at:).md)
  Removes the objects at the specified indexes from the mutable ordered set.
- [func removeObjects(in: [Any])](nsmutableorderedset/removeobjects(in:)-8h2kh.md)
  Removes the objects in the array from the mutable ordered set.
- [func removeObjects(in: NSRange)](nsmutableorderedset/removeobjects(in:)-9jkis.md)
  Removes from the mutable ordered set each of the objects within a given range.
- [func removeAllObjects()](nsmutableorderedset/removeallobjects.md)
  Removes all the objects from the mutable ordered set.
- [func replaceObject(at: Int, with: Any)](nsmutableorderedset/replaceobject(at:with:).md)
  Replaces the object at the specified index with the new object.
- [func replaceObjects(at: IndexSet, with: [Any])](nsmutableorderedset/replaceobjects(at:with:).md)
  Replaces the objects at the specified indexes with the new objects.
- [func setObject(Any, at: Int)](nsmutableorderedset/setobject(_:at:).md)
  Appends or replaces the object at the specified index.
- [func moveObjects(at: IndexSet, to: Int)](nsmutableorderedset/moveobjects(at:to:).md)
  Moves the objects at the specified indexes to the new location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutableorderedset/replaceobjects(in:with:count:))*