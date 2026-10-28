# makeObjectsPerformSelector:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Sends a message specified by a given selector to each object in the set.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```objc
- (void) makeObjectsPerformSelector:(SEL) aSelector;
```

## Discussion

The message specified by `aSelector` is sent once to each member of the set. This method raises an `NSInvalidArgumentException` if `aSelector` is `NULL`.

## Parameters

- `aSelector`: A selector that specifies the message to send to the members of the set. The method must not take any arguments. It should not have the side effect of modifying the set. This value must not be `NULL`.

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
- [- makeObjectsPerformSelector:withObject:](./makeobjectsperformselector_withobject_.md)
  Sends a message specified by a given selector to each object in the set.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsset/makeobjectsperformselector:)*