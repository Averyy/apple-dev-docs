# setRepresentation

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A set that contains the hash table’s members.

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
var setRepresentation: Set<AnyHashable> { get }
```

```objc
@property (copy, readonly) NSSet<id> * setRepresentation;
```

## See Also

### Accessing Content
- [var anyObject: ObjectType?](./anyobject.md)
  One of the objects in the hash table.
- [var allObjects: [ObjectType]](./allobjects.md)
  The hash table’s members.
- [var count: Int](./count.md)
  The number of elements in the hash table.
- [func contains(ObjectType?) -> Bool](./contains%28_%29.md)
  Returns a Boolean value that indicates whether the hash table contains a given object.
- [func member(ObjectType?) -> ObjectType?](./member%28_%29.md)
  Determines whether the hash table contains a given object, and returns that object if it is present
- [func objectEnumerator() -> NSEnumerator](./objectenumerator%28%29.md)
  Returns an enumerator object that lets you access each object in the hash table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nshashtable/setrepresentation)*