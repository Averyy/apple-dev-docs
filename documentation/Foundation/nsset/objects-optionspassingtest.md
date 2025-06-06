# objects(options:passingTest:)

**Framework**: Foundation  
**Kind**: method

Returns a set of objects that pass a test in a given block, using the specified enumeration options.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func objects(options opts: NSEnumerationOptions = [], passingTest predicate: (Any, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Set<AnyHashable>
```

#### Return Value

An [`NSSet`](nsset.md) containing objects that pass the test.

## Parameters

- `opts`: A bitmask that specifies the options for the enumeration.
- `predicate`: The block returns a Boolean value that indicates whether   passed the test.

## See Also

- [var allObjects: [Any]](nsset/allobjects.md)
  An array containing the set’s members, or an empty array if the set has no members.
- [func anyObject() -> Any?](nsset/anyobject.md)
  Returns one of the objects in the set, or `nil` if the set contains no objects.
- [func contains(Any) -> Bool](nsset/contains(_:).md)
  Returns a Boolean value that indicates whether a given object is present in the set.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsset/objects(options:passingtest:))*