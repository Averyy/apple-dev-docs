# removeObject(at:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Removes the object at `index` .

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
func removeObject(at index: Int)
```

```objc
- (void) removeObjectAtIndex:(NSUInteger) index;
```

## Discussion

To fill the gap, all elements beyond `index` are moved by subtracting 1 from their index.

## Parameters

- `index`: The index from which to remove the object in the array. The value must not exceed the bounds of the array.

  > ❗ **Important**:  Raises an exception `NSRangeException` if `index` is beyond the end of the array.

## See Also

### Related Documentation
- [func insert(Any, at: Int)](./insert%28_,at%29-5dbx5.md)
  Inserts a given object into the array’s contents at a given index.
### Removing Objects
- [func removeAllObjects()](./removeallobjects%28%29.md)
  Empties the array of all its elements.
- [func removeLastObject()](./removelastobject%28%29.md)
  Removes the object with the highest-valued index in the array
- [func remove(Any)](./remove%28_%29.md)
  Removes all occurrences in the array of a given object.
- [func remove(Any, in: NSRange)](./remove%28_,in%29.md)
  Removes all occurrences within a specified range in the array of a given object.
- [func removeObjects(at: IndexSet)](./removeobjects%28at%29.md)
  Removes the objects at the specified indexes from the array.
- [func removeObject(identicalTo: Any)](./removeobject%28identicalto%29.md)
  Removes all occurrences of a given object in the array.
- [func removeObject(identicalTo: Any, in: NSRange)](./removeobject%28identicalto,in%29.md)
  Removes all occurrences of `anObject` within the specified range in the array.
- [func removeObjects(fromIndices: UnsafeMutablePointer<Int>, numIndices: Int)](./removeobjects%28fromindices,numindices%29.md)
  Removes the specified number of objects from the array, beginning at the specified index.
- [func removeObjects(in: [Any])](./removeobjects%28in%29-4yb26.md)
  Removes from the receiving array the objects in another given array.
- [func removeObjects(in: NSRange)](./removeobjects%28in%29-1udmn.md)
  Removes from the array each of the objects within a given range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutablearray/removeobject(at:))*