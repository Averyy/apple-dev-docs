# changeWithObject:type:index:

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Creates an change object that represents inserting or removing an object from an ordered collection at a specific index.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```objc
+ (NSOrderedCollectionChange<id> *) changeWithObject:(ObjectType) anObject type:(NSCollectionChangeType) type index:(NSUInteger) index;
```

#### Return Value

An object that represents an indexed change to an ordered collection and references the object to be inserted or removed.

## Parameters

- `anObject`: An object to be removed or inserted by the change.
- `type`: The type of change
- `index`: The index location within an ordered collection where the change applies.

## See Also

### Creating a Change
- [convenience init(object: Any?, type: NSCollectionChangeType, index: Int)](./init%28object,type,index%29.md)
  Creates a change object that represents inserting or removing an object from an ordered collection at a specific index.
- [init(object: Any?, type: NSCollectionChangeType, index: Int, associatedIndex: Int)](./init%28object,type,index,associatedindex%29.md)
  Creates a change object that represents inserting, removing, or moving an object from an ordered collection at a specific index.
- [+ changeWithObject:type:index:associatedIndex:](./changewithobject_type_index_associatedindex_.md)
  Creates an change object that represents inserting or removing an object from an ordered collection at a specific index, matched with an associated location that infers a move within the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsorderedcollectionchange/changewithobject:type:index:)*