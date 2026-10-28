# objects(options:passingTest:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (NSSet<id> *) objectsWithOptions:(NSEnumerationOptions) opts passingTest:(BOOL (^)(ObjectType obj, BOOL *stop)) predicate;
```

## Return Value

An [`NSSet`](../nsset.md) containing objects that pass the test.

## Parameters

- `opts`: A bitmask that specifies the options for the enumeration.
- `predicate`: The block to apply to elements in the set.

  The block takes two arguments:

  - **obj**: The element in the set.
  - **stop**: A reference to a Boolean value. The block can set the value to [`true`](../../Swift/true.md) to stop further processing of the set. The `stop` argument is an out-only argument. You should only ever set this Boolean to [`true`](../../Swift/true.md) within the block.

  The block returns a Boolean value that indicates whether `obj` passed the test.

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
- [- makeObjectsPerformSelector:](./makeobjectsperformselector_.md)
  Sends a message specified by a given selector to each object in the set.
- [- makeObjectsPerformSelector:withObject:](./makeobjectsperformselector_withobject_.md)
  Sends a message specified by a given selector to each object in the set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsset/objects(options:passingtest:))*