# init(objects:count:)

**Framework**: Foundation  
**Kind**: init

Creates and returns a set containing a specified number of objects from a given C array of objects.

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
convenience init(objects: UnsafePointer<AnyObject>, count cnt: Int)
```

#### Return Value

A new set containing `cnt` objects from the list of objects specified by `objects`.

## Parameters

- `objects`: A C array of objects to add to the new set. If the same object appears more than once in  , it is added only once to the returned set. Each object receives a   message as it is added to the set.
- `cnt`: The number of objects from   to add to the new set.

## See Also

- [convenience init(object: Any)](nsset/init(object:).md)
  Creates and returns a set that contains a single given object.
- [func adding(Any) -> Set<AnyHashable>](nsset/adding(_:).md)
  Returns a new set formed by adding a given object to the receiving set.
- [func addingObjects(from: Set<AnyHashable>) -> Set<AnyHashable>](nsset/addingobjects(from:)-2i31h.md)
  Returns a new set formed by adding the objects in a given set to the receiving set.
- [func addingObjects(from: [Any]) -> Set<AnyHashable>](nsset/addingobjects(from:)-544m9.md)
  Returns a new set formed by adding the objects in a given array to the receiving set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsset/init(objects:count:)-65ni4)*