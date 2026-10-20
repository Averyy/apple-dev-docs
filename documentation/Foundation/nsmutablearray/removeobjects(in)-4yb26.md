# removeObjects(in:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Removes from the receiving array the objects in another given array.

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
func removeObjects(in otherArray: [Any])
```

```objc
- (void) removeObjectsInArray:(NSArray<id> *) otherArray;
```

#### Discussion

This method is similar to [`remove(_:)`](./remove%28_%29.md), but it allows you to efficiently remove large sets of objects with a single operation. If the receiving array does not contain objects in `otherArray`, the method has no effect (although it does incur the overhead of searching the contents).

This method assumes that all elements in `otherArray` respond to `hash` and `isEqual:`.

## Parameters

- `otherArray`: An array containing the objects to be removed from the receiving array.

## See Also

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
- [func removeObjects(fromIndices: UnsafeMutablePointer<Int>, numIndices: Int)](./removeobjects%28fromindices,numindices%29.md)
  Removes the specified number of objects from the array, beginning at the specified index.
- [func removeObjects(in: NSRange)](./removeobjects%28in%29-1udmn.md)
  Removes from the array each of the objects within a given range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutablearray/removeobjects(in:)-4yb26)*