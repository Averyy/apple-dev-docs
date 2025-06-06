# replaceObjects(in:withObjectsFrom:)

**Framework**: Foundation  
**Kind**: method

Replaces the objects in the receiving array specified by a given range with all of the objects from a given array.

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
func replaceObjects(in range: NSRange, withObjectsFrom otherArray: [Any])
```

#### Discussion

If `otherArray` has fewer objects than are specified by `aRange`, the extra objects in the receiving array are removed. If `otherArray` has more objects than are specified by `aRange`, the extra objects from `otherArray` are inserted into the receiving array.

## Parameters

- `range`: The range of objects to be replaced in (or removed from) the receiving array.
- `otherArray`: The array of objects from which to select replacements for the objects in  .

## See Also

- [func removeObject(at: Int)](nsmutablearray/removeobject(at:).md)
  Removes the object at `index` .
- [func insert(Any, at: Int)](nsmutablearray/insert(_:at:)-5dbx5.md)
  Inserts a given object into the array’s contents at a given index.
- [func replaceObject(at: Int, with: Any)](nsmutablearray/replaceobject(at:with:).md)
  Replaces the object at `index` with `anObject`.
- [func replaceObjects(at: IndexSet, with: [Any])](nsmutablearray/replaceobjects(at:with:).md)
  Replaces the objects in the receiving array at locations specified with the objects from a given array.
- [func replaceObjects(in: NSRange, withObjectsFrom: [Any], range: NSRange)](nsmutablearray/replaceobjects(in:withobjectsfrom:range:).md)
  Replaces the objects in the receiving array specified by one given range with the objects in another array specified by another range.
- [func setArray([Any])](nsmutablearray/setarray(_:).md)
  Sets the receiving array’s elements to those in another given array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutablearray/replaceobjects(in:withobjectsfrom:))*