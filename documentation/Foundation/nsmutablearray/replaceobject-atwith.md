# replaceObject(at:with:)

**Framework**: Foundation  
**Kind**: method

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

## Parameters

- `index`: The index of the object to be replaced. This value must not exceed the bounds of the array.
- `anObject`: The object with which to replace the object at index   in the array. This value must not be  .

## See Also

- [func removeObjects(at: IndexSet)](nsmutablearray/removeobjects(at:).md)
  Removes the objects at the specified indexes from the array.
- [func removeObject(at: Int)](nsmutablearray/removeobject(at:).md)
  Removes the object at `index` .
- [func insert(Any, at: Int)](nsmutablearray/insert(_:at:)-5dbx5.md)
  Inserts a given object into the array’s contents at a given index.
- [func replaceObjects(at: IndexSet, with: [Any])](nsmutablearray/replaceobjects(at:with:).md)
  Replaces the objects in the receiving array at locations specified with the objects from a given array.
- [func replaceObjects(in: NSRange, withObjectsFrom: [Any], range: NSRange)](nsmutablearray/replaceobjects(in:withobjectsfrom:range:).md)
  Replaces the objects in the receiving array specified by one given range with the objects in another array specified by another range.
- [func replaceObjects(in: NSRange, withObjectsFrom: [Any])](nsmutablearray/replaceobjects(in:withobjectsfrom:).md)
  Replaces the objects in the receiving array specified by a given range with all of the objects from a given array.
- [func setArray([Any])](nsmutablearray/setarray(_:).md)
  Sets the receiving array’s elements to those in another given array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutablearray/replaceobject(at:with:))*