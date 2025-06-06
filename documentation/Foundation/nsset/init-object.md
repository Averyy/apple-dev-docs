# init(object:)

**Framework**: Foundation  
**Kind**: init

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

#### Return Value

A new set that contains a single member, `object`.

## Parameters

- `object`: The object to add to the new set.   receives a   message after being added to the set.

## See Also

- [convenience init(objects: UnsafePointer<AnyObject>, count: Int)](nsset/init(objects:count:)-65ni4.md)
  Creates and returns a set containing a specified number of objects from a given C array of objects.
- [func adding(Any) -> Set<AnyHashable>](nsset/adding(_:).md)
  Returns a new set formed by adding a given object to the receiving set.
- [func addingObjects(from: Set<AnyHashable>) -> Set<AnyHashable>](nsset/addingobjects(from:)-2i31h.md)
  Returns a new set formed by adding the objects in a given set to the receiving set.
- [func addingObjects(from: [Any]) -> Set<AnyHashable>](nsset/addingobjects(from:)-544m9.md)
  Returns a new set formed by adding the objects in a given array to the receiving set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsset/init(object:))*