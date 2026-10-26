# init(object:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Creates and returns a set that contains a single given object.

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
convenience init(object: Any)
```

```objc
+ (instancetype) setWithObject:(ObjectType) object;
```

#### Return Value

A new set that contains a single member, `object`.

## Parameters

- `object`: The object to add to the new set. `object` receives a [`retain`](../../ObjectiveC/nsobject-c.protocol/retain.md) message after being added to the set.

## See Also

### Creating a Set
- [convenience init(objects: UnsafePointer<AnyObject>, count: Int)](./init%28objects,count%29-65ni4.md)
  Creates and returns a set containing a specified number of objects from a given C array of objects.
- [func adding(Any) -> Set<AnyHashable>](./adding%28_%29.md)
  Returns a new set formed by adding a given object to the receiving set.
- [func addingObjects(from: Set<AnyHashable>) -> Set<AnyHashable>](./addingobjects%28from%29-2i31h.md)
  Returns a new set formed by adding the objects in a given set to the receiving set.
- [func addingObjects(from: [Any]) -> Set<AnyHashable>](./addingobjects%28from%29-544m9.md)
  Returns a new set formed by adding the objects in a given array to the receiving set.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsset/init(object:))*