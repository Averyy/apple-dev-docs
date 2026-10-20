# addObjects(from:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Adds the objects contained in another given array to the end of the receiving array’s content.

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
func addObjects(from otherArray: [Any])
```

```objc
- (void) addObjectsFromArray:(NSArray<id> *) otherArray;
```

## Parameters

- `otherArray`: An array of objects to add to the end of the receiving array’s content.

## See Also

### Related Documentation
- [func remove(Any)](./remove%28_%29.md)
  Removes all occurrences in the array of a given object.
- [func setArray([Any])](./setarray%28_%29.md)
  Sets the receiving array’s elements to those in another given array.
### Adding Objects
- [func add(Any)](./add%28_%29.md)
  Inserts a given object at the end of the array.
- [func insert(Any, at: Int)](./insert%28_,at%29-5dbx5.md)
  Inserts a given object into the array’s contents at a given index.
- [func insert([Any], at: IndexSet)](./insert%28_,at%29-73pln.md)
  Inserts the objects in the provided array into the receiving array at the specified indexes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutablearray/addobjects(from:))*