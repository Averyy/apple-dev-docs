# enumerateObjects(options:using:)

**Framework**: Foundation  
**Kind**: method

Executes a given block using each object in the set, using the specified enumeration options.

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
func enumerateObjects(options opts: NSEnumerationOptions = [], using block: (Any, UnsafeMutablePointer<ObjCBool>) -> Void)
```

## Parameters

- `opts`: A bitmask that specifies the options for the enumeration.
- `block`: The block takes two arguments:

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
- [func objects(passingTest: (Any, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Set<AnyHashable>](nsset/objects(passingtest:).md)
  Returns a set of objects that pass a test in a given block.
- [func objects(options: NSEnumerationOptions, passingTest: (Any, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Set<AnyHashable>](nsset/objects(options:passingtest:).md)
  Returns a set of objects that pass a test in a given block, using the specified enumeration options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsset/enumerateobjects(options:using:))*