# removeObjects(at:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Removes the objects at the specified indexes from the array.

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
func removeObjects(at indexes: IndexSet)
```

```objc
- (void) removeObjectsAtIndexes:(NSIndexSet *) indexes;
```

#### Discussion

This method is similar to [`removeObject(at:)`](./removeobject%28at%29.md), but allows you to efficiently remove multiple objects with a single operation. `indexes` specifies the locations of objects to be removed given the state of the array when the method is invoked, as illustrated in the following example:

```objc
NSMutableArray *array = [NSMutableArray arrayWithObjects: @"one", @"a", @"two", @"b", @"three", @"four", nil];
NSMutableIndexSet *indexes = [NSMutableIndexSet indexSetWithIndex:1];
[indexes addIndex:3];
[array removeObjectsAtIndexes:indexes];
NSLog(@"array: %@", array);
 
// Output: array: (one, two, three, four)
```

If `indexes` is `nil`, this method raises an exception.

## Parameters

- `indexes`: The indexes of the objects to remove from the array. The locations specified by `indexes` must lie within the bounds of the array.

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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutablearray/removeobjects(at:))*