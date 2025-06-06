# objectEnumerator()

**Framework**: Foundation  
**Kind**: method

Returns an enumerator object that lets you access each object in the set.

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
func objectEnumerator() -> NSEnumerator
```

#### Return Value

An enumerator object that lets you access each object in the set.

#### Discussion

The following code fragment illustrates how you can use this method.

```objc
NSEnumerator *enumerator = [mySet objectEnumerator];
id value;
 
while ((value = [enumerator nextObject])) {
    /* code that acts on the set’s values */
}
```

When this method is used with mutable subclasses of `NSSet`, your code shouldn’t modify the set during enumeration. If you intend to modify the set, use the [`allObjects`](nsset/allobjects.md) method to create a “snapshot” of the set’s members. Enumerate the snapshot, but make your modifications to the original set.

##### Special Considerations

It is more efficient to use the fast enumeration protocol (see [`NSFastEnumeration`](nsfastenumeration.md)). Fast enumeration is available in macOS 10.5 and later and iOS 2.0 and later.

## See Also

- [func nextObject() -> Any?](nsenumerator/nextobject.md)
  Returns the next object from the collection being enumerated.
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
- [func enumerateObjects((Any, UnsafeMutablePointer<ObjCBool>) -> Void)](nsset/enumerateobjects(_:).md)
  Executes a given block using each object in the set.
- [func enumerateObjects(options: NSEnumerationOptions, using: (Any, UnsafeMutablePointer<ObjCBool>) -> Void)](nsset/enumerateobjects(options:using:).md)
  Executes a given block using each object in the set, using the specified enumeration options.
- [func objects(passingTest: (Any, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Set<AnyHashable>](nsset/objects(passingtest:).md)
  Returns a set of objects that pass a test in a given block.
- [func objects(options: NSEnumerationOptions, passingTest: (Any, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Set<AnyHashable>](nsset/objects(options:passingtest:).md)
  Returns a set of objects that pass a test in a given block, using the specified enumeration options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsset/objectenumerator())*