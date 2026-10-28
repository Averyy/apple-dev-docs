# addingObjects(from:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns a new set formed by adding the objects in a given array to the receiving set.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func addingObjects(from other: [Any]) -> Set<AnyHashable>
```

```objc
- (NSSet<id> *) setByAddingObjectsFromArray:(NSArray<id> *) other;
```

## Return Value

A new set formed by adding the objects in `other` to the receiving set.

## Parameters

- `other`: The array of objects to add to the set.

## See Also

### Creating a Set
- [convenience init(object: Any)](./init%28object%29.md)
  Creates and returns a set that contains a single given object.
- [convenience init(objects: UnsafePointer<AnyObject>, count: Int)](./init%28objects,count%29-65ni4.md)
  Creates and returns a set containing a specified number of objects from a given C array of objects.
- [func adding(Any) -> Set<AnyHashable>](./adding%28_%29.md)
  Returns a new set formed by adding a given object to the receiving set.
- [func addingObjects(from: Set<AnyHashable>) -> Set<AnyHashable>](./addingobjects%28from%29-2i31h.md)
  Returns a new set formed by adding the objects in a given set to the receiving set.
- [+ setWithSet:](./setwithset_.md)
  Creates and returns a set containing the objects from another set.
### Related Documentation
- [+ setWithArray:](./setwitharray_.md)
  Creates and returns a set containing a uniqued collection of the objects contained in a given array.
- [+ set](./set.md)
  Creates and returns an empty set.
- [+ setWithObjects:](./setwithobjects_.md)
  Creates and returns a set containing the objects in a given argument list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsset/addingobjects(from:)-544m9)*