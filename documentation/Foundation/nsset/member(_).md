# member(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Determines whether a given object is present in the set, and returns that object if it is.

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
func member(_ object: Any) -> Any?
```

```objc
- (ObjectType) member:(ObjectType) object;
```

## Return Value

Returns an object equal to `object` if it’s present in the set, otherwise `nil`.

## Discussion

Each element of the set is checked for equality with `object` until a match is found or the end of the set is reached.  Objects are considered equal if [`isEqual(_:)`](../../ObjectiveC/nsobjectprotocol/isequal%28_%29.md) returns [`true`](../../Swift/true.md).

## Parameters

- `object`: An object to look for in the set.

## See Also

### Accessing Set Members
- [var allObjects: [Any]](./allobjects.md)
  An array containing the set’s members, or an empty array if the set has no members.
- [func anyObject() -> Any?](./anyobject%28%29.md)
  Returns one of the objects in the set, or `nil` if the set contains no objects.
- [func contains(Any) -> Bool](./contains%28_%29.md)
  Returns a Boolean value that indicates whether a given object is present in the set.
- [func filtered(using: NSPredicate) -> Set<AnyHashable>](./filtered%28using%29.md)
  Evaluates a given predicate against each object in the receiving set and returns a new set containing the objects for which the predicate returns true.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsset/member(_:))*