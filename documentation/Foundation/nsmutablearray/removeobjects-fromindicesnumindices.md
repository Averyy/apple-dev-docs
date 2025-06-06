# removeObjects(fromIndices:numIndices:)

**Framework**: Foundation  
**Kind**: method

Removes the specified number of objects from the array, beginning at the specified index.

**Availability**:
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func removeObjects(fromIndices indices: UnsafeMutablePointer<Int>, numIndices cnt: Int)
```

#### Discussion

This method is similar to [`removeObject(at:)`](nsmutablearray/removeobject(at:).md), but it allows you to efficiently remove multiple objects with a single operation. If you sort the list of indexes in ascending order, you will improve the speed of this operation.

This method cannot be sent to a remote object with distributed objects.

##### Special Considerations

This deprecated method uses a C array of indices. The [`removeObjects(at:)`](nsmutablearray/removeobjects(at:).md) method uses an [`NSIndexSet`](nsindexset.md) which provides a more efficient way of indexing into an array.

## Parameters

- `indices`: A C array of the indices of the objects to remove from the receiving array.
- `cnt`: The number of objects to remove from the receiving array.

## See Also

- [init(capacity: Int)](nsmutablearray/init(capacity:).md)
  Returns an array, initialized with enough memory to initially hold a given number of objects.
- [func removeAllObjects()](nsmutablearray/removeallobjects.md)
  Empties the array of all its elements.
- [func removeLastObject()](nsmutablearray/removelastobject.md)
  Removes the object with the highest-valued index in the array
- [func remove(Any)](nsmutablearray/remove(_:).md)
  Removes all occurrences in the array of a given object.
- [func remove(Any, in: NSRange)](nsmutablearray/remove(_:in:).md)
  Removes all occurrences within a specified range in the array of a given object.
- [func removeObject(at: Int)](nsmutablearray/removeobject(at:).md)
  Removes the object at `index` .
- [func removeObjects(at: IndexSet)](nsmutablearray/removeobjects(at:).md)
  Removes the objects at the specified indexes from the array.
- [func removeObject(identicalTo: Any)](nsmutablearray/removeobject(identicalto:).md)
  Removes all occurrences of a given object in the array.
- [func removeObject(identicalTo: Any, in: NSRange)](nsmutablearray/removeobject(identicalto:in:).md)
  Removes all occurrences of `anObject` within the specified range in the array.
- [func removeObjects(in: [Any])](nsmutablearray/removeobjects(in:)-4yb26.md)
  Removes from the receiving array the objects in another given array.
- [func removeObjects(in: NSRange)](nsmutablearray/removeobjects(in:)-1udmn.md)
  Removes from the array each of the objects within a given range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutablearray/removeobjects(fromindices:numindices:))*