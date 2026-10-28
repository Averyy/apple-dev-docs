# member(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Determines whether the hash table contains a given object, and returns that object if it is present

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func member(_ object: ObjectType?) -> ObjectType?
```

```objc
- (ObjectType) member:(ObjectType) object;
```

## Return Value

If `object` is a member of the hash table, returns `object`, otherwise returns `nil`.

## Discussion

The equality test used depends on the personality option selected. For instance, choosing the [`objectPersonality`](../nspointerfunctions/options/objectpersonality.md) option will use `isEqual:` to determine equality. See [`NSPointerFunctions.Options`](../nspointerfunctions/options.md) for more information on personality options and their corresponding equality tests.

## Parameters

- `object`: The object to test for membership in the hash table.

## See Also

### Accessing Content
- [var anyObject: ObjectType?](./anyobject.md)
  One of the objects in the hash table.
- [var allObjects: [ObjectType]](./allobjects.md)
  The hash table’s members.
- [var setRepresentation: Set<AnyHashable>](./setrepresentation.md)
  A set that contains the hash table’s members.
- [var count: Int](./count.md)
  The number of elements in the hash table.
- [func contains(ObjectType?) -> Bool](./contains%28_%29.md)
  Returns a Boolean value that indicates whether the hash table contains a given object.
- [func objectEnumerator() -> NSEnumerator](./objectenumerator%28%29.md)
  Returns an enumerator object that lets you access each object in the hash table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nshashtable/member(_:))*