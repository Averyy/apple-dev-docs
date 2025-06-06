# replaceObjects(at:with:)

**Framework**: Foundation  
**Kind**: method

Replaces the objects in the receiving array at locations specified with the objects from a given array.

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
func replaceObjects(at indexes: IndexSet, with objects: [Any])
```

#### Discussion

The indexes in `indexes` are used in the same order as the objects in `objects`.

If `objects` or `indexes` is `nil`, this method raises an exception.

## Parameters

- `indexes`: The indexes of the objects to be replaced.
- `objects`: The objects with which to replace the objects in the receiving array at the indexes specified by  . The count of locations in   must equal the count of  .

## See Also

- [func removeObject(at: Int)](nsmutablearray/removeobject(at:).md)
  Removes the object at `index` .
- [func insert(Any, at: Int)](nsmutablearray/insert(_:at:)-5dbx5.md)
  Inserts a given object into the array’s contents at a given index.
- [func replaceObject(at: Int, with: Any)](nsmutablearray/replaceobject(at:with:).md)
  Replaces the object at `index` with `anObject`.
- [func replaceObjects(in: NSRange, withObjectsFrom: [Any], range: NSRange)](nsmutablearray/replaceobjects(in:withobjectsfrom:range:).md)
  Replaces the objects in the receiving array specified by one given range with the objects in another array specified by another range.
- [func replaceObjects(in: NSRange, withObjectsFrom: [Any])](nsmutablearray/replaceobjects(in:withobjectsfrom:).md)
  Replaces the objects in the receiving array specified by a given range with all of the objects from a given array.
- [func setArray([Any])](nsmutablearray/setarray(_:).md)
  Sets the receiving array’s elements to those in another given array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutablearray/replaceobjects(at:with:))*