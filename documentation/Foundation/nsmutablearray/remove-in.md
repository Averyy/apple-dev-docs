# remove(_:in:)

**Framework**: Foundation  
**Kind**: method

Removes all occurrences within a specified range in the array of a given object.

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
func remove(_ anObject: Any, in range: NSRange)
```

#### Discussion

Matches are determined by comparing `anObject` to the objects in the receiver using the `isEqual:` method. If the array does not contain `anObject` within `aRange`, the method has no effect (although it does incur the overhead of searching the contents).

## Parameters

- `anObject`: The object to be removed from the array’s content.
- `range`: The range from which to remove  .

## See Also

- [func removeAllObjects()](nsmutablearray/removeallobjects.md)
  Empties the array of all its elements.
- [func removeLastObject()](nsmutablearray/removelastobject.md)
  Removes the object with the highest-valued index in the array
- [func remove(Any)](nsmutablearray/remove(_:).md)
  Removes all occurrences in the array of a given object.
- [func removeObject(at: Int)](nsmutablearray/removeobject(at:).md)
  Removes the object at `index` .
- [func removeObjects(at: IndexSet)](nsmutablearray/removeobjects(at:).md)
  Removes the objects at the specified indexes from the array.
- [func removeObject(identicalTo: Any)](nsmutablearray/removeobject(identicalto:).md)
  Removes all occurrences of a given object in the array.
- [func removeObject(identicalTo: Any, in: NSRange)](nsmutablearray/removeobject(identicalto:in:).md)
  Removes all occurrences of `anObject` within the specified range in the array.
- [func removeObjects(fromIndices: UnsafeMutablePointer<Int>, numIndices: Int)](nsmutablearray/removeobjects(fromindices:numindices:).md)
  Removes the specified number of objects from the array, beginning at the specified index.
- [func removeObjects(in: [Any])](nsmutablearray/removeobjects(in:)-4yb26.md)
  Removes from the receiving array the objects in another given array.
- [func removeObjects(in: NSRange)](nsmutablearray/removeobjects(in:)-1udmn.md)
  Removes from the array each of the objects within a given range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutablearray/remove(_:in:))*