# setArray(_:)

**Framework**: Foundation  
**Kind**: method

Sets the receiving array’s elements to those in another given array.

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
func setArray(_ otherArray: [Any])
```

## Parameters

- `otherArray`: The array of objects with which to replace the receiving array’s content.

## See Also

- [func insert(Any, at: Int)](nsmutablearray/insert(_:at:)-5dbx5.md)
  Inserts a given object into the array’s contents at a given index.
- [func addObjects(from: [Any])](nsmutablearray/addobjects(from:).md)
  Adds the objects contained in another given array to the end of the receiving array’s content.
- [func replaceObject(at: Int, with: Any)](nsmutablearray/replaceobject(at:with:).md)
  Replaces the object at `index` with `anObject`.
- [func replaceObjects(at: IndexSet, with: [Any])](nsmutablearray/replaceobjects(at:with:).md)
  Replaces the objects in the receiving array at locations specified with the objects from a given array.
- [func replaceObjects(in: NSRange, withObjectsFrom: [Any], range: NSRange)](nsmutablearray/replaceobjects(in:withobjectsfrom:range:).md)
  Replaces the objects in the receiving array specified by one given range with the objects in another array specified by another range.
- [func replaceObjects(in: NSRange, withObjectsFrom: [Any])](nsmutablearray/replaceobjects(in:withobjectsfrom:).md)
  Replaces the objects in the receiving array specified by a given range with all of the objects from a given array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutablearray/setarray(_:))*