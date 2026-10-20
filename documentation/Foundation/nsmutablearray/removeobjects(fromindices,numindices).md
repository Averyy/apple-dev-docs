# removeObjects(fromIndices:numIndices:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Removes the specified number of objects from the array, beginning at the specified index.

**Availability**:
- iOS 2.0+ - Deprecated in 4.0
- iPadOS 2.0+ - Deprecated in 4.0
- Mac Catalyst 2.0+ - Deprecated in 4.0
- tvOS 9.0+ - Deprecated in 9.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: Do not use this method, use [`removeObjects(at:)`](./removeobjects%28at%29.md) instead.

## Declaration

```swift
func removeObjects(fromIndices indices: UnsafeMutablePointer<Int>, numIndices cnt: Int)
```

```objc
- (void) removeObjectsFromIndices:(NSUInteger *) indices numIndices:(NSUInteger) cnt;
```

#### Discussion

This method is similar to [`removeObject(at:)`](./removeobject%28at%29.md), but it allows you to efficiently remove multiple objects with a single operation. If you sort the list of indexes in ascending order, you will improve the speed of this operation.

This method cannot be sent to a remote object with distributed objects.

##### Special Considerations

This deprecated method uses a C array of indices. The [`removeObjects(at:)`](./removeobjects%28at%29.md) method uses an [`NSIndexSet`](../nsindexset.md) which provides a more efficient way of indexing into an array.

## Parameters

- `indices`: A C array of the indices of the objects to remove from the receiving array.
- `cnt`: The number of objects to remove from the receiving array.

## See Also

### Related Documentation
- [init(capacity: Int)](./init%28capacity%29.md)
  Returns an array, initialized with enough memory to initially hold a given number of objects.
### Removing Objects
- [func removeAllObjects()](./removeallobjects%28%29.md)
  Empties the array of all its elements.
- [func removeLastObject()](./removelastobject%28%29.md)
  Removes the object with the highest-valued index in the array
- [func remove(Any)](./remove%28_%29.md)
  Removes all occurrences in the array of a given object.
- [func remove(Any, in: NSRange)](./remove%28_,in%29.md)
  Removes all occurrences within a specified range in the array of a given object.
- [func removeObject(at: Int)](./removeobject%28at%29.md)
  Removes the object at `index` .
- [func removeObjects(at: IndexSet)](./removeobjects%28at%29.md)
  Removes the objects at the specified indexes from the array.
- [func removeObject(identicalTo: Any)](./removeobject%28identicalto%29.md)
  Removes all occurrences of a given object in the array.
- [func removeObject(identicalTo: Any, in: NSRange)](./removeobject%28identicalto,in%29.md)
  Removes all occurrences of `anObject` within the specified range in the array.
- [func removeObjects(in: [Any])](./removeobjects%28in%29-4yb26.md)
  Removes from the receiving array the objects in another given array.
- [func removeObjects(in: NSRange)](./removeobjects%28in%29-1udmn.md)
  Removes from the array each of the objects within a given range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutablearray/removeobjects(fromindices:numindices:))*