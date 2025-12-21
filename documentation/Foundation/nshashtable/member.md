# member(_:)

**Framework**: Foundation  
**Kind**: method

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

#### Return Value

If `object` is a member of the hash table, returns `object`, otherwise returns `nil`.

#### Discussion

The equality test used depends on the personality option selected. For instance, choosing the [`objectPersonality`](nspointerfunctions/options/objectpersonality.md) option will use `isEqual:` to determine equality. See [`NSPointerFunctions.Options`](nspointerfunctions/options.md) for more information on personality options and their corresponding equality tests.

## Parameters

- `object`: The object to test for membership in the hash table.

## See Also

- [var anyObject: ObjectType?](nshashtable/anyobject.md)
  One of the objects in the hash table.
- [var allObjects: [ObjectType]](nshashtable/allobjects.md)
  The hash table’s members.
- [var setRepresentation: Set<AnyHashable>](nshashtable/setrepresentation.md)
  A set that contains the hash table’s members.
- [var count: Int](nshashtable/count.md)
  The number of elements in the hash table.
- [func contains(ObjectType?) -> Bool](nshashtable/contains(_:).md)
  Returns a Boolean value that indicates whether the hash table contains a given object.
- [func objectEnumerator() -> NSEnumerator](nshashtable/objectenumerator.md)
  Returns an enumerator object that lets you access each object in the hash table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nshashtable/member(_:))*