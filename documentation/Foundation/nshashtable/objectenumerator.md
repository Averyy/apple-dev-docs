# objectEnumerator()

**Framework**: Foundation  
**Kind**: method

Returns an enumerator object that lets you access each object in the hash table.

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
func objectEnumerator() -> NSEnumerator
```

#### Return Value

An enumerator object that lets you access each object in the hash table.

#### Discussion

The following code fragment illustrates how you can use this method.

```objc
NSEnumerator *enumerator = [myHashTable objectEnumerator];
id value;
 
while ((value = [enumerator nextObject])) {
    /* code that acts on the hash table's values */
}
```

##### Special Considerations

It is more efficient to use the fast enumeration protocol (see [`NSFastEnumeration`](nsfastenumeration.md)).

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
- [func member(ObjectType?) -> ObjectType?](nshashtable/member(_:).md)
  Determines whether the hash table contains a given object, and returns that object if it is present


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nshashtable/objectenumerator())*