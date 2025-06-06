# addingObjects(from:)

**Framework**: Foundation  
**Kind**: method

Returns a new set formed by adding the objects in a given set to the receiving set.

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
func addingObjects(from other: Set<AnyHashable>) -> Set<AnyHashable>
```

#### Return Value

A new set formed by adding the objects in `other` to the receiving set.

## Parameters

- `other`: The set of objects to add to the receiving set.

## See Also

- [convenience init(object: Any)](nsset/init(object:).md)
  Creates and returns a set that contains a single given object.
- [convenience init(objects: UnsafePointer<AnyObject>, count: Int)](nsset/init(objects:count:)-65ni4.md)
  Creates and returns a set containing a specified number of objects from a given C array of objects.
- [func adding(Any) -> Set<AnyHashable>](nsset/adding(_:).md)
  Returns a new set formed by adding a given object to the receiving set.
- [func addingObjects(from: [Any]) -> Set<AnyHashable>](nsset/addingobjects(from:)-544m9.md)
  Returns a new set formed by adding the objects in a given array to the receiving set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsset/addingobjects(from:)-2i31h)*