# contains(_:)

**Framework**: Foundation  
**Kind**: method

Returns a Boolean value that indicates whether a given object is present in the set.

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
func contains(_ anObject: Any) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if `anObject` is present in the set, otherwise [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

Each element of the set is checked for equality with `anObject` until a match is found or the end of the set is reached.  Objects are considered equal if [`isEqual(_:)`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol/isEqual(_:)) returns [`true`](https://developer.apple.com/documentation/swift/true).

## Parameters

- `anObject`: An object to look for in the set.

## See Also

- [var allObjects: [Any]](nsset/allobjects.md)
  An array containing the set’s members, or an empty array if the set has no members.
- [func anyObject() -> Any?](nsset/anyobject.md)
  Returns one of the objects in the set, or `nil` if the set contains no objects.
- [func filtered(using: NSPredicate) -> Set<AnyHashable>](nsset/filtered(using:).md)
  Evaluates a given predicate against each object in the receiving set and returns a new set containing the objects for which the predicate returns true.
- [func member(Any) -> Any?](nsset/member(_:).md)
  Determines whether a given object is present in the set, and returns that object if it is.
- [func objectEnumerator() -> NSEnumerator](nsset/objectenumerator.md)
  Returns an enumerator object that lets you access each object in the set.
- [func enumerateObjects((Any, UnsafeMutablePointer<ObjCBool>) -> Void)](nsset/enumerateobjects(_:).md)
  Executes a given block using each object in the set.
- [func enumerateObjects(options: NSEnumerationOptions, using: (Any, UnsafeMutablePointer<ObjCBool>) -> Void)](nsset/enumerateobjects(options:using:).md)
  Executes a given block using each object in the set, using the specified enumeration options.
- [func objects(passingTest: (Any, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Set<AnyHashable>](nsset/objects(passingtest:).md)
  Returns a set of objects that pass a test in a given block.
- [func objects(options: NSEnumerationOptions, passingTest: (Any, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Set<AnyHashable>](nsset/objects(options:passingtest:).md)
  Returns a set of objects that pass a test in a given block, using the specified enumeration options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsset/contains(_:))*