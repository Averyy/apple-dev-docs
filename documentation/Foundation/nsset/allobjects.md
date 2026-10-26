# allObjects

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

An array containing the set’s members, or an empty array if the set has no members.

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
var allObjects: [Any] { get }
```

```objc
@property (copy, readonly) NSArray<id> * allObjects;
```

#### Discussion

The order of the objects in the array is undefined.

## See Also

### Accessing Set Members
- [func anyObject() -> Any?](./anyobject%28%29.md)
  Returns one of the objects in the set, or `nil` if the set contains no objects.
- [func contains(Any) -> Bool](./contains%28_%29.md)
  Returns a Boolean value that indicates whether a given object is present in the set.
- [func filtered(using: NSPredicate) -> Set<AnyHashable>](./filtered%28using%29.md)
  Evaluates a given predicate against each object in the receiving set and returns a new set containing the objects for which the predicate returns true.
- [func member(Any) -> Any?](./member%28_%29.md)
  Determines whether a given object is present in the set, and returns that object if it is.
- [func objectEnumerator() -> NSEnumerator](./objectenumerator%28%29.md)
  Returns an enumerator object that lets you access each object in the set.
- [func enumerateObjects((Any, UnsafeMutablePointer<ObjCBool>) -> Void)](./enumerateobjects%28_%29.md)
  Executes a given block using each object in the set.
- [func enumerateObjects(options: NSEnumerationOptions, using: (Any, UnsafeMutablePointer<ObjCBool>) -> Void)](./enumerateobjects%28options,using%29.md)
  Executes a given block using each object in the set, using the specified enumeration options.
- [func objects(passingTest: (Any, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Set<AnyHashable>](./objects%28passingtest%29.md)
  Returns a set of objects that pass a test in a given block.
- [func objects(options: NSEnumerationOptions, passingTest: (Any, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Set<AnyHashable>](./objects%28options,passingtest%29.md)
  Returns a set of objects that pass a test in a given block, using the specified enumeration options.
- [- makeObjectsPerformSelector:](./makeobjectsperformselector_.md)
  Sends a message specified by a given selector to each object in the set.
- [- makeObjectsPerformSelector:withObject:](./makeobjectsperformselector_withobject_.md)
  Sends a message specified by a given selector to each object in the set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsset/allobjects)*