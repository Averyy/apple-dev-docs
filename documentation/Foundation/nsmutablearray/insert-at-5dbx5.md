# insert(_:at:)

**Framework**: Foundation  
**Kind**: method

Inserts a given object into the array’s contents at a given index.

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
func insert(_ anObject: Any, at index: Int)
```

#### Discussion

If `index` is already occupied, the objects at `index` and beyond are shifted by adding `1` to their indices to make room.

Note that `NSArray` objects are not like C arrays. That is, even though you specify a size when you create an array, the specified size is regarded as a “hint”; the actual size of the array is still 0. This means that you cannot insert an object at an index greater than the current count of an array. For example, if an array contains two objects, its size is 2, so you can add objects at indices 0, 1, or 2. Index 3 is illegal and out of bounds; if you try to add an object at index 3 (when the size of the array is 2), `NSMutableArray` raises an exception.

## Parameters

- `anObject`: The object to add to the array’s content. This value must not be  .
- `index`: The index in the array at which to insert  . This value must not be greater than the count of elements in the array.

## See Also

- [func removeObject(at: Int)](nsmutablearray/removeobject(at:).md)
  Removes the object at `index` .
- [func add(Any)](nsmutablearray/add(_:).md)
  Inserts a given object at the end of the array.
- [func addObjects(from: [Any])](nsmutablearray/addobjects(from:).md)
  Adds the objects contained in another given array to the end of the receiving array’s content.
- [func insert([Any], at: IndexSet)](nsmutablearray/insert(_:at:)-73pln.md)
  Inserts the objects in the provided array into the receiving array at the specified indexes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutablearray/insert(_:at:)-5dbx5)*